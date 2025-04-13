import pytest
import random
import string
from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions
from ProjectSeleniumPython.Pages.CreateCustomer import CreateUsr



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


@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_positive_create_user():
    try:
        newCustomer.EnterFirstName("Pedro")
        newCustomer.EnterLastName("Pascal")
        newCustomer.EnterEmail("mando1424@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()

        text = f.Sel_by_Xpath("//span[@class='base'][contains(.,'My Account')]", t).text

    except AttributeError as ex:
        assert False, "It isn't possible to create a user"

    assert text == "My Account"

@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_First_and_last_name_long():
    try:
        firstname = random_char(302)
        newCustomer.EnterFirstName(firstname)
        lastname = random_char(302)
        newCustomer.EnterLastName(lastname)
        newCustomer.EnterEmail("dldg721@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()

        errorText = f.Sel_by_Xpath("//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'First Name is not valid!" + "\n" + "Last Name is not valid!')]", t).text

    except AttributeError as ex:
        assert False, "First or lastname aren't too long"

    assert errorText == "First Name is not valid! Last Name is not valid!", "The First and last name are valid"

@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_Fisrt_name_long():
    try:
        firstname = random_char(302)
        newCustomer.EnterFirstName(firstname)
        newCustomer.EnterLastName("Pascal")
        newCustomer.EnterEmail("dldg167@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()
        errorText = f.Sel_by_Xpath(
                "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'First Name is not valid!')]",
                t).text

    except AttributeError as ex:
        assert False, "First isn't too long"

    assert errorText == "First Name is not valid!", "The First name is valid"


@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_Last_name_long():
    try:
        lastname = random_char(302)
        newCustomer.EnterFirstName("Pedro")
        newCustomer.EnterLastName(lastname)
        newCustomer.EnterEmail("dldg179@gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()
        errorText = f.Sel_by_Xpath(
                "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'Last Name is not valid!')]",
                t).text

    except AttributeError as ex:
        assert False, "Lastname isn't too long"

    assert errorText == "Last Name is not valid!", "The last name is valid"


@pytest.mark.usefixtures("setup_newcustomer_screen")
def test_negative_incorrect_format_email():
    try:
        newCustomer.EnterFirstName("Pedro")
        newCustomer.EnterLastName("Pascal")
        newCustomer.EnterEmail("dldg653gmail.com")
        newCustomer.EnterPassw("Grokuforever123")
        newCustomer.ConfirmPassw("Grokuforever123")
        newCustomer.PressButtonCreate()

        errorText = f.Sel_by_Xpath("//div[@for='email_address'][contains(@id,'address-error')][contains(.,'Please enter a valid email address (Ex: johndoe@domain.com).')]", t).text

    except AttributeError as ex:
        assert False, "It doesn't look like an invalid email"

    assert errorText == "Please enter a valid email address (Ex: johndoe@domain.com).", "IT IS A VALID EMAIL"



def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))