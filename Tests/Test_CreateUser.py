import pytest
import random
import string
import allure
from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions
from ProjectSeleniumPython.Pages.CreateCustomer import CreateUsr
from allure_commons.types import AttachmentType
from ProjectSeleniumPython.Pages.ExcelFunctions import Funexcel

t = .02


@pytest.fixture(scope='function')
def setup_newcustomer_screen():
    global f, newCustomer, fe, path_excel

    f = Functions(r"C:\SeleniumDrivers\chromedriver.exe")
    f.openBrowser("https://magento.softwaretestingboard.com/customer/account/create/", t)

    fe = Funexcel()
    path_excel = "D://Projects//Projects//ProjectSeleniumPython//User_Data.xlsx"

    newCustomer = CreateUsr(f)

    print("Enter into /customer/account/create/ ")
    yield
    print("log off from /customer/account/create/")
    f.teardown_function()


@pytest.fixture(scope='function')
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(f.driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_user_exist():
    try:
        newCustomer.EnterFirstName(fe.readData(path_excel, "magento_new_users", 2, 2))
        newCustomer.EnterLastName(fe.readData(path_excel, "magento_new_users", 2, 3))
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 2, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 2, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 2, 6))
        newCustomer.PressButtonCreate()

        #text = f.Sel_by_Xpath("//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account.')]", t).text
        text = f.return_element("xpath",
                                "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account.')]",
                                t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="UserExist", attachment_type=AttachmentType.PNG)

    except AttributeError as ex:
        fe.writeData(path_excel, "magento_new_users", 2, 7, "Failed - That user hasn't been created")
        assert False, "That user hasn't been created"

    assert text == "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."
    fe.writeData(path_excel, "magento_new_users", 2, 7, "Pass - That user exists")


