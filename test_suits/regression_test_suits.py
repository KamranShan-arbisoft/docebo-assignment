import unittest

from tests.test_login_google_form import TestGoogleForm
from tests.test_negative_google_form import TestNegativeGoogleForm

positive_test = unittest.TestLoader().loadTestsFromTestCase(TestGoogleForm)
negative_test = unittest.TestLoader().loadTestsFromTestCase(TestNegativeGoogleForm)
regression_suit = unittest.TestSuite([positive_test, negative_test])
unittest.TextTestRunner().run(regression_suit)