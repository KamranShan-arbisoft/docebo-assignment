
from datetime import datetime
from pages.common.selectors import DateAndTimeSelector
from pages.common.base_page import BasePage
from selenium.webdriver.common.by import By


class DateAndTime(BasePage):

    def current_time(self):
        hh = datetime.now().strftime("%H")
        mint = datetime.now().strftime("%M")
        self.visibility_of_element_located(DateAndTimeSelector.hours)
        self.driver.find_element(By.CSS_SELECTOR, DateAndTimeSelector.hours).send_keys(hh)
        self.driver.find_element(By.CSS_SELECTOR, DateAndTimeSelector.minut).send_keys(mint)

    def current_date(self):
        mm = datetime.now().month
        dd = datetime.now().day
        yy = datetime.now().year
        self.visibility_of_element_located(DateAndTimeSelector.date_elm)
        self.driver.find_element(By.CSS_SELECTOR, DateAndTimeSelector.date_elm).send_keys(dd,mm,yy)

    def submitForm(self):
        self.driver.find_element(By.CSS_SELECTOR, DateAndTimeSelector.submit_btn).click()