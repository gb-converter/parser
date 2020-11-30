
import requests
from bs4 import BeautifulSoup
import json
import os
import argparse

# запрос на сервер и получение ответа в html
def get_html(url):
    req = requests.get(url)
    return req.text


# запись в json
def write_json(data, way):
    try:
        with open(os.path.join(way, "data_file.json"), "w", encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'data_file.json сохранен в {way}')
    except:
        print(f'не удалось сохранить файл в {way}')

# сам парсинг и создание словаря с результатом
def get_data(html):

    data = BeautifulSoup(html, 'lxml')

    tr_data = data.find('table', class_='data').find('tbody').find_all('tr')
    date = data.find('div', class_='datepicker-filter').find('button', class_='datepicker-filter_button').text

    dict_ = {'Date': date}

    data_s = BeautifulSoup(get_html('https://ru.currencyrate.today/different-currencies'), 'lxml')
    tr_s_data = data_s.find('table', class_='table table-striped table-hover').find('tbody').find_all('tr')
    dict_s = {}
    for tr_s in tr_s_data:
        td_s_data = tr_s.find_all('td')
        if len(td_s_data) != 0:
            ISO_code = td_s_data[0].text
            if dict_s.get(ISO_code) is None:
                dict_s[ISO_code] = td_s_data[3].text
    print(dict_s)
    print(len(dict_s))
    for tr in tr_data:
        td_data = tr.find_all('td')
        if len(td_data) != 0:
            num_code = td_data[0].text
            char_code = td_data[1].text
            unit = td_data[2].text
            currency = td_data[3].text
            rate = td_data[4].text
            symbol = dict_s.get(char_code)
            if symbol is None:
                symbol = ''
                print('symbol for', char_code, 'is None')

            data = {
                char_code: {
                    'Цифр. код': num_code,
                    'Символ': symbol,
                    'Единица': unit,
                    'Валюта': currency,
                    'Курс': rate
                    }
                }
            dict_.update(data)
    print(len(dict_))
    return dict_


#  адрес сервера, путь для сохранения данных, вызов функций, место где создается json
def main():
    url = 'https://www.cbr.ru/currency_base/daily/'
    
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


if __name__ == '__main__':
    main()
