from ProjectSeleniumPython.Pages.Functions import Functions


class Menu:
    """
    Page Object Model (POM) class for navigating the website's main menu,
    specifically: Women → Tops → Jackets.

    This class uses **composition** by accepting an instance of the `Functions` class,
    which provides utility methods for interacting with web elements.

    Attributes:
        f (Functions): A utility instance used to perform browser actions (e.g., hover, click).
        t (float): Time delay used for interaction timing (e.g., hover duration).
    """

    def __init__(self, functions: Functions, t: float):
        """
        Initializes the Menu object with helper functions and a time delay.

        Args:
            functions (Functions): An instance of the Functions utility class.
            t (float): Delay time in seconds used for element interactions.
        """
        self.f = functions
        self.t = t

        # LOCATORS
        self.MENU_WOMEN = "//span[contains(.,'Women')]"
        self.WOMEN_TOPS = (
            "//a[@id='ui-id-9' and span[@class='ui-menu-icon ui-icon ui-icon-carat-1-e']]"
            "/span[text()='Tops']"
        )
        self.WOMEN_TOPS_JACKETS = "//a[@id='ui-id-11']/span[text()='Jackets']"

    # METHODS: Here is the method to navigate_to_women_jacket fro example purpose, but for every menu option a method
    # should be created.

    def navigate_to_women_jacket(self):
        """
        Performs sequential actions to navigate to the 'Jackets' section
        under the 'Women > Tops' menu.

        Steps:
            1. Hover over the 'Women' main menu item.
            2. Hover over the 'Tops' submenu item.
            3. Click on the 'Jackets' submenu item.
        """
        self.f.move_to_element("xpath", self.MENU_WOMEN, self.t)
        self.f.move_to_element("xpath", self.WOMEN_TOPS, self.t)
        self.f.move_on_element_and_click("xpath", self.WOMEN_TOPS_JACKETS, self.t)
