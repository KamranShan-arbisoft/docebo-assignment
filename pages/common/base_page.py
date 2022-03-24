import csv
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver: WebDriver):
        self.base_url = "https://docs.google.com/forms/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/viewform"
        self.driver = driver
        self.form_data = self.read_csv()

    def read_csv(self):
        with open('../pages/common/answer_list.csv', 'r') as csvfile:
            data = list(csv.reader(csvfile))
            return data

    def write_csv(self, final_ans):
        data = self.form_data
        with open('../pages/common/answer_list.csv', 'w+') as f:
            writer = csv.writer(f)
            writer.writerow(['Question', 'Random Answer', 'Correct Answer'])
            for index, valuee in enumerate(data[1:]):
                valuee[2] = final_ans[index]
                writer.writerow(valuee)

    def creat_csv(self, final_ans):
        try:
            mydict = final_ans
            with open('../pages/common/answer_list.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=mydict)
                writer.writeheader()
                writer.writerows([mydict])
        except FileNotFoundError as e:
            print(e)

    def visibility_of_element_located(self, elm):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, elm)))

    def invisibility_of_element_located(self, elm):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, elm)))

    def presence_of_element_located(self, elm):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, elm)))

    def presence_of_element_located_click(self, elm, keys=False):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, elm)))
        element.click()
        if keys:
            element.click()
            element.send_keys(keys)

    def element_to_be_clickable(self, elm, keys=False):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, elm)))
        element.click()
        if keys:
            element.click()
            element.send_keys(keys)

    def visibility_of_element_located_click(self, elm, keys=False):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, elm)))
        element.click()
        if keys:
            element.send_keys(keys)