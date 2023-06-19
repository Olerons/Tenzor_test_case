from YandexPages import  YaSearchPage
from selenium.webdriver.common.by import By

def test_search_field(browser):
    yandex_main = YaSearchPage(browser)
    yandex_main.to_site()
    assert yandex_main.check_search_field()

def test_input_word(browser):
    yandex_main = YaSearchPage(browser)
    assert yandex_main.enter_word("Тензор")

def test_suggest_list(browser):
    yandex_main = YaSearchPage(browser)
    elements_suggest = yandex_main.view_suggest_field()
    assert elements_suggest

def test_search_result(browser):
    yandex_main = YaSearchPage(browser)
    yandex_main.click_search_button()
    assert yandex_main.view_search_result()

def test_first_href(browser):
    yandex_main = YaSearchPage(browser)
    first_href = yandex_main.view_first_href()
    assert first_href == "https://tensor.ru/"
