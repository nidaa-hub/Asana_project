from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Infra.base_page import BasePage


class DisplayPage(BasePage):

    DISPLAY = "//span[text()='Display']"
    THEME = "//div[@id='profile_settings_color_theme_preference_select']"
    DARK_MODE = "//span[text()='Dark']"
    LANGUAGE = "//div[@id='profile_settings_locale_select']"
    SPANISH = "//span[text()='Español']"

    def __init__(self, driver):
        super().__init__(driver)
        self.display = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.DISPLAY)))
        self.theme = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.THEME)))
        self.Language = WebDriverWait(self._driver, 20).until(EC.presence_of_element_located((By.XPATH, self.LANGUAGE)))
        self.spanish = None

    def click_on_display_button(self):
        self.display.click()

    def click_on_theme_button(self):
        self.theme.click()
        self.dark_mode = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.DARK_MODE)))

    def click_on_dark_mode(self):
        self.dark_mode.click()

    def change_to_dark_mode(self):
        self.click_on_display_button()
        self.click_on_theme_button()
        self.click_on_dark_mode()

    def dark_mode_is_displayed(self):
        return self.dark_mode

    def click_on_language_website(self):
        self.Language.click()
        self.spanish = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.SPANISH)))

    def choose_spanish_language(self):
        self.spanish.click()

    def change_to_spanish_language(self):
        self.click_on_language_website()
        self.choose_spanish_language()

    def spanish_language_is_displayed(self):
        return self.spanish()

