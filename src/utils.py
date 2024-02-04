import logging

from bs4 import BeautifulSoup
from requests import RequestException
from exceptions import ParserFindTagException


def get_response(session, url, encoding='utf-8'):
    try:
        response = session.get(url)
        response.encoding = encoding
        return response
    except RequestException:
        raise ConnectionError(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def get_soup(session, url):
    return BeautifulSoup(get_response(session, url).text, 'lxml')


def find_elements(soup, expression, single_tag=False):
    selected = (
        soup.select_one(expression) if single_tag else soup.select(expression)
    )
    if not selected:
        raise ParserFindTagException(f"Нет элементов по запросу: {expression}")
    return selected
