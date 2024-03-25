from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class SettingPage(BasePage):

    SETTING = "//span[text()='Settings']"

    def __init__(self, driver):
        super().__init__(driver)
        self.setting = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.SETTING)))

    def click_on_setting_button(self):
        self.setting.click()





