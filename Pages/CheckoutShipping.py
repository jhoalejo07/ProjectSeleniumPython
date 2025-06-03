from ProjectSeleniumPython.utils.Functions import Functions


class Checkout_Shipping:
    """
    Checkout_Shipping Class

    This class automates interactions with the shipping step in an e-commerce checkout flow.
    It uses composition to include the reusable 'Functions' utility class for performing
    Selenium actions like clicking, sending keys, and selecting dropdown options.

    Responsibilities:
    - Fill out customer shipping information
    - Select shipping method
    - Proceed to the next step in the checkout process

    Parameters:
    - functions (Functions): An instance of the Functions class to perform Selenium actions
    - t (float): Time delay used in all element interactions (for waits/synchronization)
    """

    # Locators for the shipping form fields and controls
    FIRST_NAME = "//input[contains(@name,'firstname')]"
    LAST_NAME = "//input[contains(@name,'lastname')]"
    ADDRESS = "//input[@name='street[0]']"
    CITY = "//input[contains(@name,'city')]"
    STATE_PROV = "//select[contains(@name,'region_id')]"
    POSTALCODE = "//input[contains(@name, 'postcode')]"
    COUNTRY = "//select[contains(@name,'country_id')]"
    PHONE = "//input[contains(@name, 'telephone')]"
    EMAIL = "(//input[contains(@id,'customer-email')])[1]"
    SP_TableRate = "//input[contains(@aria-labelledby,'label_method_bestway_tablerate label_carrier_bestway_tablerate')]"
    SP_Fixed = "//input[contains(@aria-labelledby,'label_method_flatrate_flatrate label_carrier_flatrate_flatrate')]"
    NEXT_BUTTON = "//button[contains(@data-role,'opc-continue')]"

    def __init__(self, functions: Functions, t: float):
        """
        Constructor for Checkout_Shipping

        :param functions: Instance of Functions class for Selenium interactions
        :param t: Float indicating wait/sleep time between actions
        """
        self.f = functions
        self.t = t

    def EnterFirstName(self, p_firstName):
        """Enter the customer's first name into the input field."""
        self.f.move_to_element("xpath", self.FIRST_NAME, self.t)
        self.f.input_text("xpath", self.FIRST_NAME, p_firstName, self.t)

    def EnterLastName(self, p_lastName):
        """Enter the customer's last name into the input field."""
        self.f.move_to_element("xpath", self.LAST_NAME, self.t)
        self.f.input_text("xpath", self.LAST_NAME, p_lastName, self.t)

    def EnterAddress(self, p_address):
        """Enter the customer's street address."""
        self.f.move_to_element("xpath", self.ADDRESS, self.t)
        self.f.input_text("xpath", self.ADDRESS, p_address, self.t)

    def EnterCity(self, p_city):
        """Enter the customer's city."""
        self.f.move_to_element("xpath", self.CITY, self.t)
        self.f.input_text("xpath", self.CITY, p_city, self.t)

    def SelectStateProvince(self, p_type_sel, p_value):
        """
        Select a state or province from the dropdown.

        :param p_type_sel: Type of selection (e.g., 'text', 'value', or 'index')
        :param p_value: The value to select
        """
        self.f.move_to_element("xpath", self.STATE_PROV, self.t)
        self.f.Select_Combo("xpath", self.STATE_PROV, p_type_sel, p_value, self.t)

    def EnterPostalCode(self, p_postalcode):
        """Enter the postal/zip code."""
        self.f.move_to_element("xpath", self.POSTALCODE, self.t)
        self.f.input_text("xpath", self.POSTALCODE, p_postalcode, self.t)

    def SelectCountry(self, p_type_sel, p_value):
        """
        Select a country from the dropdown.

        :param p_type_sel: Type of selection (e.g., 'text', 'value', or 'index')
        :param p_value: The value to select
        """
        self.f.move_to_element("xpath", self.COUNTRY, self.t)
        self.f.Select_Combo("xpath", self.COUNTRY, p_type_sel, p_value, self.t)

    def EnterTelephone(self, p_telephone):
        """Enter the customer's phone number."""
        self.f.move_to_element("xpath", self.PHONE, self.t)
        self.f.input_text("xpath", self.PHONE, p_telephone, self.t)

    def EnterEmail(self, p_email):
        """Enter the customer's email address."""
        self.f.move_to_element("xpath", self.EMAIL, self.t)
        self.f.input_text("xpath", self.EMAIL, p_email, self.t)

    def CheckShippingTableRate(self):
        """Select the 'Table Rate' shipping option."""
        self.f.click_on_element("xpath", self.SP_TableRate, self.t)

    def CheckShippingFixed(self):
        """Select the 'Fixed Rate' shipping option."""
        self.f.click_on_element("xpath", self.SP_Fixed, self.t)

    def PressNext(self):
        """Click the 'Next' button to proceed in the checkout process."""
        self.f.move_on_element_and_click("xpath", self.NEXT_BUTTON, self.t)
