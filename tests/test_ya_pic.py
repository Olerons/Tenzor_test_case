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

def test_open_second_pic(browser):
    yandex_main = YaPicPage(browser)
    first_pic = yandex_main.get_original_pic()
    browser.add_cookie({'name': 'fp_test', 'first_pic': first_pic})
    yandex_main.next_pic()
    second_pic = yandex_main.get_original_pic()
    assert first_pic != second_pic

def test_check_prev_pic(browser):
    yandex_main = YaPicPage(browser)
    yandex_main.prev_pic()
    prev_pic = yandex_main.get_original_pic()
    first_pic = browser.get_cookies()[-1]
    assert prev_pic == first_pic
