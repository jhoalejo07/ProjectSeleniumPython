import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
class Functions():
    """
    A utility class to simplify Selenium WebDriver interactions for UI test automation with Pytest.

    This class provides a reusable library of common Selenium WebDriver operations
    for use in Pytest-based UI test automation. It encapsulates browser initialization,
    element selection, interactions (clicks, typing, drag & drop, etc.), and waiting logic.

    Usage:
        1. Create an instance by providing the path to your ChromeDriver executable.
        2. Use methods like `OpenBrowser`, `click_on_element_by_xpath`, `f_text_Mix`, etc.
        3. Combine these methods in your Pytest test cases for efficient and structured automation.

    Note:
        This code is intended for private use only. Do not publish or distribute it without permission.

    Attributes:
        driver (webdriver.Chrome): The Selenium Chrome WebDriver instance.


    Methods:
        OpenBrowser(p_URL, p_time): Opens a URL in a Chrome browser and waits.
        teardown_function(): Closes the browser.
        Time(p_time): Pauses execution for a given time in seconds.
        click_on_element_by_xpath(p_xpath, p_time): Clicks an element by XPath.
        move_to_element_by_xpath(p_xpath, p_time): Moves to an element by XPath.
        move_on_element_and_click_by_xpath(p_xpath, p_time): Moves to and clicks an element.
        Sel_by_Xpath(p_selector, p_time): Finds an element by XPath.
        Sel_by_ID(p_selector): Finds an element by ID.
        f_Select_By_Xpath(p_Xpath, p_type, p_value, p_Time): Selects from dropdown by XPath.
        f_Select_By_ID(p_id, p_type, p_value, p_Time): Selects from dropdown by ID.
        f_text_Mix(p_type, p_selector, p_text, p_time): Types into a field (XPath or ID).
        f_Click_Mix(p_type, p_selector, p_time): Clicks an element (XPath or ID).
        f_DoubleClick_Mix(p_type, p_selector, p_time): Double-clicks an element.
        f_RightClick_Mix(p_type, p_selector, p_time): Right-clicks an element.
        f_DragandDropClick_Mix(p_type, p_sel_orig, p_sel_dest, p_time): Drags and drops an element to a target.
        f_DragandDrop_X_Y_Mix(p_type, p_sel, p_x, p_y, p_time): Drags an element by X and Y offsets.
    """
    def __init__(self, p_driverPath):
         # Use a raw string or double backslashes for the path
        chrome_driver_path = p_driverPath #r"C:\SeleniumDrivers\chromedriver.exe"  # or "C:\\SeleniumDrivers\\chromedriver.exe"

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

    def Time(self,p_time):
        t = time.sleep(p_time)
        return t

    def OpenBrowser(self, p_URL, p_time):
        self.driver.get(p_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("Page open: " + str(p_URL))
        self.Time(p_time)


    def move_to_element_by_xpath(self, p_xpath, p_time):
        try:
            element = WebDriverWait(self.driver, p_time).until(EC.visibility_of_element_located((By.XPATH, p_xpath)))
            ActionChains(self.driver).move_to_element(element).perform()
            print("Moving to {} ".format(p_xpath))
            self.Time(p_time)

        except TimeoutException as ex:
            print(ex.msg)
            print("It's not possible to move to the element, it's not available" + p_xpath)
            self.Time(p_time)


    def click_on_element_by_xpath(self, p_xpath, p_time):
        try:
            element = WebDriverWait(self.driver, p_time).until(EC.element_to_be_clickable((By.XPATH, p_xpath)))
            element.click()
            print("Clicking on {} ".format(p_xpath))
            self.Time(p_time)
        except TimeoutException as ex:
            print(ex.msg)
            print("It's not possible to click on the element, it's not available" + p_xpath)
            self.Time(p_time)

    def move_on_element_and_click_by_xpath(self, p_xpath, p_time):
        try:
            element = WebDriverWait(self.driver, p_time).until(EC.visibility_of_element_located((By.XPATH, p_xpath)))
            ActionChains(self.driver).move_to_element(element).perform()
            element = WebDriverWait(self.driver, p_time).until(EC.element_to_be_clickable((By.XPATH, p_xpath)))
            element.click()
            print("Moving and Clicking on {} ".format(p_xpath))
            self.Time(p_time)
        except TimeoutException as ex:
            print(ex.msg)
            print("It's not possible to move and click on the element, it's not available" + p_xpath)
            self.Time(p_time)

    def Sel_by_Xpath (self, p_selector, p_time):
        try:
            element = WebDriverWait(self.driver, p_time).until(EC.visibility_of_element_located((By.XPATH, p_selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element = self.driver.find_element(By.XPATH, p_selector)
            return element
        except TimeoutException as ex:
            print(ex.msg)
            print("It's not possible to move and click on the element, it's not available" + p_selector)
            return None


    def f_Select_By_Xpath(self, p_Xpath, p_type,p_value, p_Time):
        try:
            # In explicit wait Selenium waits until the expected condition find the element (EC has several types)
            submit_look = WebDriverWait(self.driver, p_Time).until(
                EC.visibility_of_element_located((By.XPATH, p_Xpath)))
            # located the button by its Xpath
            combo = self.driver.find_element(By.XPATH, p_Xpath)
            sort = Select(combo)
            if (p_type == "Text"):
                sort.select_by_visible_text(p_value)
            elif (p_type == "Value"):
                sort.select_by_value(p_value)
            else:
                sort.select_by_index(p_value)

            print("Sorting by {} ".format(p_type))
            self.Time(p_Time)

        except TimeoutException as ex:
            print(ex.msg)
            print("Element not available")

    def f_Select_By_ID(self, p_id, p_type,p_value, p_Time):
        try:
            # In explicit wait Selenium waits until the expected condition find the element (EC has several types)
            submit_look = WebDriverWait(self.driver, p_Time).until(
                EC.visibility_of_element_located((By.XPATH, p_id)))
            # located the button by its Xpath
            combo = self.driver.find_element(By.ID, p_id)
            sort = Select(combo)
            if (p_type == "Text"):
                sort.select_by_visible_text(p_value)
            elif (p_type == "Value"):
                sort.select_by_value(p_value)
            else:
                sort.select_by_index(p_value)

        except TimeoutException as ex:
            print(ex.msg)
            print("Element not available")

    def Sel_by_ID(self, p_selector):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, p_selector)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element = self.driver.find_element(By.ID, p_selector)
        return element

    def f_text_Mix(self, p_type, p_selector, p_text, p_time):
        if(p_type=="xpath"):
            try:
                val = self.Sel_by_Xpath(p_selector, p_time)
                val.clear()
                val.send_keys(p_text)
                print("Typing on {} the text -> {} ".format(p_selector,p_text))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not available" + p_selector)
                self.Time(p_time)

        elif(p_type == "id"):
            try:
                '''
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, p_selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, p_selector)
                '''
                val = self.Sel_by_ID(p_selector)
                val.clear()
                val.send_keys(p_text)
                print("Typing on {} the text -> {} ".format(p_selector,p_text))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not available" + p_selector)
                self.Time(p_time)

    def f_Click_Mix(self, p_type, p_selector,p_time):
        if (p_type == "xpath"):
            try:
                val = self.Sel_by_Xpath(p_selector, p_time)
                val.click()
                print("Click on {} ".format(p_selector))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not available" + p_selector)
                self.Time(p_time)
        elif (p_type == "id"):
            try:
                val = self.Sel_by_ID(p_selector)
                val.click()
                print("Click on {} -> {} ".format(p_selector, p_selector))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not available" + p_selector)
                self.Time(p_time)

    def f_DoubleClick_Mix(self, p_type, p_selector,p_time):
        if (p_type == "xpath"):
            try:
                btn = self.Sel_by_Xpath(p_selector, p_time)
                act = ActionChains(self.driver)
                act.double_click(btn).perform()
                print("DoubleClick on {} ".format(p_selector))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not available" + p_selector)
                self.Time(p_time)
        elif (p_type == "id"):
            try:
                btn = self.Sel_by_ID(p_selector)
                act = ActionChains(self.driver)
                act.double_click(btn).perform()
                print("DoubleClick on {} ".format(p_selector))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not available" + p_selector)
                self.Time(p_time)

    def f_RightClick_Mix(self, p_type, p_selector,p_time):
        if (p_type == "xpath"):
            try:
                btn = self.Sel_by_Xpath(p_selector, p_time)
                act = ActionChains(self.driver)
                act.context_click(btn).perform()
                print("RightClick on {} ".format(p_selector))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not available" + p_selector)
                self.Time(p_time)
        elif (p_type == "id"):
            try:
                btn = self.Sel_by_ID(p_selector)
                act = ActionChains(self.driver)
                act.context_click(btn).perform()
                print("RightClick on {} ".format(p_selector))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not available" + p_selector)
                self.Time(p_time)

    def f_DragandDropClick_Mix(self, p_type, p_sel_orig, p_sel_dest,p_time):
        if (p_type == "xpath"):
            try:
                orig = self.Sel_by_Xpath(p_sel_orig, p_time)
                dest = self.Sel_by_Xpath(p_sel_dest, p_time)
                act = ActionChains(self.driver)
                act.drag_and_drop(orig, dest).perform()
                print("Drag element from {} to {} ".format(p_sel_orig, p_sel_dest))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Might be any of element {} or {} aren't available ".format(p_sel_orig, p_sel_dest))
                self.Time(p_time)
        elif (p_type == "id"):
            try:
                orig = self.Sel_by_ID(p_sel_orig)
                dest = self.Sel_by_ID(p_sel_dest)
                act = ActionChains(self.driver)
                act.drag_and_drop(orig, dest).perform()
                print("Drag element from {} to {} ".format(p_sel_orig, p_sel_dest))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("Might be any of element {} or {} aren't available ".format(p_sel_orig, p_sel_dest))
                self.Time(p_time)


    def f_DragandDrop_X_Y_Mix(self, p_type, p_sel, p_x, p_y,p_time):

            try:
                self.driver.switch_to.frame(0)
                if (p_type == "xpath"):
                 orig = self.Sel_by_Xpath(p_sel ,p_time)
                elif (p_type == "id"):
                 orig = self.Sel_by_ID(p_sel)

                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(orig, p_x, p_y).perform()
                print("The element {} was moved to {} to {} ".format(p_sel, p_x, p_y))
                self.Time(p_time)

            except TimeoutException as ex:
                print(ex.msg)
                print("element {}  isn't available ".format(p_sel))
                self.Time(p_time)
