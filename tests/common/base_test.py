import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    __driver = None

    @classmethod
    def setUpClass(cls):
        cls.__driver = webdriver.Chrome()

    @property
    def driver(self):
        return self.__driver

