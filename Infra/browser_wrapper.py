from selenium import webdriver
from Utils.config_loader import ConfigLoader


class BrowserWrapper:

    def __init__(self):
        self.driver = None
        self.configloader = ConfigLoader()
        self.config = self.configloader.load_config()
        print("test start")

    def create_options(self, browser_type):
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_type.lower() == 'edge':
            options = webdriver.EdgeOptions()
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return options

    def get_driver(self, browser='chrome'):
        if self.config["grid"]:
            options = self.set_up_capabilities(browser)
            self.driver = webdriver.Remote(command_executor=self.config["hub"], options=options)
        else:

            if browser.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser.lower() == 'edge':
                self.driver = webdriver.Edge()

        url = self.config["url"]
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver

    def set_up_capabilities(self, browser_type):
        options = None
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_type.lower() == 'edge':
            options = webdriver.EdgeOptions()
        if options is not None:
            platform_name = self.config["platform"]
            options.add_argument(f'--platformName={platform_name}')
            return options
        else:
            raise ValueError("Unsupported browser type")
