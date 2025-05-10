from ProjectSeleniumPython.Pages.Functions import Functions

t = .8


class SelectProduct(Functions):
    """
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to SelectProduct as a dependency.

     This is a small example that maps the functionality for selecting Juno Jacket from  Woman → Tops → Jackets options.
     There is a method to sort the products.

     Each product on Woman → Tops → Jackets page requires its own locator and a corresponding method implementation.
    """

    def __init__(self, functions):

        # f variable instantiate all the functionality from class Functions
        self.f = functions

        # LOCATORS for the web elements (buttons, fields, etc.)
        self.JUNO_JACKET = "//a[@class='product-item-link'][contains(.,'Juno Jacket')]"
        self.SORTER = "//select[@id='sorter']"

    # METHODS to perform actions on those elements
    def SelectJunoJacket(self):
        self.f.click_on_element("xpath", self.JUNO_JACKET, t)

    def SortByPrices(self, p_type, p_value):
        self.f.Select_Combo("xpath", self.SORTER, p_type, p_value, t)