@pytest.mark.positive
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_positive_create_user():
    try:
        newCustomer.EnterFirstName(fe.readData(path_excel, "magento_new_users", 3, 2))
        newCustomer.EnterLastName(fe.readData(path_excel, "magento_new_users", 3, 3))
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 3, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 3, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 3, 6))
        newCustomer.PressButtonCreate()

        # text = f.Sel_by_Xpath("//span[@class='base'][contains(.,'My Account')]", t).text
        text = f.return_element("xpath", "//span[@class='base'][contains(.,'My Account')]", t).text

        allure.attach(f.driver.get_screenshot_as_png(), name="CreatingUser", attachment_type=AttachmentType.PNG)

    except AttributeError as ex:
        fe.writeData(path_excel, "magento_new_users", 3, 7, "Failed - It isn't possible to create a user")
        assert False, "It isn't possible to create a user"

    assert text == "My Account"
    fe.writeData(path_excel, "magento_new_users", 3, 7, "Pass - User Created")


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_First_and_last_name_long():
    try:
        firstname = random_char(302)
        newCustomer.EnterFirstName(firstname)
        lastname = random_char(302)
        newCustomer.EnterLastName(lastname)
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 4, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 4, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 4, 6))
        newCustomer.PressButtonCreate()

        # errorText = f.Sel_by_Xpath("//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'First Name is not valid!" + "\n" + "Last Name is not valid!')]", t).text
        errorText = f.return_element("xpath", "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']["
                                              "contains(.,'First Name is not valid!" + "\n" + "Last Name is not "
                                                                                              "valid!')]", t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="fnameLnameLong", attachment_type=AttachmentType.PNG)

    except AttributeError as ex:
        fe.writeData(path_excel, "magento_new_users", 4, 7, "Failed - First and lastname aren't too long")
        assert False, "First or lastname aren't too long"

    assert errorText == "First Name is not valid! Last Name is not valid!", "The First and last name are valid"
    fe.writeData(path_excel, "magento_new_users", 4, 7, "Pass - First  and last Name are not valid")


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_Fisrt_name_long():
    try:
        firstname = random_char(301)
        newCustomer.EnterFirstName(firstname)
        newCustomer.EnterLastName(fe.readData(path_excel, "magento_new_users", 5, 3))
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 5, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 5, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 5, 6))
        newCustomer.PressButtonCreate()
        errorText = f.return_element("xpath",
                                     "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'First Name is not valid!')]",
                                     t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="fnameLong", attachment_type=AttachmentType.PNG)
    except AttributeError as ex:
        fe.writeData(path_excel, "magento_new_users", 5, 7, "Failed - First isn't too long")
        assert False, "First isn't too long"

    assert errorText == "First Name is not valid!", "The First name is valid"
    fe.writeData(path_excel, "magento_new_users", 5, 7, "Pass - First Name is not valid!")


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_Last_name_long():
    try:
        lastname = random_char(301)
        newCustomer.EnterFirstName(fe.readData(path_excel, "magento_new_users", 6, 2))
        newCustomer.EnterLastName(lastname)
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 6, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 6, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 6, 6))
        newCustomer.PressButtonCreate()
        errorText = f.return_element("xpath",
                                     "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'Last Name is not valid!')]",
                                     t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="LnameLong", attachment_type=AttachmentType.PNG)

    except AttributeError as ex:
        fe.writeData(path_excel, "magento_new_users", 6, 7, "Failed - Lastname isn't too long")
        assert False, "Lastname isn't too long"

    assert errorText == "Last Name is not valid!", "The last name is valid"
    fe.writeData(path_excel, "magento_new_users", 6, 7, "Pass - Last Name is not valid!!")


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_incorrect_format_email():
    try:
        newCustomer.EnterFirstName(fe.readData(path_excel, "magento_new_users", 7, 2))
        newCustomer.EnterLastName(fe.readData(path_excel, "magento_new_users", 7, 3))
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 7, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 7, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 7, 6))
        newCustomer.PressButtonCreate()

        errorText = f.return_element("xpath", "//div[@for='email_address'][contains(@id,'address-error')][contains(.,"
                                              "'Please enter a valid email address (Ex: johndoe@domain.com).')]",
                                     t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="incorrect_format_email",
                      attachment_type=AttachmentType.PNG)
    except AttributeError as ex:
        fe.writeData(path_excel, "magento_new_users", 7, 7, "Failed - It doesn't look like an invalid email")
        assert False, "It doesn't look like an invalid email"

    assert errorText == "Please enter a valid email address (Ex: johndoe@domain.com).", "IT IS A VALID EMAIL"
    fe.writeData(path_excel, "magento_new_users", 7, 7, "Pass - email is not valid!!")


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_password_Strength():
    try:
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 8, 5))

        errorText = f.return_element("xpath", "//*[@id='password-strength-meter-label']", t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="weak_pass_Strength",
                      attachment_type=AttachmentType.PNG)
        if errorText == "No Password" or errorText == "Weak":
            assert True, "Not accurate Password"
            fe.writeData(path_excel, "magento_new_users", 8, 7, "Pass - Not accurate Password!")
        else:
            fe.writeData(path_excel, "magento_new_users", 8, 7, "Failed - Accurate Password!")
            assert False, "Accurate Password"


    except AttributeError as ex:
        assert False, "textbox is not found"


@pytest.mark.positive
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_positive_password_Strength():
    try:

        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 9, 5))

        errorText = f.return_element("xpath", "//*[@id='password-strength-meter-label']", t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="strong_pass_Strength",
                      attachment_type=AttachmentType.PNG)

        if errorText == "Strong" or errorText == "Very Strong":
            assert True, "Not accurate Password"
            fe.writeData(path_excel, "magento_new_users", 9, 7, "Pass - Accurate Password!")
        else:
            fe.writeData(path_excel, "magento_new_users", 9, 7, "Failed - Not accurate Password!")
            assert False, "Accurate Password"

    except AttributeError as ex:
        assert False, "textbox is not found"


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_password_confirm_diff():
    try:
        newCustomer.EnterFirstName(fe.readData(path_excel, "magento_new_users", 10, 2))
        newCustomer.EnterLastName(fe.readData(path_excel, "magento_new_users", 10, 3))
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 10, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 10, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 10, 6))
        newCustomer.PressButtonCreate()

        errorText = f.return_element("xpath",
                                     "//div[@for='password-confirmation'][contains(.,'Please enter the same value "
                                     "again.')]",
                                     t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="confirm_pass_diff",
                      attachment_type=AttachmentType.PNG)

    except AttributeError as ex:
        fe.writeData(path_excel, "magento_new_users", 10, 7, "Failed - Password and confirm are the same")
        assert False, "Password and confirm are the same"

    assert errorText == "Please enter the same value again.", "Password and confirm are the same"
    fe.writeData(path_excel, "magento_new_users", 10, 7, "Pass - Password and confirm are different")


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
