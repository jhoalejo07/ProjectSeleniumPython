from ProjectSeleniumPython.Pages.Functions import Functions

t = .8


class Menu(Functions):
    """
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to Menu as a dependency.


    This is a small example that maps the functionality for selecting Women → Tops → Jackets from the menu.
    Each menu option requires its own locator and a corresponding method implementation.
    """

    def __init__(self, functions):
        # f variable instantiate all the functionality from class Functions
        self.f = functions

        # LOCATORS for the web elements (buttons, fields, etc.)
        self.MENU_WOMEN = "//span[contains(.,'Women')]"
        self.WOMEN_TOPS = "//a[@id='ui-id-9' and span[@class='ui-menu-icon ui-icon ui-icon-carat-1-e']]/span[""text()='Tops']"
        self.WOMEN_TOPS_JACKETS = "//a[@id='ui-id-11']/span[text()='Jackets']"

     #METHODS to perform actions on those elements
    def NavegateToWomenJacket(self):
        self.f.move_to_element("xpath", self.MENU_WOMEN, t)
        self.f.move_to_element("xpath", self.WOMEN_TOPS, t)
        self.f.move_on_element_and_click("xpath", self.WOMEN_TOPS_JACKETS, t)
