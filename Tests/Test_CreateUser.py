import pytest
import random
import string
from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions
from ProjectSeleniumPython.Pages.CreateCustomer import CreateUsr



t=.02

@pytest.fixture(scope='module')
def setup_newcustomer_screen():
    global f, newCustomer

    f = Functions(r"C:\SeleniumDrivers\chromedriver.exe")
    f.OpenBrowser("https://magento.softwaretestingboard.com/customer/account/create/", t)


    newCustomer = CreateUsr(f)

    print("Enter into /customer/account/create/ ")
    yield
    print("log off from /customer/account/create/")


@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_positive_create_user():
    newCustomer.EnterFirstName("Pedro")
    newCustomer.EnterLastName("Pascal")
    newCustomer.EnterEmail("mando@gmail.com")
    newCustomer.EnterPassw("Grokuforever123")
    newCustomer.ConfirmPassw("Grokuforever123")
    newCustomer.PressButtonCreate()
    newCustomer.Time(2)
@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_Fisrt_and_last_name_long():
    firstname = random_char(302)
    newCustomer.EnterFirstName(firstname)
    lastname = random_char(302)
    newCustomer.EnterLastName(lastname)
    newCustomer.EnterEmail("dldg4@gmail.com")
    newCustomer.EnterPassw("Grokuforever123")
    newCustomer.ConfirmPassw("Grokuforever123")
    newCustomer.PressButtonCreate()

    # I HAVE THE WAY TO PUT THE MESSAGE WITH ENTER First Name is not valid!
    # Last Name is not valid!
    errorText = f.Sel_by_Xpath(
        "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'First Name is not valid!" + "\n" + "Last Name is not valid!')]",
        t).text

    assert errorText == "First Name is not valid! Last Name is not valid!", "The First and last name are valid"


@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_Fisrt_name_long():
    firstname = random_char(302)
    newCustomer.EnterFirstName(firstname)
    newCustomer.EnterLastName("Pascal")
    newCustomer.EnterEmail("dldg4@gmail.com")
    newCustomer.EnterPassw("Grokuforever123")
    newCustomer.ConfirmPassw("Grokuforever123")
    newCustomer.PressButtonCreate()
    errorText = f.Sel_by_Xpath(
            "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'First Name is not valid!')]",
            t).text

    assert errorText == "First Name is not valid!", "The First name is valid"
    newCustomer.Time(t)

@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_Last_name_long():
    lastname = random_char(302)
    newCustomer.EnterFirstName("Pedro")
    newCustomer.EnterLastName(lastname)
    newCustomer.EnterEmail("dldg4@gmail.com")
    newCustomer.EnterPassw("Grokuforever123")
    newCustomer.ConfirmPassw("Grokuforever123")
    newCustomer.PressButtonCreate()
    errorText = f.Sel_by_Xpath(
            "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'Last Name is not valid!')]",
            t).text

    assert errorText == "Last Name is not valid!", "The last name is valid"
    newCustomer.Time(t)

@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_incorrect_format_email():
    try:
        newCustomer.EnterFirstName("Pedro")
        newCustomer.EnterLastName("Pascal")
        newCustomer.EnterEmail("dldg14gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()

        error_element = f.Sel_by_Xpath(
            "//div[@for='email_address'][contains(@id,'address-error')][contains(.,'Please enter a valid email address (Ex: johndoe@domain.com).')]",
            t)

        errorText = f.Sel_by_Xpath("//div[@for='email_address'][contains(@id,'address-error')][contains(.,'Please enter a valid email address (Ex: johndoe@domain.com).')]", t).text
        assert errorText == "Please enter a valid email address (Ex: johndoe@domain.com).", "IT IS A VALID EMAIL"
        #newCustomer.Time(t)

    except AttributeError as ex:
        #print("IT IS A VALID EMAIL")
        pytest.fail(f"It's a valid email")


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))