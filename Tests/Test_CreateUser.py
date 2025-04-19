import pytest
import random
import string
import allure
from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions
from ProjectSeleniumPython.Pages.CreateCustomer import CreateUsr
from allure_commons.types import AttachmentType



t=.02

@pytest.fixture(scope='function')
def setup_newcustomer_screen():
    global f, newCustomer

    f = Functions(r"C:\SeleniumDrivers\chromedriver.exe")
    f.OpenBrowser("https://magento.softwaretestingboard.com/customer/account/create/", t)


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
        newCustomer.EnterFirstName("Pedro")
        newCustomer.EnterLastName("Pascal")
        newCustomer.EnterEmail("mando18042025@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()

        text = f.Sel_by_Xpath("//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account.')]", t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="UserExist", attachment_type=AttachmentType.PNG)

    except AttributeError as ex:
            assert False, "That user hasn't been created"

    assert text == "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."

@pytest.mark.positive
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_positive_create_user():
    try:
        newCustomer.EnterFirstName("Pedro")
        newCustomer.EnterLastName("Pascal")
        newCustomer.EnterEmail("mando190420252@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()

        text = f.Sel_by_Xpath("//span[@class='base'][contains(.,'My Account')]", t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="CreatingUser", attachment_type=AttachmentType.PNG)

    except AttributeError as ex:
        assert False, "It isn't possible to create a user"

    assert text == "My Account"

@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_First_and_last_name_long():
    try:
        firstname = random_char(302)
        newCustomer.EnterFirstName(firstname)
        lastname = random_char(302)
        newCustomer.EnterLastName(lastname)
        newCustomer.EnterEmail("dldg1904@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()

        errorText = f.Sel_by_Xpath("//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'First Name is not valid!" + "\n" + "Last Name is not valid!')]", t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="fnameLnameLong", attachment_type=AttachmentType.PNG)

    except AttributeError as ex:
        assert False, "First or lastname aren't too long"

    assert errorText == "First Name is not valid! Last Name is not valid!", "The First and last name are valid"

@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_Fisrt_name_long():
    try:
        firstname = random_char(302)
        newCustomer.EnterFirstName(firstname)
        newCustomer.EnterLastName("Pascal")
        newCustomer.EnterEmail("dldg1905@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()
        errorText = f.Sel_by_Xpath(
                "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'First Name is not valid!')]",
                t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="fnameLong", attachment_type=AttachmentType.PNG)
    except AttributeError as ex:
        assert False, "First isn't too long"

    assert errorText == "First Name is not valid!", "The First name is valid"

@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_Last_name_long():
    try:
        lastname = random_char(302)
        newCustomer.EnterFirstName("Pedro")
        newCustomer.EnterLastName(lastname)
        newCustomer.EnterEmail("dldg1906@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()
        errorText = f.Sel_by_Xpath(
                "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'Last Name is not valid!')]",
                t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="LnameLong", attachment_type=AttachmentType.PNG)
    except AttributeError as ex:
        assert False, "Lastname isn't too long"

    assert errorText == "Last Name is not valid!", "The last name is valid"

@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_incorrect_format_email():
    try:
        newCustomer.EnterFirstName("Pedro")
        newCustomer.EnterLastName("Pascal")
        newCustomer.EnterEmail("dldg653@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()

        errorText = f.Sel_by_Xpath("//div[@for='email_address'][contains(@id,'address-error')][contains(.,'Please enter a valid email address (Ex: johndoe@domain.com).')]", t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="incorrect_format_email", attachment_type=AttachmentType.PNG)
    except AttributeError as ex:
        assert False, "It doesn't look like an invalid email"

    assert errorText == "Please enter a valid email address (Ex: johndoe@domain.com).", "IT IS A VALID EMAIL"

@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_password_Strength():
    try:
        newCustomer.EnterPassw("Groku")

        errorText = f.Sel_by_Xpath("//*[@id='password-strength-meter-label']", t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="weak_pass_Strength",
                      attachment_type=AttachmentType.PNG)
        if errorText == "No Password" or errorText == "Weak":
            assert True, "Not accurate Password"
        else:
            assert False, "Accurate Password"

    except AttributeError as ex:
        assert False, "textbox is not found"


@pytest.mark.positive
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_positive_password_Strength():
    try:
        newCustomer.EnterPassw("Grokuforever123")

        errorText = f.Sel_by_Xpath("//*[@id='password-strength-meter-label']", t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="strong_pass_Strength",
                      attachment_type=AttachmentType.PNG)

        if errorText == "Strong" or errorText == "Very Strong":
            assert True, "Not accurate Password"
        else:
            assert False, "Accurate Password"

    except AttributeError as ex:
        assert False, "textbox is not found"

@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_password_confirm_diff():
    try:
        newCustomer.EnterFirstName("Pedro")
        newCustomer.EnterLastName("Pascal")
        newCustomer.EnterEmail("dldg653@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()

        errorText = f.Sel_by_Xpath("//div[@for='password-confirmation'][contains(.,'Please enter the same value again.')]", t).text
        allure.attach(f.driver.get_screenshot_as_png(), name="confirm_pass_diff",
                      attachment_type=AttachmentType.PNG)

    except AttributeError as ex:
        assert False, "Password and confirm are the same"

    assert errorText == "Please enter the same value again.", "Password and confirm are the same"

def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))