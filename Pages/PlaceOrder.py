from ProjectSeleniumPython.utils.Functions import Functions


class PlaceOrder:
    """
     PlaceOrder Class — Handles the final step in the checkout process: placing the order.

     Design Principle:
    - Follows composition over inheritance by receiving an instance of the `Functions` class as a dependency.
    - This promotes flexibility, testability, and easier maintenance.

     Main Responsibility:
    - Automates the interaction with the "Place Order" button on the checkout page.
    """

    def __init__(self, functions: Functions, t: float):
        """
        Initializes the PlaceOrder class with required dependencies.

        :param functions: Instance of the utility class 'Functions' that provides browser interaction methods.
        :param t: Wait time used for all web element interactions.
        """
        self.f = functions
        self.t = t

        # Locator for the 'Place Order' button
        self.PLACE_BUTTON = "//span[contains(.,'Place Order')]"

    def PressPlaceOrder(self):
        """
         Clicks on the 'Place Order' button to submit the order.

        - Moves to the element and performs a click using the provided interaction functions.
        """
        self.f.move_on_element_and_click("xpath", self.PLACE_BUTTON, self.t)
