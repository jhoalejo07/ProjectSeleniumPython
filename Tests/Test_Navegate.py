import pytest
import time
from ProjectSeleniumPython.Pages.Functions import Functions
from ProjectSeleniumPython.Pages.Menu import Menu
from ProjectSeleniumPython.Pages.SelectProduct import SelectProduct
from ProjectSeleniumPython.Pages.Product import Product
from ProjectSeleniumPython.Pages.CartPage import Cart
from ProjectSeleniumPython.Pages.PlaceOrder import PlaceOrder
from ProjectSeleniumPython.Pages.CheckoutShipping import Checkout_Shipping

t: float = .2

@pytest.fixture(scope='module')
def setup_login_magento():
    global f, menu, selProduct, product, cart, newusr, checkout, placeOrder

    p_driverPath = r"C:\SeleniumDrivers\chromedriver.exe"

    f = Functions(p_driverPath)
    f.openBrowser("https://magento.softwaretestingboard.com/", t)

    menu = Menu(f, t)
    selProduct = SelectProduct(f, t)
    product = Product(f, t)
    cart = Cart(f, t)
    checkout = Checkout_Shipping(f, t)
    placeOrder = PlaceOrder(f, t)

    print("Login into admin-demo.magento.com ")
    yield
    print("log off from admin-demo.magento.com")


@pytest.mark.usefixtures("setup_login_magento")
def test_navigate():
    print("Opening magento")
    menu.navigate_to_women_jacket()
    selProduct.select_juno_jacket()
    product.select_juno_jacket_green_l()
    cart.modify_quantity(2)
    cart.Proceed_to_checkout()
    checkout.EnterFirstName("Pedro")
    checkout.EnterLastName("Pascal")
    checkout.EnterAddress("123 Main st")
    checkout.EnterCity("Saint John")
    checkout.EnterPostalCode("A1B 2C3")
    checkout.SelectCountry("Value", "CA")
    checkout.SelectStateProvince("Value", "70")
    checkout.EnterTelephone("9209621005")
    checkout.EnterEmail("grogu@starwars.com")
    checkout.CheckShippingFixed()
    checkout.PressNext()
    placeOrder.PressPlaceOrder()
    time.sleep(2)
    f.teardown_function()
