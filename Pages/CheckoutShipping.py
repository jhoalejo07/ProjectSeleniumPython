from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions

t = .2
class Checkout_Shipping(Functions):

    """
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to SelectProduct as a dependency.
    """

    def __init__(self, functions_instance):
        self.f = functions_instance  # Store the existing Functions instance
        self.FIRST_NAME = "//input[contains(@name,'firstname')]"
        self.LAST_NAME = "//input[contains(@name,'lastname')]"
        self.ADDRESS = "//input[@name='street[0]']"
        self.CITY = "//input[contains(@name,'city')]"
        self.STATE_PROV = "//select[contains(@name,'region_id')]"
        self.POSTALCODE = "//input[contains( @ name, 'postcode')]"
        self.COUNTRY = "//select[contains(@name,'country_id')]"
        self.PHONE = "//input[contains( @ name, 'telephone')]"
        self.EMAIL = "(//input[contains(@id,'customer-email')])[1]"


    def EnterFirstName(self, p_firstName):
        self.f.move_to_element("xpath", self.FIRST_NAME, t)
        self.f.input_text("xpath",self.FIRST_NAME, p_firstName, t)

    def EnterLastName(self, p_lastName):
        self.f.move_to_element("xpath",self.LAST_NAME, t)
        self.f.input_text("xpath",self.LAST_NAME, p_lastName, t)

    def EnterAddress(self, p_address):
        self.f.move_to_element("xpath",self.ADDRESS, t)
        self.f.input_text("xpath",self.ADDRESS, p_address, t)

    def EnterCity(self, p_city):
        self.f.move_to_element("xpath",self.CITY, t)
        self.f.input_text("xpath", self.CITY, p_city, t)

    def SelectStateProvince(self, p_type_sel, p_value):
        self.f.move_to_element("xpath", self.STATE_PROV, t)
        self.f.Select_Combo("xpath", self.STATE_PROV, p_type_sel, p_value, t)

    """

    def EnterEmail(self, p_email):
        self.f.move_to_element("xpath",self.EMAIL, t)
        self.f.input_text("xpath",self.EMAIL, p_email, t)

    def EnterPassw(self, p_password):
        self.f.move_to_element("xpath",self.PASSWORD, t)
        self.f.input_text("xpath",self.PASSWORD, p_password, t)

    def ConfirmPassw(self, p_password):
        self.f.move_to_element("xpath",self.CONFIRM_PASS, t)
        self.f.input_text("xpath",self.CONFIRM_PASS, p_password, t)

    def PressButtonCreate(self):
        self.f.move_on_element_and_click("xpath", self.CREATE_BUTTON, t)
    """
