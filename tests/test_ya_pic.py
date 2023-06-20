from YandexPages import YaPicPage


def test_menu_button(browser):
    yandex_main = YaPicPage(browser)
    yandex_main.to_site()
    assert yandex_main.check_service_btns()

def test_open_ya_pic(browser):
    yandex_main = YaPicPage(browser)
    yandex_main.click_service_pic()
    assert browser.current_url == 'https://yandex.ru/images/'

def test_category_name(browser):
    yandex_main = YaPicPage(browser)
    category_name = yandex_main.check_popular_category()
    assert category_name[0] == category_name[1]

def test_open_pic(browser):
    yandex_main = YaPicPage(browser)
    picture = yandex_main.open_first_pic()
    assert picture.is_displayed()

