class LoginPageSelector:
    email_id = 'input[type="email"]'
    password = 'input[type="password"]'


class NextButton:
    next_btn_login_page = 'div[jsname="k77Iif"] button[jsname="LgbsSe"]'
    next_btn_pages = '[jsname|=OCpkoe]'
    view_source = 'a[aria-label="View score"]'
    form_questions = 'div[role="list"] div[role="heading"][aria-Level="3"]'
    field_validation_text = 'div[role="list"] div[role="alert"]>span'


class ValidationCheck:
    error_msg_ele = '[data-params*="Phone Number"] input'
    error_msg_text = '[data-params*="{}"] input'


class BasicInfoSelector:
    phone_number = '[data-params*="Phone Number"] input'
    cnic_num = '[data-params*="CNIC"] input'
    name = '[data-params*="Name"] input'
    email = '[data-params*="Email"] input'


class MultipleTypeMcqsSelector:
    mcq_elm1 = 'div[aria-label="{}"]'
    mcq_elm2 = 'div[aria-label="{}"]'


class CheckBoxesPageSelector:
    equal_values1 = 'div[aria-label="{}"]'
    equal_values2 = 'div[data-answer-value="5*6 = 10*6"]'
    prime_num1 = 'div[data-answer-value="51"]'
    prime_num2 = 'div[aria-label="31"]'


class DropDownPagesSelector:
    drop_of_pakistan = 'div[data-params*="Capital of Pakistan"] div[role="listbox"]'
    drop_of_punjab = 'div[data-params*="Capital of Punjab"] div[role="listbox"]'
    capital_of_pakistan = 'div[role="presentation"] div[data-value="{}"][role="option"]'
    capital_of_punjab = 'div[role="presentation"] div[data-value="{}"][role="option"]'


class FileUploadingPageSelector:
    upload_image_file = 'div[data-params*="Upload Image File"] div[role="button"]'
    upload_pdf_file = 'div[data-params*="Upload pdf file"] div[role="button"]'
    ifram1 = 'iframe[src*="https://docs.google.com"]'
    my_drive = 'div[id=":6"]'
    pdf_file = 'div[id*="DoclistBlob"]:nth-child(1)'
    image_file = 'div[aria-label="IMG_1300.PNG"]'
    select_file_btn = 'div[role="button"][id="picker:ap:2"]'


class DateAndTimeSelector:
    date_elm = 'input[type="date"]'
    hours = 'input[aria-label="Hour"]'
    minut = 'input[aria-label="Minute"]'
    submit_btn = 'div[role="button"][jsname="M2UYVd"]'


class CorrectAnswerSelectot:
    total_points = 'span[aria-describedby="i1"]'
    email = 'div[data-item-id="261164311"]>div:nth-child(2)>div'
    name = 'div[data-item-id="2021179574"]>div:nth-child(2)>div'
    phone = 'div[data-item-id="885951454"]>div:nth-child(2)>div'
    cnic = 'div[data-item-id="2098358926"]>div:nth-child(2)>div'
    firebug_in_selenium = 'div[data-item-id="866567686"]>div:nth-child(3) span[dir="auto"]'
    type_of_locator = 'div[data-item-id="1325168097"]>div:nth-child(3) span[dir="auto"]'
    correct_ans_list = 'div[data-item-id="1944594563"]>div:nth-child(5) span[dir="auto"]'
    prime_num_list = 'div[data-item-id="639199141"]>div:nth-child(5) span[dir="auto"]'
    cap_of_pun = 'div[data-item-id="543587841"]>div:nth-child(3)>div:nth-child(2)>div>div>div'
    cap_of_pak = 'div[data-item-id="434999194"]>div:nth-child(3)>div:nth-child(2)>div>div>div'