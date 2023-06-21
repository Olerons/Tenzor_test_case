from YandexPages import YaPicPage
import allure
import logging

href_first_pic = ''


@allure.step("Проверяем, появляется ли кнопка с сервисами Яндекс")
def test_menu_button(browser):
    yandex_main = YaPicPage(browser)
    yandex_main.to_site()
    assert yandex_main.check_service_btns()


@allure.step("Проверяем, получилось ли перейти на сервис 'картинки' при нажатии на кнопку")
def test_open_ya_pic(browser):
    yandex_main = YaPicPage(browser)
    yandex_main.click_service_pic()
    assert browser.current_url == 'https://yandex.ru/images/'


@allure.step("Проверяем, отображается ли в поле поиска название категории картинок, при нажатии")
def test_category_name(browser):
    yandex_main = YaPicPage(browser)
    category_name = yandex_main.check_popular_category()
    assert category_name[0] == category_name[1]


@allure.step("Проверяем, отображается ли картинка, при нажатии на нее")
def test_open_pic(browser):
    yandex_main = YaPicPage(browser)
    picture = yandex_main.open_first_pic()
    assert picture.is_displayed()


@allure.step("Проверяем, меняется ли картинка, при переходе к следующей")
def test_open_second_pic(browser):
    global href_first_pic

    yandex_main = YaPicPage(browser)
    href_first_pic = yandex_main.get_original_pic()
    yandex_main.next_pic()
    second_pic = yandex_main.get_original_pic()
    assert href_first_pic != second_pic


@allure.step("Проверяем, возвращается ли та же самая картинка, при переходе назад")
def test_check_prev_pic(browser):
    global href_first_pic

    yandex_main = YaPicPage(browser)
    yandex_main.prev_pic()
    prev_pic = yandex_main.get_original_pic()

    assert prev_pic == href_first_pic

