from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class YandexSearchLocators:
    LOCATOR_YA_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YA_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YA_SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOCATOR_YA_SEARCH_RESULT = (By.CLASS_NAME, "content__left")
    LOCATOR_YA_FIRST_RESULT = (By.XPATH, "//li[@data-cid='0']")
    LOCATOR_YA_FIRST_RESULT_CHECK_AD = (By.XPATH, "//*[@id='search-result']/li[1]/div/div[3]/div[1]/span/span[1]")
    LOCATOR_YA_FIRST_RESULT_IF_AD = (By.XPATH, "//li[@data-cid='1']")
    LOCATOR_YA_FIRST_RESULT_HREF = (By.XPATH, "//*[@id='search-result']/li[1]/div/div[2]/div[1]/a")

    LOCATOR_YA_SERVICE_BUTTONS = (By.CLASS_NAME, "services-suggest__list")
    LOCATOR_YA_SERVICE_BUTTON_ALL = (By.CLASS_NAME, "services-suggest__list-item-more")
    LOCATOR_YA_SERVICE_BUTTON_PICTURE = (By.XPATH, "//a[@aria-label='Картинки']")
    LOCATOR_YA_PICTURE_NAV_TAB = (By.XPATH, "//*[@role='main']")
    LOCATOR_YA_PICTURE_POPULAR_REQUESTS = (By.XPATH, "//div[@class='PopularRequestList']/div[1]")
    LOCATOR_YA_PICTURE_INPUT_BOX = (By.XPATH, "//span[@class='input__box']/input")
    LOCATOR_YA_PICTURE_FIRST_PIC = (By.CLASS_NAME, "serp-item__preview")
    LOCATOR_YA_PICTURE_OPENED_PIC = (By.CLASS_NAME, "MMImage-Preview")
    LOCATOR_YA_PICTURE_GALLERY = (By.TAG_NAME, "body")
    LOCATOR_YA_PICTURE_CHECK_AD = (By.CLASS_NAME, "DirectLabel DirectOffersHeader-Ad")
    LOCATOR_YA_PICTURE_FIRST_PIC_IF_AD = (By.XPATH, "//div[@class='serp-controller__content']/div/div[2]")


class YaSearchPage(BasePage):
    def check_search_field(self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YA_SEARCH_FIELD)
        return search_field

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YA_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def view_suggest_field(self):
        suggest_field = self.find_element(YandexSearchLocators.LOCATOR_YA_SUGGEST,time=15)
        actions = ActionChains(self.driver)
        actions.move_to_element(suggest_field)
        actions.perform()

        return suggest_field

    def click_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YA_SEARCH_BUTTON).click()

    def view_search_result(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YA_SEARCH_RESULT)

    def view_first_href(self):
        first_result = self.find_element(YandexSearchLocators.LOCATOR_YA_FIRST_RESULT)
        try:
            if first_result.find_element(YandexSearchLocators.LOCATOR_YA_FIRST_RESULT_CHECK_AD).text == "Реклама":
                first_result = self.find_element(YandexSearchLocators.LOCATOR_YA_FIRST_RESULT_IF_AD)
        except Exception:
            first_result = self.find_element(YandexSearchLocators.LOCATOR_YA_FIRST_RESULT)

        href = first_result.find_element(*YandexSearchLocators.LOCATOR_YA_FIRST_RESULT_HREF).get_attribute("href")

        return str(href)


class YaPicPage(BasePage):
    def check_service_btns(self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YA_SEARCH_FIELD).click()
        service_btns = self.find_elements(YandexSearchLocators.LOCATOR_YA_SERVICE_BUTTONS)

        return service_btns

    def click_service_pic(self):
        service_all = self.find_element(YandexSearchLocators.LOCATOR_YA_SERVICE_BUTTON_ALL).click()
        pic_btn = self.find_element(YandexSearchLocators.LOCATOR_YA_SERVICE_BUTTON_PICTURE).click()
        self.switch_to_window()
        return self.find_element(YandexSearchLocators.LOCATOR_YA_PICTURE_NAV_TAB, time=15)

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_popular_category(self):
        popular_req = self.find_element(YandexSearchLocators.LOCATOR_YA_PICTURE_POPULAR_REQUESTS, time=15)
        popular_req.click()
        input_field = self.find_element(YandexSearchLocators.LOCATOR_YA_PICTURE_INPUT_BOX)
        return popular_req.text, input_field.get_attribute("value")

    def open_first_pic(self):
        try:
            if self.find_element(YandexSearchLocators.LOCATOR_YA_PICTURE_CHECK_AD, time=2).text.lower() == "реклама":
                self.find_element(YandexSearchLocators.LOCATOR_YA_PICTURE_FIRST_PIC_IF_AD, time=3).click()
            else:
                self.find_elements(YandexSearchLocators.LOCATOR_YA_PICTURE_FIRST_PIC, time=3)[0].click()
        except Exception:
            self.find_elements(YandexSearchLocators.LOCATOR_YA_PICTURE_FIRST_PIC, time=3)[0].click()

        self.first_pic = self.find_element(YandexSearchLocators.LOCATOR_YA_PICTURE_OPENED_PIC)
        return self.first_pic

    def get_original_pic(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YA_PICTURE_OPENED_PIC).get_attribute("src")

    def next_pic(self):
        self.find_element(YandexSearchLocators.LOCATOR_YA_PICTURE_GALLERY).send_keys(Keys.ARROW_RIGHT)

    def prev_pic(self):
        self.find_element(YandexSearchLocators.LOCATOR_YA_PICTURE_GALLERY).send_keys(Keys.ARROW_LEFT)