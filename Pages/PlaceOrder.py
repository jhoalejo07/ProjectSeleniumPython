from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions

t = .2
class PlaceOrder(Functions):

    """
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to SelectProduct as a dependency.
    """

    def __init__(self, functions_instance):
        self.f = functions_instance  # Store the existing Functions instance
        self.PLACE_BUTTON = "//span[contains(.,'Place Order')]"

    def PressPlaceOrder(self):
        self.f.move_on_element_and_click("xpath", self.PLACE_BUTTON, t)

