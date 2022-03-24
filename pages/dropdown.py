
from pages.common.selectors import DropDownPagesSelector
from pages.common.base_page import BasePage
from selenium.webdriver.common.by import By


class DropDown(BasePage):

    def drop_capital_of_pakistan(self, capital_city_pak):
        self.visibility_of_element_located(DropDownPagesSelector.drop_of_pakistan)
        self.presence_of_element_located(DropDownPagesSelector.drop_of_pakistan)
        self.driver.find_element(By.CSS_SELECTOR, DropDownPagesSelector.drop_of_pakistan).click()
        self.visibility_of_element_located_click(DropDownPagesSelector.capital_of_pakistan.format(capital_city_pak))
        self.visibility_of_element_located('div[aria-selected="true"]')

    def drop_capital_of_punjab(self, capital_city_pun):
        self.visibility_of_element_located(DropDownPagesSelector.drop_of_punjab)
        self.presence_of_element_located(DropDownPagesSelector.drop_of_punjab)
        self.driver.find_element(By.CSS_SELECTOR, DropDownPagesSelector.drop_of_punjab).click()
        self.visibility_of_element_located_click(DropDownPagesSelector.capital_of_pakistan.format(capital_city_pun))
        self.visibility_of_element_located('div[aria-selected="true"]')
