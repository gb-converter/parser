
import requests
from bs4 import BeautifulSoup
import json
import os


def get_html(url):                                                          # запрос на сервер и получение ответа в html
    req = requests.get(url)
    return req.text


def write_json(data):                                                             # создание пути сохранения и файл json
    file_name = 'data_file.json'
    home_dir = os.getcwd()
    try:
        answer = input(f'(yes) сохранить в *{home_dir}*, или (no) изменить путь сохранения: ')
        if answer == 'no':
            path_dir_name = input(f'Укажите путь сохранения файла {file_name}: ')

            if not os.path.exists(path_dir_name):                                  # Если пути не существует создаем его
                os.makedirs(path_dir_name)

            full_file_name = os.path.join(path_dir_name, file_name)

            with open(full_file_name, "w", encoding='UTF-8') as file:                      # создание json в новом месте
                json.dump(data, file, indent=2, ensure_ascii=False)
            print(f'Сохранен в *{full_file_name}*')

        elif answer == 'yes':
            with open(file_name, "w", encoding='UTF-8') as file:                        # создание json в корневой папке
                json.dump(data, file, indent=2, ensure_ascii=False)
            print(f'Сохранен в *{home_dir}*')
        else:
            print('Пожалуйста введите (yes) или (no).')
            write_json(data)

    except FileNotFoundError:
        print(f'Системе не удается найти указанный путь: {path_dir_name}\nУкажите верный путь.')
        write_json(data)


def get_data(html):                                                       # сам парсинг и создание словаря с результатом

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
                    'Единица': unit,
                    'Валюта': currency,
                    'Курс': rate
                    }
                }
            dict_.update(data)

    write_json(dict_)


def main():                                                                              # адрес сервера, вызов функиций
    url = 'https://www.cbr.ru/currency_base/daily/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
