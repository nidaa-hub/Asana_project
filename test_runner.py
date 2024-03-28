from typing import Type
import unittest
from concurrent.futures import ThreadPoolExecutor
from Utils.config_loader import ConfigLoader
from Test.UI_test.non_functional_test import Asana_non_functional_Test
from Test.UI_test.task_test import Asana_Task_Test
from Test.API_test.asana_api_test import MainTest
from Test.API_test.section_test import SectionTest
from Test.UI_test.task_test import Asana_Task_Test


serial_cases = [Asana_non_functional_Test, Asana_Task_Test, MainTest, SectionTest, Asana_Task_Test]
parallel_cases = [Asana_non_functional_Test,Asana_Task_Test, MainTest, SectionTest, Asana_Task_Test]
test_cases = [Asana_non_functional_Test,Asana_Task_Test, MainTest, SectionTest ,Asana_Task_Test]
demo_cases = [Asana_non_functional_Test,Asana_Task_Test, MainTest, SectionTest, Asana_Task_Test]


def run_tests_for_browser(browser: str, test_case: Type[unittest.TestCase]):
    test_case.browser = browser
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner().run(test_suite)


def run_tests_for_browser_serial(browsers, serial_tests):
    for test in serial_tests:
        for browser in browsers:
            run_tests_for_browser(browser, test)


def run_tests_for_browser_parallel(browsers, parallel_tests):
    tasks = [(browser, test_case) for browser in browsers for test_case in parallel_tests]
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(run_tests_for_browser, browser, test_case) for browser, test_case in tasks]


if __name__ == "__main__":
    config_loader = ConfigLoader()
    config = config_loader.load_config()
    is_parallel = config['parallel']
    is_serial = not config['parallel']
    browsers = config["browser_types"]
    grid_url = config["hub"]
   # if is_parallel:
   #     run_tests_for_browser_parallel(browsers, parallel_cases)
  #      run_tests_for_browser_serial(browsers, serial_cases)
   # elif is_serial:
    #    run_tests_for_browser_serial(browsers, test_cases)
  #  else:
    run_tests_for_browser_serial(browsers, demo_cases)

