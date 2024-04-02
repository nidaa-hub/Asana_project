import time
import unittest

from jirafile import JiraReport
from Utils.read_from_env import Credentials
from Utils.asana_login import AsanaLogin
from Infra.browser_wrapper import BrowserWrapper
from Logic.UI_logic.display_page import DisplayPage
from Logic.UI_logic.home_page import HomePage
from Logic.UI_logic.setting_page import SettingPage


class Asana_non_functional_Test(unittest.TestCase):
    def setUp(self):
        self.data = Credentials()
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.login = AsanaLogin(self.driver)
        self.login.asana_login_with_email()
        time.sleep(5)
        self.asana_home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
        if not self._outcome.success:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in non_functional_test"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))

    def test_change_to_dark_mode(self):
        self.asana_home_page.click_on_profile_icon()
        time.sleep(7)
        self.asana_setting_page = SettingPage(self.driver)
        self.asana_setting_page.click_on_setting_button()
        time.sleep(7)
        self.asana_display = DisplayPage(self.driver)
        self.asana_display.change_to_dark_mode()
        self.check_mode = self.asana_display.dark_mode_is_displayed()
        self.assertTrue(self.check_mode, "the mode is Light")

    def test_change_website_language(self):
        self.asana_home_page.click_on_profile_icon()
        time.sleep(5)
        self.asana_setting_page = SettingPage(self.driver)
        self.asana_setting_page.click_on_setting_button()
        time.sleep(5)
        self.asana_display = DisplayPage(self.driver)
        self.asana_display.change_to_spanish_language()
        self.check_language = self.asana_display.spanish_language_is_displayed()
        self.assertTrue(self.check_language, "the language is't spanish")
