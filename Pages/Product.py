from ProjectSeleniumPython.utils.Functions import Functions

class Product:
    """
    🛍️ Product Class.

    This class is part of the Page Object Model (POM) structure and manages
    user interactions such as selecting the product characteristics and
    navigating to the shopping cart. For this project color, size were selected for Juno jacket and adding to cart.

    Methods should be developed in this class to handle the selection of all details for every product.

    🧩 Composition over Inheritance:
    An instance of the `Functions` class is passed in as a dependency to promote
    flexibility and clean architecture.

    Attributes:
        f (Functions): Instance that provides utility methods for UI interactions.
        t (float): Time delay for each interaction to allow UI elements to load.

        JUNO_JACKET_COLOR_GREEN (str): XPath locator for the green color option.
        JUNO_JACKET_SIZE_L (str): XPath locator for size L.
        ADD_TO_CART_BTN (str): XPath locator for the "Add to Cart" button.
        SHOPPING_CART_BTN (str): XPath locator for the link to the shopping cart.
        JUNO_JACKET_COLOR_BLUE_id (str): ID locator for blue color option.
        JUNO_JACKET_SIZE_M_id (str): ID locator for size M.
        ADD_TO_CART_BTN_id (str): ID locator for the "Add to Cart" button.
    """

    def __init__(self, functions: Functions, t: float):
        """
        Initializes the Product class with locators and a Functions instance.

        Args:
            functions (Functions): Utility class instance for interacting with elements.
            t (float): Delay time for UI actions.
        """
        self.f = functions
        self.t = t

        # Locators for green L jacket
        self.JUNO_JACKET_COLOR_GREEN = "//div[@id='option-label-color-93-item-53']"
        self.JUNO_JACKET_SIZE_L = "//div[@id='option-label-size-143-item-169']"
        self.ADD_TO_CART_BTN = "//button[@id='product-addtocart-button']"
        self.SHOPPING_CART_BTN = "//a[contains(text(),'shopping cart')]"

        # Locators for blue M jacket (using ID)
        self.JUNO_JACKET_COLOR_BLUE_id = "option-label-color-93-item-53"
        self.JUNO_JACKET_SIZE_M_id = "option-label-size-143-item-168"
        self.ADD_TO_CART_BTN_id = "product-addtocart-button"

    def select_juno_jacket_green_l(self):
        """
        🟢 Selects the Juno Jacket in green color and size L,
        then adds it to the cart and navigates to the shopping cart.
        """
        self.select_options_and_add_to_cart("xpath", self.JUNO_JACKET_COLOR_GREEN, self.JUNO_JACKET_SIZE_L)

    def select_juno_jacket_blue_m(self):
        """
        🔵 Selects the Juno Jacket in blue color and size M,
        then adds it to the cart and navigates to the shopping cart.
        """
        self.select_options_and_add_to_cart("id", self.JUNO_JACKET_COLOR_BLUE_id, self.JUNO_JACKET_SIZE_M_id)

    def select_options_and_add_to_cart(self, p_type: str, p_color: str, p_size: str):
        """
        📦 Selects color and size options, adds the product to the cart,
        and navigates to the shopping cart.

        Args:
            p_type (str): Locator type ("xpath" or "id").
            p_color (str): Locator for the selected color.
            p_size (str): Locator for the selected size.
        """
        self.f.move_on_element_and_click(p_type, p_color, self.t)
        self.f.move_on_element_and_click(p_type, p_size, self.t)
        self.f.move_on_element_and_click(p_type, self.ADD_TO_CART_BTN, self.t)
        self.f.move_on_element_and_click(p_type, self.SHOPPING_CART_BTN, self.t)

