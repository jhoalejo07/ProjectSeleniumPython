from ProjectSeleniumPython.Pages.Functions import Functions

t = .8
class Product(Functions):

    '''
     Composition is generally preferred over inheritance for building page objects, as it leads to more flexible and
      maintainable code. For that reason, an instance of Functions is passed to SelectProduct as a dependency.
    '''
    def __init__(self, functions_instance):
        self.f = functions_instance  # Store the existing Functions instance
    def select_options_and_add_to_cart(self):
        self.f.move_on_element_and_click_by_xpath("//div[@id='option-label-color-93-item-53']", t)
        self.f.move_on_element_and_click_by_xpath("//div[@id='option-label-size-143-item-169']", t)
        self.f.move_on_element_and_click_by_xpath("//button[@id='product-addtocart-button']", t)
        self.f.move_on_element_and_click_by_xpath("//a[contains(text(),'shopping cart')]", t)