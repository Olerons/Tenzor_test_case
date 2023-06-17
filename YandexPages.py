from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class YandexSearchLocators:
    LOCATOR_YA_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YA_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YA_SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOCATOR_YA_SEARCH_RESULT = (By.CLASS_NAME, "content__left")

class YaSearchPage(BasePage):
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