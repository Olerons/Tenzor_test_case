from BaseApp import BasePage
from selenium.webdriver.common.by import By
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