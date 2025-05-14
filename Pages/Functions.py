import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service


class Functions:
    def __init__(self, p_driverPath):
        """
        Initializes the Selenium WebDriver using the provided ChromeDriver path.

        Args:
            p_driverPath (str): The path to the ChromeDriver executable.
        """
        service = Service(p_driverPath)
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def teardown_function(self):
        """
        Closes the browser and ends the test session.
        """
        print("End of test")
        self.driver.close()

    def openBrowser(self, p_URL, p_time):
        """
        Opens a URL in the browser, maximizes the window, and waits.

        Args:
            p_URL (str): URL to open.
            p_time (int): Time to wait after opening (in seconds).
        """
        self.driver.get(p_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("Page open: " + str(p_URL))
        time.sleep(p_time)

    def move_to_element(self, p_type, p_selector, p_time):
        """
        Scrolls to and hovers over an element.

        Args:
            p_type (str): Type of selector ('xpath' or 'id').
            p_selector (str): Selector value.
            p_time (int): Timeout in seconds.
        """
        try:
            if p_type == "xpath":
                element = WebDriverWait(self.driver, p_time).until(
                    EC.visibility_of_element_located((By.XPATH, p_selector)))
            else:
                element = WebDriverWait(self.driver, p_time).until(
                    EC.visibility_of_element_located((By.ID, p_selector)))

            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            ActionChains(self.driver).move_to_element(element).perform()
            print("Moving to {} ".format(p_selector))
        except TimeoutException:
            print("It's not possible to move to the element, it's not available: " + p_selector)
            time.sleep(p_time)

    def click_on_element(self, p_type, p_selector, p_time):
        """
        Clicks on a web element after waiting for it to be clickable.

        Args:
            p_type (str): Type of selector ('xpath' or 'id').
            p_selector (str): Selector value.
            p_time (int): Timeout in seconds.
        """
        try:
            if p_type == "xpath":
                element = WebDriverWait(self.driver, p_time).until(EC.element_to_be_clickable((By.XPATH, p_selector)))
            else:
                element = WebDriverWait(self.driver, p_time).until(EC.element_to_be_clickable((By.ID, p_selector)))

            element.click()
            print("Clicking on {} ".format(p_selector))

        except TimeoutException:
            print("It's not possible to click on the element, it's not available: " + p_selector)
            time.sleep(p_time)

    def move_on_element_and_click(self, p_type, p_selector, p_time):
        """
        Moves to an element and clicks on it.

        Args:
            p_type (str): Type of selector ('xpath' or 'id').
            p_selector (str): Selector value.
            p_time (int): Timeout in seconds.
        """
        try:
            if p_type == "xpath":
                element = WebDriverWait(self.driver, p_time).until(
                    EC.visibility_of_element_located((By.XPATH, p_selector)))
            else:
                element = WebDriverWait(self.driver, p_time).until(
                    EC.visibility_of_element_located((By.ID, p_selector)))

            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            ActionChains(self.driver).move_to_element(element).perform()

            element = WebDriverWait(self.driver, p_time).until(EC.element_to_be_clickable((By.XPATH, p_selector)))
            element.click()
            print("Moving and Clicking on {} ".format(p_selector))

        except TimeoutException:
            print("It's not possible to move and click on the element, it's not available: " + p_selector)
            time.sleep(p_time)

    def Select_Combo(self, p_type, p_selector, p_type_sel, p_value, p_time):
        """
        Selects an option from a dropdown.

        Args:
            p_type (str): Type of selector ('xpath' or 'id').
            p_selector (str): Selector value.
            p_type_sel (str): Selection type ('Text', 'Value', or 'Index').
            p_value (str|int): Value to select (text, value, or index).
            p_time (int): Timeout in seconds.
        """
        try:
            if p_type == "xpath":
                element = WebDriverWait(self.driver, p_time).until(
                    EC.visibility_of_element_located((By.XPATH, p_selector)))
            else:
                element = WebDriverWait(self.driver, p_time).until(
                    EC.visibility_of_element_located((By.ID, p_selector)))

            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            ActionChains(self.driver).move_to_element(element).perform()

            sort = Select(element)
            if p_type_sel == "Text":
                sort.select_by_visible_text(p_value)
            elif p_type_sel == "Value":
                sort.select_by_value(p_value)
            else:
                sort.select_by_index(int(p_value))

            print("Sorting by {} ".format(p_type_sel))

        except TimeoutException:
            print("Element not available: " + p_selector)

    def input_text(self, p_type, p_selector, p_text, p_time):
        """
        Inputs text into a field.

        Args:
            p_type (str): Type of selector ('xpath' or 'id').
            p_selector (str): Selector value.
            p_text (str): Text to input.
            p_time (int): Timeout in seconds.
        """
        try:
            if p_type == "xpath":
                val = self.return_element("xpath", p_selector, p_time)
            else:
                val = self.return_element("id", p_selector, p_time)

            val.clear()
            val.send_keys(p_text)
            print("Typing on {} the text -> {} ".format(p_selector, p_text))

        except TimeoutException:
            print("Element not available to insert text: " + p_selector)
            time.sleep(p_time)

    def return_element(self, p_type, p_selector, p_time):
        """
        Returns a web element, scrolling and moving to it.

        Args:
            p_type (str): Type of selector ('xpath' or 'id').
            p_selector (str): Selector value.
            p_time (int): Timeout in seconds.

        Returns:
            WebElement: The located element, or None if not found.
        """
        try:
            if p_type == "xpath":
                element = WebDriverWait(self.driver, p_time).until(
                    EC.visibility_of_element_located((By.XPATH, p_selector)))
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                ActionChains(self.driver).move_to_element(element).perform()
                element = self.driver.find_element(By.XPATH, p_selector)
                return element
            else:
                element = WebDriverWait(self.driver, p_time).until(
                    EC.visibility_of_element_located((By.ID, p_selector)))
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                ActionChains(self.driver).move_to_element(element).perform()
                element = self.driver.find_element(By.ID, p_selector)
                return element

        except TimeoutException as ex:
            print(ex.msg)
            print("The element: " + p_selector + " is not available")
            return None
