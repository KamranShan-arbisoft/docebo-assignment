from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.common.selectors import NextButton
from pages.common.base_page import BasePage
import requests


class Utils(BasePage):

    def next_page(self, elm):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, elm)))
        element.click()

    def view_submit_score(self, elm):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, elm)))
        element.click()

    def form_questions_text(self):
        wait = WebDriverWait(self.driver, 10)
        question_headings = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, NextButton.form_questions)))
        return question_headings

    def response_of_request(self):
        url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/formResponse'
        response = requests.post(url)
        return response
