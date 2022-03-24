from pages.common.selectors import CheckBoxesPageSelector
from pages.common.base_page import BasePage


class CheckBoxes(BasePage):

    def select_the_correct_answer(self, correct_ans1):
        self.element_to_be_clickable(CheckBoxesPageSelector.equal_values1.format(correct_ans1))
        self.element_to_be_clickable(CheckBoxesPageSelector.equal_values2)

    def select_numbers_that_are_not_prime(self, prime_num):
        self.element_to_be_clickable(CheckBoxesPageSelector.prime_num1.format(prime_num))
        self.element_to_be_clickable(CheckBoxesPageSelector.prime_num2)

