
from pages.common.selectors import NextButton
from tests.utils.utils import Utils
from tests.common.base_test import BaseTest
from pages.login_google_form import LoginPage
from pages.fill_basic_info import BasicInformation
from pages.multi_type_mcqs import MultipleMcq
from pages.checkboxes import CheckBoxes
from pages.dropdown import DropDown
from pages.file_uploading_page import FileUpLoading
from pages.current_date_time import DateAndTime
from pages.correct_answers import StoreCorrectAnswer
from pages.common.base_page import BasePage
from selenium.webdriver.common.by import By


class TestNegativeGoogleForm(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.driver.get(self.login_page.base_url)
        self.basic_info = BasicInformation(self.driver)
        self.multiple_type_ques = MultipleMcq(self.driver)
        self.checkbox = CheckBoxes(self.driver)
        self.next_btn = Utils(self.driver)
        self.response = Utils(self.driver)
        self.validation = Utils(self.driver)
        self.drop_down = DropDown(self.driver)
        self.file_upload = FileUpLoading(self.driver)
        self.current_date_time = DateAndTime(self.driver)
        self.final_correct_ans = StoreCorrectAnswer(self.driver)
        self.base_page = BasePage(self.driver)

    def test_negative_google_form(self):
        # login form and submit basic infomation
        self.login_page.login()
        # Page 1 Validation check on user personal Info
        status = self.response.response_of_request()
        assert status.status_code == 401
        # Getting all pages question title
        all_page_titles = self.next_btn.form_questions_text()
        for page_title in all_page_titles:
            if page_title.text == "Phone Number *":
                self.validation.invalid_validation_check("Phone Number", "string")
            elif page_title.text == "Email *":
                self.validation.invalid_validation_check("Email", "string")
            elif page_title.text == "CNIC *":
                self.validation.invalid_validation_check("CNIC", "string")
            elif page_title.text == "Name *":
                self.driver.find_element(By.CSS_SELECTOR, '[data-params*="Name"] input').click()
        self.next_btn.next_page(NextButton.next_btn_pages)

        # Getting validation of each field of page 1
        page_validation = self.next_btn.form_validation_text()
        for i in range(len(page_validation)):
            if all_page_titles[i].text == "Phone Number *":
                if page_validation[i].text == "Must match pattern":
                    self.validation.valid_validation_check("Phone Number", "03224542504")
            elif all_page_titles[i].text == "Email *":
                if page_validation[i].text == "Must be a valid email":
                    self.validation.valid_validation_check("Email", "hk@arbisoft.com")
            elif all_page_titles[i].text == "CNIC *":
                if page_validation[i].text == "Must match pattern":
                    self.validation.valid_validation_check("CNIC", "3525252525254")
            elif all_page_titles[i].text == "Name *":
                if page_validation[i].text == "This is a required question":
                    self.validation.valid_validation_check("Name", "kmaran")

            self.next_btn.next_page(NextButton.next_btn_pages)

        # Page 2 Validation check on Multiple type Questions
        status = self.response.response_of_request()
        assert status.status_code == 401
        self.next_btn.next_page(NextButton.next_btn_pages)
        # Getting all pages question title
        all_page_titles = self.next_btn.form_questions_text()
        # Getting validation of each field of page 1
        page_validation = self.next_btn.form_validation_text()
        error_msg = page_validation[0].text
        for i in range(len(all_page_titles)):
            if all_page_titles[i].text == "Select the name which is NOT a type of the locater? *":
                if error_msg == "This is a required question":
                    self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Link Text"]').click()
                    self.next_btn.next_page(NextButton.next_btn_pages)
            elif all_page_titles[i].text == "Use of Firebug in Selenium? *":
                if error_msg == "This is a required question":
                    self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Programming"]').click()
                    self.next_btn.next_page(NextButton.next_btn_pages)

        # Page 3 Validation check on checkboxes
        status = self.response.response_of_request()
        assert status.status_code == 401
        self.next_btn.next_page(NextButton.next_btn_pages)
        # Getting all pages question title
        all_page_titles = self.next_btn.form_questions_text()
        # Getting validation of each field of page 1
        page_validation = self.next_btn.form_validation_text()
        error_msg = page_validation[0].text
        for i in range(len(all_page_titles)):
            if all_page_titles[i].text == "Select the correct answers *":
                if error_msg == "This is a required question":
                    self.driver.find_element(By.CSS_SELECTOR, 'div[data-answer-value="5*6 = 10*6"]').click()
                    self.next_btn.next_page(NextButton.next_btn_pages)
            elif all_page_titles[i].text == "Select the two numbers that are not prime. *":
                if error_msg == "This is a required question":
                    self.driver.find_element(By.CSS_SELECTOR, 'div[data-answer-value="51"]').click()
                    self.next_btn.next_page(NextButton.next_btn_pages)

        # Page 4 Validation check on Dropdown
        status = self.response.response_of_request()
        assert status.status_code == 401
        self.next_btn.next_page(NextButton.next_btn_pages)
        # Getting all pages question title
        all_page_titles = self.next_btn.form_questions_text()
        # Getting validation of each field of page 1
        page_validation = self.next_btn.form_validation_text()
        error_msg = page_validation[0].text
        for i in range(len(all_page_titles)):
            if all_page_titles[i].text == 'Capital of Pakistan *':
                if error_msg == "This is a required question":
                    capital_of_pak = self.base_page.form_data[9]
                    capital_city_pak = capital_of_pak[1].split(',')[0]
                    self.drop_down.drop_capital_of_pakistan(capital_city_pak)
                    self.next_btn.next_page(NextButton.next_btn_pages)
            elif all_page_titles[i].text == 'Capital of Punjab *':
                if error_msg == "This is a required question":
                    capital_of_pun = self.base_page.form_data[10]
                    capital_city_pun = capital_of_pun[1].split(',')[0]
                    self.drop_down.drop_capital_of_punjab(capital_city_pun)
                    self.next_btn.next_page(NextButton.next_btn_pages)

        # Page 5 Validation check on files uploads
        status = self.response.response_of_request()
        assert status.status_code == 401
        self.next_btn.next_page(NextButton.next_btn_pages)
        # Getting all pages question title
        all_page_titles = self.next_btn.form_questions_text()
        # Getting validation of each field of page 1
        page_validation = self.next_btn.form_validation_text()
        error_msg = page_validation[0].text
        for i in range(len(all_page_titles)):
            if all_page_titles[i].text == "Upload Image File *":
                if error_msg == "This is a required question":
                    self.file_upload.upload_image_file()
                    self.next_btn.next_page(NextButton.next_btn_pages)
            elif all_page_titles[i].text == "Upload pdf file *":
                if error_msg == "This is a required question":
                    self.file_upload.upload_pdf_file()
                    self.next_btn.next_page(NextButton.next_btn_pages)

        # Page 6 Validation check on current time and date
        status = self.response.response_of_request()
        assert status.status_code == 401
        self.next_btn.next_page(NextButton.next_btn_pages)
        # Getting all pages question title
        all_page_titles = self.next_btn.form_questions_text()
        # Getting validation of each field of page 1
        page_validation = self.next_btn.form_validation_text()
        error_msg = page_validation[0].text
        for i in range(len(all_page_titles)):
            if all_page_titles[i].text == "Enter Current date *":
                if error_msg == "This is a required question":
                    self.current_date_time.current_date()
                    self.current_date_time.submitForm()
            elif all_page_titles[i].text == "Enter Current time *":
                if error_msg == "This is a required question":
                    self.current_date_time.current_time()
                    self.current_date_time.submitForm()