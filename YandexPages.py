from BaseApp import BasePage
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


class YandexSearchLocators:
    LOCATOR_YA_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YA_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YA_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")

class YaSearchPage(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YA_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def view_suggest_field(self):
        suggest_field = self.find_element(YandexSearchLocators.LOCATOR_YA_SUGGEST,time=5)
        return suggest_field.text

    def click_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YA_SEARCH_BUTTON).click()


driver = webdriver.Firefox()
#driver.get('https://yandex.ru')

main = YaSearchPage(driver)
main.to_site()
main.enter_word("Тензор")
x = main.view_suggest_field()
print(x)
print(x.split())

driver.quit()