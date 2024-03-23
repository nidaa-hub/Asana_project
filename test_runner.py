import unittest

from Test.login_test import Asana_Page_Test


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Asana_Page_Test)
    for i in range(20):
        result = unittest.TextTestRunner().run(suite)
