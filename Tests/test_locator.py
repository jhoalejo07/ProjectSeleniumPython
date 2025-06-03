import pytest
import time
from ProjectSeleniumPython.utils.Functions import Functions
from ProjectSeleniumPython.Pages.Menu import Menu
from ProjectSeleniumPython.Pages.SelectProduct import SelectProduct
from ProjectSeleniumPython.Pages.Product import Product
from ProjectSeleniumPython.Pages.CartPage import Cart
from ProjectSeleniumPython.Pages.PlaceOrder import PlaceOrder
from ProjectSeleniumPython.Pages.CheckoutShipping import Checkout_Shipping
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains




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
    MENU_WOMEN = "//span[contains(.,'Women')]"
    WOMEN_TOPS_JACKETS = "//a[@id='ui-id-11']/span[text()='Jackets']"

    f.move_to_element("xpath", MENU_WOMEN, t)

    element = WebDriverWait(f.driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='ui-id-9' and span[@class='ui-menu-icon ui-icon ui-icon-carat-1-e']]/span[text()='Tops']")))
    f.driver.execute_script("arguments[0].scrollIntoView();", element)
    ActionChains(f.driver).move_to_element(element).perform()
    print("Moving to {} ".format("//a[@id='ui-id-9']"))

    f.move_on_element_and_click("xpath", WOMEN_TOPS_JACKETS, t)
