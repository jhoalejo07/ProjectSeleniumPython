import pytest
from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions
from ProjectSeleniumPython.Pages.SelectProduct import SelectProduct


@pytest.fixture(scope='function')
def loading_magento():
    """
    Fixture that initializes the browser, loads the Magento women's jackets page,
    and provides page interaction utilities to the test.

    Yields:
        dict: A dictionary containing:
            - 'functions': instance of the Functions class to interact with the browser
            - 'selProduct': instance of SelectProduct to handle product sorting
            - 't': default sleep time between actions
    """
    p_driverPath = r"C:\SeleniumDrivers\chromedriver.exe"
    t: float = .2  # Default wait time used for element interaction (in seconds)

    # Create an instance of the custom Functions class (used to handle browser actions)
    f = Functions(p_driverPath)

    # Open the target Magento page for women’s jackets
    f.openBrowser("https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html", t)

    # Create an instance of the page object for product selection and sorting
    selProduct = SelectProduct(f, t)

    print("Login into admin-demo.magento.com (simulated)")

    # Yield context objects to the test function
    yield {
        "functions": f,
        "selProduct": selProduct,
        "t": t
    }

    # Teardown: close the browser and clean up
    print("Log off from admin-demo.magento.com (simulated)")
    f.teardown_function()


@pytest.mark.usefixtures("loading_magento")
def test_sorting_by_price_low_to_high(loading_magento):
    """
    Test Case: Verifies that products are correctly sorted from low to high price on Magento page.

    Steps:
    1. Load the jackets page.
    2. Sort products by price (low to high).
    3. Capture all displayed product prices.
    4. Validate that the prices are in ascending order.

    Args:
        loading_magento (fixture): Provides browser and page interaction objects.
    """
    # Extract provided context from the fixture
    ctx = loading_magento
    selProduct = ctx["selProduct"]
    f = ctx["functions"]

    # Select the sorting criteria. Here, we sort by "Price" using position 2.
    # sort_by_prices(sort_type, option)
    # sort_type can be "Text", "Value", or "Position"
    # option can be "Price", or index like 2
    selProduct.sort_by_prices("Position", 2)

    # Find all price elements on the page using XPath
    price_elements = f.driver.find_elements(By.XPATH, "//span[@class='price']")

    # Parse and clean the prices, converting from strings to float values
    prices = []
    for price in price_elements:
        price_text = price.text.replace("$", "").replace(",", "").strip()  # Remove "$", ",", and extra spaces
        if price_text:  # Only consider non-empty strings
            prices.append(float(price_text))

    # Create a sorted copy of the prices list for comparison
    sorted_prices = sorted(prices)

    # Validate that the original list is sorted in ascending order
    assert prices == sorted_prices, f"Prices are not sorted correctly: {prices}"

