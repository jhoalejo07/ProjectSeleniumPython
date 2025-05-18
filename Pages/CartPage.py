from ProjectSeleniumPython.Pages.Functions import Functions

class Cart:
    """
    Cart Class – Handles interactions on the Shopping Cart page.

    This class is part of the Page Object Model (POM) structure and for this project has methods to:
    - Modify the quantity of an item in the cart.
    - Proceed to the checkout process.

    ✅ Composition is used instead of inheritance by passing an instance of `Functions`.

    Attributes:
        f (Functions): An instance used to interact with UI elements.
        t (float): Time delay used for each interaction to ensure stability.

    Locators:
        SHOPPING_CART_QTY (str): XPath locator for the quantity input field.
        PROCEED_BUTTON (str): XPath locator for the "Proceed to Checkout" button.
    """

    # XPath locator for the quantity input field for the Juno Jacket (size L, green)
    SHOPPING_CART_QTY = "(//input[contains(@data-cart-item-id,'WJ06-L-Green')])[2]"

    # XPath locator for the "Proceed to Checkout" button
    PROCEED_BUTTON = "//button[span[text()='Proceed to Checkout']]"

    def __init__(self, functions: Functions, t: float):
        """
        Initializes the Cart class with required utilities.

        Args:
            functions (Functions): Object containing helper methods for Selenium actions.
            t (float): Time delay used for interactions.
        """
        self.f = functions
        self.t = t

    def modify_quantity(self, p_quantity):
        """
         Modifies the quantity of a product in the shopping cart.

        Args:
            p_quantity (int): The new quantity to set for the item.
        """

        self.f.input_text("xpath", self.SHOPPING_CART_QTY, str(p_quantity), self.t)

    def Proceed_to_checkout(self):
        """
         Proceeds to the checkout page by clicking the corresponding button.
        """
        self.f.move_on_element_and_click("xpath", self.PROCEED_BUTTON, self.t)
