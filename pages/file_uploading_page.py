
from pages.common.selectors import FileUploadingPageSelector
from pages.common.base_page import BasePage
from selenium.webdriver.common.by import By


class FileUpLoading(BasePage):

    def upload_pdf_file(self):
        self.visibility_of_element_located(FileUploadingPageSelector.upload_pdf_file)
        self.presence_of_element_located_click(FileUploadingPageSelector.upload_pdf_file)
        iframe2 = self.driver.find_elements(By.CSS_SELECTOR, FileUploadingPageSelector.ifram1)
        self.driver.switch_to.frame(iframe2[1])
        self.visibility_of_element_located(FileUploadingPageSelector.my_drive)
        self.element_to_be_clickable(FileUploadingPageSelector.my_drive)
        self.visibility_of_element_located_click(FileUploadingPageSelector.pdf_file)
        self.visibility_of_element_located_click(FileUploadingPageSelector.select_file_btn)
        self.driver.switch_to.default_content()

    def upload_image_file(self):
        self.visibility_of_element_located(FileUploadingPageSelector.upload_image_file)
        self.presence_of_element_located_click(FileUploadingPageSelector.upload_image_file)
        iframe2 = self.driver.find_element(By.CSS_SELECTOR, FileUploadingPageSelector.ifram1)
        self.driver.switch_to.frame(iframe2)
        self.visibility_of_element_located(FileUploadingPageSelector.my_drive)
        self.element_to_be_clickable(FileUploadingPageSelector.my_drive)
        self.visibility_of_element_located_click(FileUploadingPageSelector.image_file)
        self.visibility_of_element_located_click(FileUploadingPageSelector.select_file_btn)
        self.driver.switch_to.default_content()