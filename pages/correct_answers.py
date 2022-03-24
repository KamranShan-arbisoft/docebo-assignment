from pages.common.selectors import CorrectAnswerSelectot
from pages.common.base_page import BasePage
from selenium.webdriver.common.by import By


class StoreCorrectAnswer(BasePage):

    def get_correct_answers(self):
        email = self.driver.find_element(By.CSS_SELECTOR, CorrectAnswerSelectot.email).text
        name = self.driver.find_element(By.CSS_SELECTOR, CorrectAnswerSelectot.name).text
        phone = self.driver.find_element(By.CSS_SELECTOR, CorrectAnswerSelectot.phone).text
        cnic = self.driver.find_element(By.CSS_SELECTOR, CorrectAnswerSelectot.cnic).text
        use_fire_bug = self.driver.find_element(By.CSS_SELECTOR, CorrectAnswerSelectot.firebug_in_selenium).text
        locator_type = self.driver.find_element(By.CSS_SELECTOR, CorrectAnswerSelectot.type_of_locator).text
        list_of_ans = self.driver.find_elements(By.CSS_SELECTOR, CorrectAnswerSelectot.correct_ans_list)
        prime_nums = self.driver.find_elements(By.CSS_SELECTOR, CorrectAnswerSelectot.prime_num_list)
        capital_of_pak = self.driver.find_element(By.CSS_SELECTOR, CorrectAnswerSelectot.cap_of_pak).text
        capital_of_pun = self.driver.find_element(By.CSS_SELECTOR, CorrectAnswerSelectot.cap_of_pun).text

        num_list = []
        for num in prime_nums:
            num_list.append(num.text)
        correct_ans_list = []
        for correct_ans in list_of_ans:
            correct_ans_list.append(correct_ans.text)

        final_ans_list = [email, name, phone, cnic, use_fire_bug, locator_type, num_list, correct_ans_list, capital_of_pak, capital_of_pun]
        return final_ans_list



