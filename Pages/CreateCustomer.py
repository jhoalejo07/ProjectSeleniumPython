from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions

t = .8
class CreateUsr(Functions):

    '''
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to SelectProduct as a dependency.
    '''
    FIRST_NAME = "//input[contains(@name,'firstname')]"
    LAST_NAME = "//input[contains(@name,'lastname')]"
    EMAIL = "//input[@type='email'][contains(@id,'address')]"
    PASSWORD = "//input[@title='Password']"
    CONFIRM_PASS = "//input[contains(@name,'password_confirmation')]"
    CREATE_BUTTON = "//button[@type='submit'][contains(.,'Create an Account')]"
    def __init__(self, functions_instance):
        self.f = functions_instance  # Store the existing Functions instance
    def EnterFirstName(self, p_firstName):
        self.f.move_to_element_by_xpath(self.FIRST_NAME, t)
        self.f.f_text_Mix("xpath",self.FIRST_NAME, p_firstName, t)

    def EnterLastName(self, p_lastName):
        self.f.move_to_element_by_xpath(self.LAST_NAME, t)
        self.f.f_text_Mix("xpath",self.LAST_NAME, p_lastName, t)

    def EnterEmail(self, p_email):
        self.f.move_to_element_by_xpath(self.EMAIL, t)
        self.f.f_text_Mix("xpath",self.EMAIL, p_email, t)

    def EnterPassw(self, p_password):
        self.f.move_to_element_by_xpath(self.PASSWORD, t)
        self.f.f_text_Mix("xpath",self.PASSWORD, p_password, t)

    def ConfirmPassw(self, p_password):
        self.f.move_to_element_by_xpath(self.CONFIRM_PASS, t)
        self.f.f_text_Mix("xpath",self.CONFIRM_PASS, p_password, t)

    def PressButtonCreate(self):
        self.f.move_on_element_and_click_by_xpath(self.CREATE_BUTTON, t)