from selenium.webdriver.common.by import By
from ProjectSeleniumPython.Pages.Functions import Functions

t = .8
class Cart(Functions):

    '''
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to SelectProduct as a dependency.
    '''
    SHOPPING_CART_QTY = "(//input[contains(@data-cart-item-id,'WJ06-L-Green')])[2]"
    PROCEED_BUTTON = "//button[span[text()='Proceed to Checkout']]"
    def __init__(self, functions_instance):
        self.f = functions_instance  # Store the existing Functions instance
    def modifyQuantity(self, p_quantity):
        self.f.input_text("xpath", self.SHOPPING_CART_QTY, p_quantity, t)

    def ProceedToCheckout(self):
        self.f.move_on_element_and_click("xpath", self.PROCEED_BUTTON, t)
