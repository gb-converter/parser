import requests
from bs4 import BeautifulSoup
import json
import os
import argparse
import logging
import logs.config_log


URL = 'https://www.cbr.ru/currency_base/daily/'

# Инициализация клиентского логера
PARSER_LOGGER = logging.getLogger('parser')

# запрос на сервер и получение ответа в html
def get_html(url):
    try:
        req = requests.get(url)
        if req.status_code == 200:
            PARSER_LOGGER.info(f'Ответ от сайта {url} успешно получен')
            return req.text
        else:
            PARSER_LOGGER.critical(f'Ответ от сайта {url} не получен, код ошибки {req.status_code}')
            return None
    except Exception:
        PARSER_LOGGER.critical(f'Адрес {url} задан неверно или настройки сервера изменены')
        return None


# запись в json
def write_json(data, way):
    try:
        with open(os.path.join(way, "data_file.json"), "w", encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'data_file.json сохранен в {way}')
        PARSER_LOGGER.info(f'data_file.json сохранен в {way}')
        return True
    except Exception:
        print(f'не удалось сохранить файл в {way}')
        PARSER_LOGGER.critical(f'не удалось сохранить файл в {way}')
        return False

# сам парсинг и создание словаря с результатом
def get_data(html):

    data = BeautifulSoup(html, 'lxml')

    try:
        tr_data = data.find('table', class_='data').find('tbody').find_all('tr')
        date = data.find('div', class_='datepicker-filter').find('button', class_='datepicker-filter_button').text
    except Exception:
        PARSER_LOGGER.critical(f'Структура страницы изменена, таблицы больше нет')
        return None

    dict_ = {'Date': date}
    strError = ''

    for tr in tr_data:
        td_data = tr.find_all('td')
        if len(td_data) != 0:
            try:
                strError = 'цифровой код'
                num_code = int(td_data[0].text)
                strError = 'букв. код'
                if not any(map(str.isdigit, td_data[1].text)):
                    char_code = td_data[1].text
                else:
                    raise TypeError
                strError = 'количество единиц'
                unit = int(td_data[2].text)
                strError = 'валюту'
                if not any(map(str.isdigit, td_data[3].text)):
                    currency = td_data[3].text
                strError = 'курс'
                float(td_data[4].text.replace(',', '.'))
                rate = td_data[4].text
            except Exception:
                PARSER_LOGGER.critical(f'Структура страницы изменена, не удалось извлечь {strError}')
                return None
            data = {
                char_code: {
                    'Цифр. код': str(num_code),
                    'Единица': str(unit),
                    'Валюта': currency,
                    'Курс': rate
                    }
                }
            dict_.update(data)
    data = {
        'RUB': {
            'Цифр. код': str(643),
            'Единица': str(1),
            'Валюта': 'Российский рубль',
            'Курс': str(1)
        }
    }
    dict_.update(data)
    PARSER_LOGGER.info(f'Словарь с результами сохранен')
    return dict_


#  адрес сервера, путь для сохранения данных, вызов функций, место где создается json
def main():
    PARSER_LOGGER.info(f'Запущен парсинг сайта {URL}')
    
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

    answer_data = get_html(URL)
    if answer_data is not None:
        dict_to_write = get_data(answer_data)
        if dict_to_write is not None:
            write_json(dict_to_write, way)
            PARSER_LOGGER.info(f'Завершен парсинг сайта')


if __name__ == '__main__':
    main()
