from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions

t = .2
class CreateUsr(Functions):

    '''
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to SelectProduct as a dependency.
    '''

    def __init__(self, functions_instance):
        self.f = functions_instance  # Store the existing Functions instance
        self.FIRST_NAME = "//input[contains(@name,'firstname')]"
        self.LAST_NAME = "//input[contains(@name,'lastname')]"
        self.EMAIL = "//input[@type='email'][contains(@id,'address')]"
        self.PASSWORD = "//input[@title='Password']"
        self.CONFIRM_PASS = "//input[contains(@name,'password_confirmation')]"
        self.CREATE_BUTTON = "//button[@type='submit'][contains(.,'Create an Account')]"


    def EnterFirstName(self, p_firstName):
        self.f.move_to_element("xpath", self.FIRST_NAME, t)
        self.f.input_text("xpath",self.FIRST_NAME, p_firstName, t)

    def EnterLastName(self, p_lastName):
        self.f.move_to_element("xpath",self.LAST_NAME, t)
        self.f.input_text("xpath",self.LAST_NAME, p_lastName, t)

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
