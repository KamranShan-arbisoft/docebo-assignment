
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


class TestGoogleForm(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.driver.get(self.login_page.base_url)
        self.basic_info = BasicInformation(self.driver)
        self.multiple_type_ques = MultipleMcq(self.driver)
        self.checkbox = CheckBoxes(self.driver)
        self.next_btn = Utils(self.driver)
        self.response = Utils(self.driver)
        self.drop_down = DropDown(self.driver)
        self.file_upload = FileUpLoading(self.driver)
        self.current_date_time = DateAndTime(self.driver)
        self.final_correct_ans = StoreCorrectAnswer(self.driver)
        self.base_page = BasePage(self.driver)

    def test_google_form(self):
        # login form and submit basic infomation
        self.login_page.login()
        # Fill Basic Personal Info
        self.basic_info.fill_basic_info()
        self.next_btn.next_page(NextButton.next_btn_pages)

        # select multiple type ans
        status = self.response.response_of_request()
        assert status.status_code == 401
        self.assertIn("Multiple type Questions", self.driver.page_source)
        mcq_questions = Utils.form_questions_text(self)
        for question in mcq_questions:
            if question.text == "Use of Firebug in Selenium? *":
                mcqs = self.base_page.form_data[6]
                correct_mcq1 = mcqs[1].split(',')[0]
                self.multiple_type_ques.select_multi_mcq(correct_mcq1)
            elif question.text == "Select the name which is NOT a type of the locater? *":
                mcqs = self.base_page.form_data[5]
                correct_mcq2 = mcqs[1].split(',')[0]
                self.multiple_type_ques.select_multi_mcq(correct_mcq2)
        self.next_btn.next_page(NextButton.next_btn_pages)

        # Select multiple chack boxes
        status = self.response.response_of_request()
        assert status.status_code == 401
        content_length = status.headers.get('content-length')
        assert "Checkboxes" in self.driver.page_source
        if content_length == None:
            checkboxes_mcqs_text = Utils.form_questions_text(self)
            for checkbox in checkboxes_mcqs_text:
                if checkbox.text == "Select the two numbers that are not prime. *":
                    prime_numbers = self.base_page.form_data[7]
                    prime_num = prime_numbers[1].split(',')[0]
                    self.checkbox.select_numbers_that_are_not_prime(prime_num)
                elif checkbox.text == 'Select the correct answers *':
                    answers = self.base_page.form_data[8]
                    correct_ans1 = answers[1].split(',')[0]
                    self.checkbox.select_the_correct_answer(correct_ans1)
        self.next_btn.next_page(NextButton.next_btn_pages)

        # Select capital of punjab and capital of pakistan
        status = self.response.response_of_request()
        assert status.status_code == 401
        if status.status_code == 401:
            assert "Dropdown" in self.driver.page_source
            expected_assert = self.driver.title
            self.assertEqual("Automation Assessment", expected_assert, "Comparison are not match")
            capitals_mcqs_text = Utils.form_questions_text(self)
            for capital in capitals_mcqs_text:
                if capital.text == 'Capital of Pakistan *':
                    capital_of_pak = self.base_page.form_data[9]
                    capital_city_pak = capital_of_pak[1].split(',')[0]
                    self.drop_down.drop_capital_of_pakistan(capital_city_pak)
                elif capital.text == 'Capital of Punjab *':
                    capital_of_pun = self.base_page.form_data[10]
                    capital_city_pun = capital_of_pun[1].split(',')[0]
                    self.drop_down.drop_capital_of_punjab(capital_city_pun)
        self.next_btn.next_page(NextButton.next_btn_pages)

        # upload PDF and image file
        status = self.response.response_of_request()
        assert status.status_code == 401
        if status.status_code == 401:
            assert "File Uploading" in self.driver.page_source
            self.file_upload.upload_image_file()
            self.file_upload.upload_pdf_file()
            self.next_btn.next_page(NextButton.next_btn_pages)

        # Enter Current date and time
        status = self.response.response_of_request()
        assert status.status_code == 401
        assert "Enter Current time" in self.driver.page_source
        self.current_date_time.current_time()
        self.current_date_time.current_date()
        self.current_date_time.submitForm()

        # Click on the view resource button to see the submit results
        status = self.response.response_of_request()
        assert status.status_code == 401
        assert "Automation Assessment" in self.driver.page_source
        self.next_btn.view_submit_score(NextButton.view_source)

        # Get the all correct answers and store into the correct answer column of csv
        status = self.response.response_of_request()
        assert status.status_code == 401
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert "Automation Assessment" in self.driver.page_source
        final_ans = self.final_correct_ans.get_correct_answers()
        self.base_page.write_csv(final_ans)


