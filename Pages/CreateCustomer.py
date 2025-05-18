from ProjectSeleniumPython.Pages.Functions import Functions


class CreateUsr:

    '''
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to SelectProduct as a dependency.
    '''

    def __init__(self, functions: Functions, t: float):

        self.FIRST_NAME = "//input[contains(@name,'firstname')]"
        self.LAST_NAME = "//input[contains(@name,'lastname')]"
        self.EMAIL = "//input[@type='email'][contains(@id,'address')]"
        self.PASSWORD = "//input[@title='Password']"
        self.CONFIRM_PASS = "//input[contains(@name,'password_confirmation')]"
        self.CREATE_BUTTON = "//button[@type='submit'][contains(.,'Create an Account')]"

        self.f = functions
        self.t = t

    def EnterFirstName(self, p_firstName):
        self.f.move_to_element("xpath", self.FIRST_NAME,  self.t)
        self.f.input_text("xpath",self.FIRST_NAME, p_firstName,  self.t)

    def EnterLastName(self, p_lastName):
        self.f.move_to_element("xpath",self.LAST_NAME,  self.t)
        self.f.input_text("xpath",self.LAST_NAME, p_lastName,  self.t)

    def EnterEmail(self, p_email):
        self.f.move_to_element("xpath",self.EMAIL,  self.t)
        self.f.input_text("xpath",self.EMAIL, p_email,  self.t)

    def EnterPassw(self, p_password):
        self.f.move_to_element("xpath",self.PASSWORD,  self.t)
        self.f.input_text("xpath",self.PASSWORD, p_password,  self.t)

    def ConfirmPassw(self, p_password):
        self.f.move_to_element("xpath",self.CONFIRM_PASS,  self.t)
        self.f.input_text("xpath",self.CONFIRM_PASS, p_password,  self.t)

    def PressButtonCreate(self):
        self.f.move_on_element_and_click("xpath", self.CREATE_BUTTON,  self.t)
