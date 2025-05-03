import pytest
from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions
from ProjectSeleniumPython.Pages.Menu import Menu
from ProjectSeleniumPython.Pages.SelectProduct import SelectProduct


t=.8

@pytest.fixture(scope='module')
def loading_magento():
    global f, selProduct

    f = Functions(r"C:\SeleniumDrivers\chromedriver.exe")
    f.OpenBrowser("https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html", t)


    selProduct = SelectProduct(f)

    print("Login into admin-demo.magento.com ")
    yield
    print("log off from admin-demo.magento.com")
    f.teardown_function()


@pytest.mark.usefixtures("loading_magento")
def test_sorting_by_price_low_to_high():

    selProduct.SortByPrices("Position", 2) # other options for p_type ("Text" ("Position", "Producto Name", "Price"), "Value" (0,1,2),"Position" )
    #f.Time(5)

    # Extract all product prices
    price_elements = f.driver.find_elements(By.XPATH, "//span[@class='price']")

    # Convert price strings to float (handling currency symbols)
    prices = []
    for price in price_elements:
        price_text = price.text.replace("$", "").replace(",", "").strip()  # Remove $ and spaces
        if price_text:  # Ensure it's not empty
            prices.append(float(price_text))

    # Check if the prices are sorted
    sorted_prices = sorted(prices)  # Expected sorted order

    # Assert that the extracted prices are sorted
    assert prices == sorted_prices, f"Prices are not sorted correctly: {prices}"
