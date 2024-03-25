from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class DisplayPage(BasePage):

    DISPLAY = "//span[text()='Display']"
    THEME = "//div[@id='profile_settings_color_theme_preference_select']"
    DARK_MODE = "//span[text()='Dark']"

    def __init__(self, driver):
        super().__init__(driver)
        self.display = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.DISPLAY)))
        self.theme = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.THEME)))
        self.dark_mode = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.DARK_MODE)))

    def click_on_display_button(self):
        self.display.click()

    def click_on_theme_button(self):
        self.theme.click()

    def click_on_dark_mode(self):
        self.dark_mode.click()

