from ProjectSeleniumPython.Pages.Functions import Functions

class SelectProduct:
    """
    Page Object Model class to interact with the product selection interface on the
    'Women > Tops > Jackets -' section of the Magento demo site.

    This class follows the composition pattern by receiving an instance of `Functions`
    instead of using inheritance.

    Functionality:
        - Selects the 'Juno Jacket' from the list of women's jackets.
        - Sorts the list of products based on user-defined criteria.

    Attributes:
        f (Functions): Utility class instance to handle interactions with web elements.
        t (float): Time delay for waits and element interactions.
        JUNO_JACKET (str): XPath locator for the 'Juno Jacket' product.
        SORTER (str): XPath locator for the sort-by dropdown element.

    Methods:
        select_juno_jacket(): Clicks on the 'Juno Jacket' product link.
        sort_by_prices(p_type, p_value): Selects an option from the sorting dropdown
                                         (e.g., sort by price or name).
    """

    def __init__(self, functions: Functions, t: float):
        """
        Initializes the SelectProduct class with the given Functions instance and wait time.

        Args:
            functions (Functions): An instance of the Functions utility class for interacting with the page.
            t (float): A delay time in seconds to use between interactions.
        """
        self.f = functions
        self.t = t

        # LOCATORS for the web elements
        self.JUNO_JACKET = "//a[@class='product-item-link'][contains(.,'Juno Jacket')]"
        self.SORTER = "//select[@id='sorter']"

    # METHODS to perform actions on those elements
    def select_juno_jacket(self):
        """
                Selects the 'Juno Jacket' product by clicking on its link.
        """
        self.f.click_on_element("xpath", self.JUNO_JACKET, self.t)

    def sort_by_prices(self, p_type, p_value):
        """
        Sorts the product list using the sorter dropdown.

        Args:
            p_type (str): The type of selection (e.g., 'value', 'visible_text', etc.).
            p_value (str): The value to be selected from the dropdown.
        """
        self.f.Select_Combo("xpath", self.SORTER, p_type, p_value, self.t)
