import pytest
from ProjectSeleniumPython.Pages.Functions import Functions
from ProjectSeleniumPython.Pages.Menu import Menu
from ProjectSeleniumPython.Pages.SelectProduct import SelectProduct
from ProjectSeleniumPython.Pages.Product import Product
from ProjectSeleniumPython.Pages.CartPage import Cart
from ProjectSeleniumPython.Pages.CreateCustomer import CreateUsr
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



t=.8

@pytest.fixture(scope='module')
def setup_login_magento():
    global f, menu, selProduct, product, cart, newusr

    f = Functions(r"C:\SeleniumDrivers\chromedriver.exe")
    f.OpenBrowser("https://magento.softwaretestingboard.com/", t)

    menu = Menu(f)
    selProduct = SelectProduct(f)
    product = Product(f)
    cart = Cart(f)
    newusr = CreateUsr(f)

    print("Login into admin-demo.magento.com ")
    yield
    print("log off from admin-demo.magento.com")


@pytest.mark.usefixtures("setup_login_magento")
def test_navegate():
    print("Openning magento")
    menu.NavegateToWomenJacket()
    selProduct.SelectJunoJacket()
    product.select_options_and_add_to_cart()
    cart.modifyQuantity(2)
    cart.ProceedToCheckout()
    newusr.EnterFirstName("Pedro")
    newusr.EnterLastName("Pascal")
    f.Time(t)
    f.teardown_function()

