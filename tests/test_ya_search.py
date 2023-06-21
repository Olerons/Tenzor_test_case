from YandexPages import  YaSearchPage
import allure
import logging


@allure.step("Проверяем, появляется поле ввода запросов на ya.ru")
def test_search_field(browser):
    yandex_main = YaSearchPage(browser)
    yandex_main.to_site()
    assert yandex_main.check_search_field()


@allure.step("Проверяем, можем ли мы ввести поисковый запрос в поле запросов")
def test_input_word(browser):
    yandex_main = YaSearchPage(browser)
    assert yandex_main.enter_word("Тензор")


@allure.step("Проверяем, появляются ли подсказки при вводе запроса")
def test_suggest_list(browser):
    yandex_main = YaSearchPage(browser)
    elements_suggest = yandex_main.view_suggest_field()
    assert elements_suggest


@allure.step("Проверяем, отображается ли страница с результатами поиска")
def test_search_result(browser):
    yandex_main = YaSearchPage(browser)
    yandex_main.click_search_button()
    assert yandex_main.view_search_result()


@allure.step("Проверяем, что первая ссылка (не считая рекламы) ведет на tensor.ru")
def test_first_href(browser):
    yandex_main = YaSearchPage(browser)
    first_href = yandex_main.view_first_href()
    assert first_href == "https://tensor.ru/"
