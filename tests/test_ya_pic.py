from YandexPages import YaPicPage
from time import time

def test_menu_button(browser):
    yandex_main = YaPicPage(browser)
    yandex_main.to_site()
    yandex_main.click_search_field()

    assert 1