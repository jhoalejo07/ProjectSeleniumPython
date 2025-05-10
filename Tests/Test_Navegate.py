import pytest
import time
from ProjectSeleniumPython.Pages.Functions import Functions
from ProjectSeleniumPython.Pages.Menu import Menu
from ProjectSeleniumPython.Pages.SelectProduct import SelectProduct
from ProjectSeleniumPython.Pages.Product import Product
from ProjectSeleniumPython.Pages.CartPage import Cart
from ProjectSeleniumPython.Pages.CreateCustomer import CreateUsr


t = .2

@pytest.fixture(scope='module')
def setup_login_magento():
    global f, menu, selProduct, product, cart, newusr

    p_driverPath = r"C:\SeleniumDrivers\chromedriver.exe"

    f = Functions(p_driverPath)
    f.openBrowser("https://magento.softwaretestingboard.com/", t)

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
    product.select_juno_jacket_green_l()
    cart.modifyQuantity(2)
    cart.ProceedToCheckout()
    newusr.EnterFirstName("Pedro")
    newusr.EnterLastName("Pascal")

    # f.Time(t)
    time.sleep(t)
    f.teardown_function()

