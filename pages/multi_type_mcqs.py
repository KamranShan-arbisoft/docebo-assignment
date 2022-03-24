from pages.common.selectors import MultipleTypeMcqsSelector
from pages.common.base_page import BasePage


class MultipleMcq(BasePage):

    def select_multi_mcq(self, correct_mcq2):
        self.element_to_be_clickable(MultipleTypeMcqsSelector.mcq_elm1.format(correct_mcq2))

