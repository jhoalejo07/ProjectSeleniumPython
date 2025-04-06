from ProjectSeleniumPython.Pages.Functions import Functions

t = .8
class Menu(Functions):
    '''
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to Menu as a dependency.
    '''
    def __init__(self, functions_instance):
        self.f = functions_instance  # Store the existing Functions instance

   # global f = Functions(r"C:\SeleniumDrivers\chromedriver.exe")
    def NavegateToWomenJacket(self):
        self.f.move_to_element_by_xpath("//span[contains(.,'Women')]", t)
        self.f.move_to_element_by_xpath("//a[@id='ui-id-9' and span[@class='ui-menu-icon ui-icon ui-icon-carat-1-e']]/span["
                           "text()='Tops']", t)
        self.f.move_on_element_and_click_by_xpath("//a[@id='ui-id-11']/span[text()='Jackets']", t)
