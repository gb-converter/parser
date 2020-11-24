
import requests
from bs4 import BeautifulSoup
import json
import os
import argparse
import logging
import logs.config_log


# Инициализация клиентского логера
PARSER_LOGGER = logging.getLogger('parser')

# запрос на сервер и получение ответа в html
def get_html(url):
    req = requests.get(url)
    PARSER_LOGGER.info(f'Ответ от сайта {url} получен')
    return req.text


# запись в json
def write_json(data, way):
    try:
        with open(os.path.join(way, "data_file.json"), "w", encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'data_file.json сохранен в {way}')
        PARSER_LOGGER.info(f'data_file.json сохранен в {way}')
    except:
        print(f'не удалось сохранить файл в {way}')
        PARSER_LOGGER.critical(f'не удалось сохранить файл в {way}')

# сам парсинг и создание словаря с результатом
def get_data(html):

    data = BeautifulSoup(html, 'lxml')

    tr_data = data.find('table', class_='data').find('tbody').find_all('tr')
    date = data.find('div', class_='datepicker-filter').find('button', class_='datepicker-filter_button').text

    dict_ = {'Date': date}

    for tr in tr_data:
        td_data = tr.find_all('td')
        if len(td_data) != 0:
            num_code = td_data[0].text
            char_code = td_data[1].text
            unit = td_data[2].text
            currency = td_data[3].text
            rate = td_data[4].text

            data = {
                char_code: {
                    'Цифр. код': num_code,
                    'Букв. код': char_code,
                    'Единица': unit,
                    'Валюта': currency,
                    'Курс': rate
                    }
                }
            dict_.update(data)
    PARSER_LOGGER.info(f'Словарь с результами сохранен')
    return dict_


#  адрес сервера, путь для сохранения данных, вызов функций, место где создается json
def main():
    url = 'https://www.cbr.ru/currency_base/daily/'
    PARSER_LOGGER.info(f'Запущен парсинг сайта {url}')
    
    # добавляем возможность указывать путь, по которому будем сохранять файл с данными
    arg_ability = argparse.ArgumentParser()
    arg_ability.add_argument('--path', type=str, help='the path to save the file with data')  # это необязательный аргумент
    way = arg_ability.parse_args().path
    
    way_is_default = way is None  # True, если приложение запущено без параметра --path
    
    # если в параметрах запуска приложения был указан путь для сохранения файла с данными,
    # проверяем: существует ли указанный путь?, если нет - пытаемся создать недостающие директории
    if not way_is_default:
        if not os.path.isdir(way):
            try:
                os.makedirs(way)
            except:
                way_is_default = True
            
    if way_is_default:
        way = os.getcwd()  # по-умолчанию, директория сохранения файла - текущая
        
    write_json(get_data(get_html(url)), way)

    PARSER_LOGGER.info(f'Завершен парсинг сайта')


    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # вычленяет буквенный код из словаря
    parsed_cbr = get_data(get_html('https://www.cbr.ru/currency_base/daily/'))
    #   parsed_cbr   =   {'Date': '21.11.2020', 'AUD': {'Цифр. код': '036', 'Букв. код': 'AUD', 'Единица': '1', 'Валюта': 'Австралийский доллар', 'Курс': '55,4127'},
    for value in parsed_cbr.values():
        if type(value) is dict:
            letter_code = value['Букв. код']
            # print(letter_code)

    # парсит wiki | ищет icon
    html_wiki = 'https://en.wikipedia.org/wiki/List_of_circulating_currencies'
    data_wiki = BeautifulSoup(get_html(html_wiki), 'lxml')
    date_icon = data_wiki.find('table').find('tbody').find_all('tr')  # date_icon - все tr

    dict_with_icon = {}
    switch = 0  # для строк, где первый столбец сконкатенирован с предыдущей строкой. switch = 11or2 если rowspan='2'or'3'

    # цикл вычленяет иконки и коды
    for td in date_icon[1:]:
        if switch == 0:
            icon = td.find_all('td')[2].text[:-1]
            ico_code = td.find_all('td')[3].text[:-1]
        elif switch == 1 or switch == 2:
            icon = td.find_all('td')[1].text[:-1]
            ico_code = td.find_all('td')[2].text[:-1]
            switch -= 1

        # если строка с конкатенацией то в след. строке иконка будет на -1 позиции
        if td.find('td', rowspan='2') != None:
            switch = 1
        elif td.find('td', rowspan='3') != None:
            switch = 2

        # заполняем новый словарь, состоящ. из иконок из буквенных кодов
        if ico_code != r'(none)\n':  # !!! хочу избавиться от пустых значений в словаре
            new_data = {
                ico_code: {
                    'Знак': icon,
                    # 'Букв. код': ico_code,
                }
            }
        dict_with_icon.update(new_data)

    # print(dict_with_icon)

    # объединение двух словарей
    def merge(d1, d2):
        d = {k: d1[k] for k in set(d1) - set(d2)}
        d.update({k: d2[k] for k in set(d2) - set(d1)})
        for k in set(d2) & set(d1):
            assert isinstance(d1[k], dict) == isinstance(d2[k], dict), "inconsistent dicts"
            if isinstance(d1[k], dict):
                d[k] = merge(d1[k], d2[k])
            else:
                d[k] = d2[k]  # keep only the second value, but we can keep a list if needed
        return d

    print(merge(parsed_cbr, dict_with_icon))



if __name__ == '__main__':
    main()
