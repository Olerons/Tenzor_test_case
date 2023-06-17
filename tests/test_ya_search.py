from YandexPages import  YaSearchPage



def test_ya_search(browser):
    yandex_main = YaSearchPage(browser)
    yandex_main.to_site()
    assert yandex_main.enter_word("Тензор")

    elements_suggest = yandex_main.view_suggest_field()
    assert elements_suggest

    yandex_main.click_search_button()
    assert yandex_main.view_search_result()
