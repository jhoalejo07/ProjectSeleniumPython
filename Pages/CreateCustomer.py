from ProjectSeleniumPython.Pages.Functions import Functions


class CreateUsr:
    """
    The CreateUsr class automates the user registration process on a web page.

    Design Note:
    Composition is used instead of inheritance to promote loose coupling and greater flexibility.
    An instance of the `Functions` utility class is passed in to perform reusable browser actions.
    """

    def __init__(self, functions: Functions, t: float):
        """
        Initializes the CreateUsr page object with locators and shared utilities.

        Args:
            functions (Functions): An instance of the Functions class used to perform web actions.
            t (float): Time in seconds to wait during actions (e.g., delays for visibility).
        """
        self.FIRST_NAME = "//input[contains(@name,'firstname')]"
        self.LAST_NAME = "//input[contains(@name,'lastname')]"
        self.EMAIL = "//input[@type='email'][contains(@id,'address')]"
        self.PASSWORD = "//input[@title='Password']"
        self.CONFIRM_PASS = "//input[contains(@name,'password_confirmation')]"
        self.CREATE_BUTTON = "//button[@type='submit'][contains(.,'Create an Account')]"

        self.f = functions
        self.t = t

    def EnterFirstName(self, p_firstName):
        """
        Enters the user's first name into the input field.

        Args:
            p_firstName (str): First name to input.
        """
        self.f.move_to_element("xpath", self.FIRST_NAME, self.t)
        self.f.input_text("xpath", self.FIRST_NAME, p_firstName, self.t)

    def EnterLastName(self, p_lastName):
        """
        Enters the user's last name into the input field.

        Args:
            p_lastName (str): Last name to input.
        """
        self.f.move_to_element("xpath", self.LAST_NAME, self.t)
        self.f.input_text("xpath", self.LAST_NAME, p_lastName, self.t)

    def EnterEmail(self, p_email):
        """
        Enters the user's email address.

        Args:
            p_email (str): Email to input.
        """
        self.f.move_to_element("xpath", self.EMAIL, self.t)
        self.f.input_text("xpath", self.EMAIL, p_email, self.t)

    def EnterPassw(self, p_password):
        """
        Enters the password into the input field.

        Args:
            p_password (str): Password to input.
        """
        self.f.move_to_element("xpath", self.PASSWORD, self.t)
        self.f.input_text("xpath", self.PASSWORD, p_password, self.t)

    def ConfirmPassw(self, p_password):
        """
        Re-enters the password into the confirmation field.

        Args:
            p_password (str): Password to confirm.
        """
        self.f.move_to_element("xpath", self.CONFIRM_PASS, self.t)
        self.f.input_text("xpath", self.CONFIRM_PASS, p_password, self.t)

    def PressButtonCreate(self):
        """
        Clicks the "Create an Account" button to submit the form.
        """
        self.f.move_on_element_and_click("xpath", self.CREATE_BUTTON, self.t)