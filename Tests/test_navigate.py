import pytest
import time
from ProjectSeleniumPython.utils.Functions import Functions
from ProjectSeleniumPython.Pages.Menu import Menu
from ProjectSeleniumPython.Pages.SelectProduct import SelectProduct
from ProjectSeleniumPython.Pages.Product import Product
from ProjectSeleniumPython.Pages.CartPage import Cart
from ProjectSeleniumPython.Pages.PlaceOrder import PlaceOrder
from ProjectSeleniumPython.Pages.CheckoutShipping import Checkout_Shipping


@pytest.fixture(scope='module')
def setup_login_magento():
    """
    Fixture to set up the Selenium environment and initialize all page objects
    before running the test case. It opens the browser and navigates to the
    Magento demo site. Once the test module is completed, it closes the browser.

    Yields:
        dict: A dictionary containing initialized page object instances and delay time.
    """
    p_driverPath = r"C:\SeleniumDrivers\chromedriver.exe"
    t: float = .2  # Default wait time for interactions

    # Initialize the main Functions class (responsible for browser control)
    f = Functions(p_driverPath)
    f.openBrowser("https://magento.softwaretestingboard.com/", t)

    # Initialize all the page object classes with shared Functions instance
    menu = Menu(f, t)
    selProduct = SelectProduct(f, t)
    product = Product(f, t)
    cart = Cart(f, t)
    checkout = Checkout_Shipping(f, t)
    placeOrder = PlaceOrder(f, t)

    print("Login into admin-demo.magento.com ")
    yield {
        "functions": f,
        "menu": menu,
        "selProduct": selProduct,
        "product": product,
        "cart": cart,
        "checkout": checkout,
        "placeOrder": placeOrder,
        "t": t
    }
    print("Log off from admin-demo.magento.com")
    f.teardown_function()


def test_navigate(setup_login_magento):
    """
    Test to simulate a complete user purchase journey on the Magento demo site.

    Steps:
        1. Navigate to Women's Jackets category.
        2. Select the Juno Jacket product.
        3. Choose green color and size L.
        4. Add 2 units of the product to the cart.
        5. Proceed to checkout.
        6. Fill in the shipping and contact information.
        7. Select a fixed shipping method.
        8. Continue to payment and place the order.
    """
    print("Opening Magento site and starting test flow...")
    ctx = setup_login_magento
    menu = ctx["menu"]
    selProduct = ctx["selProduct"]
    product = ctx["product"]
    cart = ctx["cart"]
    checkout = ctx["checkout"]
    placeOrder = ctx["placeOrder"]
    f = ctx["functions"]
    t = ctx["t"]

    # Navigate to the desired product category
    menu.navigate_to_women_jacket()

    # Select product
    selProduct.select_juno_jacket()
    product.select_juno_jacket_green_l()

    # Modify quantity and go to checkout
    cart.modify_quantity(2)
    cart.Proceed_to_checkout()

    # Fill in shipping details
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

    # Place the order
    placeOrder.PressPlaceOrder()

    # Verifies that the order confirmation message appears after placing the order.
    text = f.return_element("xpath", "//span[@class='base'][contains(.,'Thank you for your purchase!')]", t).text
    assert text == "Thank you for your purchase!", "Order confirmation message not found"

    # Pause to observe the result before closing browser
    time.sleep(2)
