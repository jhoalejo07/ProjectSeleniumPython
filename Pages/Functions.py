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
        # Use a raw string or double backslashes for the path
        chrome_driver_path = p_driverPath  #r"C:\SeleniumDrivers\chromedriver.exe"  # or "C:\\SeleniumDrivers\\chromedriver.exe"

        # Set up the Service object with the correct path
        service = Service(chrome_driver_path)

        # Initialize the WebDriver with the service and options
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def teardown_function(self):
        print("End of test")
        self.driver.close()

    def openBrowser(self, p_URL, p_time):
        self.driver.get(p_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("Page open: " + str(p_URL))
        time.sleep(p_time)

    def move_to_element(self, p_type, p_selector, p_time):

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
        except TimeoutException as ex:
            print("It's not possible to move to the element, it's not available" + p_selector)
            # self.Time(p_time)
            time.sleep(p_time)

    def click_on_element(self, p_type, p_selector, p_time):
        try:
            if p_type == "xpath":
                element = WebDriverWait(self.driver, p_time).until(EC.element_to_be_clickable((By.XPATH, p_selector)))
            else:
                element = WebDriverWait(self.driver, p_time).until(EC.element_to_be_clickable((By.ID, p_selector)))

            element.click()
            print("Clicking on {} ".format(p_selector))

        except TimeoutException as ex:
            print("It's not possible to click on the element, it's not available " + p_selector)
            # self.Time(p_time)
            time.sleep(p_time)

    def move_on_element_and_click(self, p_type, p_selector, p_time):
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

        except TimeoutException as ex:
            print("It's not possible to move and click on the element, it's not available" + p_selector)
            # self.Time(p_time)
            time.sleep(p_time)

    def Select_Combo(self, p_type, p_selector, p_type_sel, p_value, p_time):
        try:
            if p_type == "xpath":
                element = WebDriverWait(self.driver, p_time).until(
                    EC.visibility_of_element_located((By.XPATH, p_selector)))
            else:
                element = WebDriverWait(self.driver, p_time).until(
                    EC.visibility_of_element_located((By.ID, p_selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            ActionChains(self.driver).move_to_element(element).perform()

            #combo = self.driver.find_element(By.XPATH, p_Xpath)

            sort = Select(element)
            if p_type_sel == "Text":
                sort.select_by_visible_text(p_value)
            elif p_type_sel == "Value":
                sort.select_by_value(p_value)
            else:
                sort.select_by_index(p_value)

            print("Sorting by {} ".format(p_type_sel))

        except TimeoutException as ex:
            print("Element not available " + p_selector)

    def input_text(self, p_type, p_selector, p_text, p_time):
        try:
            if p_type == "xpath":
                val = self.return_element("xpath", p_selector, p_time)
            else:
                val = self.return_element("id", p_selector, p_time)

            val.clear()
            val.send_keys(p_text)
            print("Typing on {} the text -> {} ".format(p_selector, p_text))

        except TimeoutException as ex:
            print("Element not available to insert text" + p_selector)
            # self.Time(p_time)
            time.sleep(p_time)
        """
        elif (p_type == "id"):
            try:
                val = self.return_element("id", p_selector, p_time)
                val.clear()
                val.send_keys(p_text)
                print("Typing on {} the text -> {} ".format(p_selector, p_text))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not available" + p_selector)
                self.Time(p_time)
        """

    #use for locating a element and return it.
    def return_element(self, p_type, p_selector, p_time):

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
            print("The element: " + p_selector + " it's not available")
            return None
