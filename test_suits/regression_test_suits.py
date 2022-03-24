import unittest

from tests.test_login_google_form import TestGoogleForm

login = unittest.TestLoader().loadTestsFromTestCase(TestGoogleForm)
regression_suit = unittest.TestSuite([login])
unittest.TextTestRunner().run(regression_suit)