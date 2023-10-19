import time
import string
import requests
from bs4 import BeautifulSoup


def remove_whitespace(text: str) -> str:
    for whitespace in string.whitespace:
        text = text.replace(whitespace, '')
    return text


def get_carbon_level():
    try:
        # raise Exception('This exception will be removed before deployment')
        start_time = time.time()
        html = requests.get(
            'https://climate.nasa.gov/vital-signs/carbon-dioxide/').text
        end_time = time.time()
        soup = BeautifulSoup(html, 'html.parser')
        value_text = remove_whitespace(soup.select_one('.value').text)
        value_text = value_text.replace('ppm', '') + ' ppm'
        month_year_text = remove_whitespace(
            soup.select_one('.month_year').text)
        space_added = False
        new_month_year_text = ''
        for char in month_year_text:
            if char in string.digits and not space_added:
                space_added = True
                new_month_year_text += f' {char}'
            else:
                new_month_year_text += char
        return {
            'status': True,
            'carbonLevel': value_text,
            'measured': new_month_year_text,
            'durationSeconds': end_time - start_time,
        }
    except Exception as error:
        return {
            'status': False,
            'error': repr(error),
        }


print(get_carbon_level())
