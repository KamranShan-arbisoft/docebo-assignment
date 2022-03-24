
import os
from pages.common.base_page import BasePage
from pages.common.selectors import LoginPageSelector
from pages.common.selectors import NextButton
from pages.utils.utils import Utils


class LoginPage(BasePage):

    def login(self):
        email = os.environ["EMAIL"]
        password = os.environ['PASSWORD']
        self.visibility_of_element_located(LoginPageSelector.email_id)
        self.presence_of_element_located_click(LoginPageSelector.email_id, email)
        Utils.next_page(self, NextButton.next_btn_login_page)
        self.visibility_of_element_located(LoginPageSelector.password)
        self.presence_of_element_located_click(LoginPageSelector.password, password)
        Utils.next_page(self, NextButton.next_btn_login_page)