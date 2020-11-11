
import requests
from bs4 import BeautifulSoup
import json
import os


# запрос на сервер и получение ответа в html
def get_html(url):
    req = requests.get(url)
    return req.text


# запись в json
def write_json(data):
    with open("data_file.json", "w", encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


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

    write_json(dict_)


#  адрес сервера, вызов функиций, место где создается json
def main():
    url = 'https://www.cbr.ru/currency_base/daily/'
    get_data(get_html(url))
    way = os.getcwd()
    print(f'data_file.json сохранен в {way}')


if __name__ == '__main__':
    main()
