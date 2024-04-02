from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Infra.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class SearchPage(BasePage):

    SEARCH = "//div[@aria-label='Search']"

    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.SEARCH)))

    def click_on_search(self):
        self.search_input.click()

    def is_display_search_button(self):
        return self.search_input.is_displayed()

    def fill_search_input(self, text):
        self.search_input.send_keys(text)

    def press_enter_on_search_input(self):
        self.search_input.send_keys(Keys.RETURN)

    def search_flow(self, text):
        self.click_on_search()
        self.fill_search_input(text)
        self.press_enter_on_search_input()
        return True
