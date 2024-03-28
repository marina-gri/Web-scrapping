from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


def gen_headers():
    headers = Headers(browser='chrome', os='win')
    return headers.generate()


url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
response = requests.get(url=url, headers=gen_headers())

html_data = response.text
main_soup = BeautifulSoup(html_data, 'lxml')

vacancy_tags = main_soup.find_all('div', class_='vacancy-serp-item__layout')

result = []
for vacancy_tag in vacancy_tags:
    position_tag = vacancy_tag.find('span', class_='serp-item__title-link serp-item__title')
    a_tag = vacancy_tag.find('a', class_='bloko-link')
    salary_tag = vacancy_tag.find('span', class_='bloko-header-section-2')
    company_tag = vacancy_tag.find('a', class_='bloko-link bloko-link_kind-tertiary')
    city_tag = vacancy_tag.find('div', class_='bloko-text')

    position = position_tag.text
    link = a_tag['href']
    company = company_tag.text.strip()
    city = city_tag.text
    print(city)

    some_list = [city]
    print(some_list)

    if salary_tag is not None:
        salary = salary_tag.text
    else:
        salary = "НЕ УКАЗАНО"

    if "python" in position.lower():
        result.append({
            'position': position,
            'link': link,
            'company': company,
            'city': city,
            'salary': salary
        })


pprint(result)
