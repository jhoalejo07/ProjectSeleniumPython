from ProjectSeleniumPython.Pages.Functions import Functions

t = .8


class Product(Functions):
    """
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to SelectProduct as a dependency.

     Each product page requires locators and a corresponding method implementation to change size, color, quantity, add
     and go to the cart.
    """

    def __init__(self, functions_instance):
        self.f = functions_instance

        self.JUNO_JACKET_COLOR_GREEN = "//div[@id='option-label-color-93-item-53']"
        self.JUNO_JACKET_SIZE_L = "//div[@id='option-label-size-143-item-169']"
        self.ADD_TO_CART_BTN = "//button[@id='product-addtocart-button']"
        self.SHOPPING_CART_BTN = "//a[contains(text(),'shopping cart')]"
        self.JUNO_JACKET_COLOR_BLUE_id = "option-label-color-93-item-53"
        self.JUNO_JACKET_SIZE_M_id = "option-label-size-143-item-168"
        self.ADD_TO_CART_BTN_id = "product-addtocart-button"

    def select_juno_jacket_green_l(self):
        self.select_options_and_add_to_cart("xpath", self.JUNO_JACKET_COLOR_GREEN, self.JUNO_JACKET_SIZE_L)

    def select_juno_jacket_blue_m(self):
        self.select_options_and_add_to_cart("id", self.JUNO_JACKET_COLOR_BLUE_id, self.JUNO_JACKET_SIZE_M_id)

    def select_options_and_add_to_cart(self, p_type, p_color, p_size):
        self.f.move_on_element_and_click(p_type, p_color, t)
        self.f.move_on_element_and_click(p_type, p_size, t)
        self.f.move_on_element_and_click(p_type, self.ADD_TO_CART_BTN, t)
        self.f.move_on_element_and_click(p_type, self.SHOPPING_CART_BTN, t)

    """
    def add_to_cart(self, p_type="xpath"):
        if p_type == "xpath":
            self.f.move_on_element_and_click(p_type, self.ADD_TO_CART_BTN, t)
            self.f.move_on_element_and_click(p_type, self.SHOPPING_CART_BTN, t)
        else:
            self.f.move_on_element_and_click(p_type, self.ADD_TO_CART_BTN_id, t)
            self.f.move_on_element_and_click(p_type, self.SHOPPING_CART_BTN, t)

    """
