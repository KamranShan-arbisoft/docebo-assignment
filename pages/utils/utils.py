
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.common.base_page import BasePage


class Utils(BasePage):

    def next_page(self, elm):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, elm)))
        element.click()
