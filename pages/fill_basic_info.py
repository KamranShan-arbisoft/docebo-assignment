
from pages.common.selectors import BasicInfoSelector
from pages.common.base_page import BasePage
import os
from selenium.webdriver.common.by import By


class BasicInformation(BasePage):

    def fill_basic_info(self):
        # Read data from csv files and store into personal data
        name = self.form_data[1]
        email = self.form_data[2]
        cnic = self.form_data[3]
        # Read phone number from env variables
        phone_num = os.environ["PHONE"]
        self.visibility_of_element_located(BasicInfoSelector.phone_number)
        self.element_to_be_clickable(BasicInfoSelector.phone_number, phone_num)
        self.driver.find_element(By.CSS_SELECTOR, BasicInfoSelector.cnic_num).send_keys(cnic[1])
        self.driver.find_element(By.CSS_SELECTOR, BasicInfoSelector.name).send_keys(name[1])
        self.driver.find_element(By.CSS_SELECTOR, BasicInfoSelector.email).send_keys(email[1])