from ProjectSeleniumPython.Pages.Functions import Functions

t = .8
class SelectProduct(Functions):

    '''
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to SelectProduct as a dependency.
    '''
    def __init__(self, functions_instance):
        self.f = functions_instance  # Store the existing Functions instance
    def SelectJunoJacket(self):
        self.f.click_on_element_by_xpath("//a[@class='product-item-link'][contains(.,'Juno Jacket')]", t)

    def SortByPrices(self, p_type, p_value):
        self.f.f_Select_By_Xpath("//select[@id='sorter']", p_type, p_value, t)