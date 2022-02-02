from features.helper.actions import Actions
from features.helper.search_actions import SearchTests


class AddToBag:

    def __init__(self, context):
        self._context = context

    # Locators
    add_to_bag_btn = "mx.com.liverpool.shoppingapp:id/btnAddMyBag"
    popup = "//*[@text='Agregaste un producto a tu bolsa']"

    """TouchAction(driver)   .press(x=324, y=1285)   .move_to(x=336, y=1050)   .release()   .perform()"""

    def select_product_found(self):
        Actions(self._context).tap_on_element(SearchTests.myProduct, locatorType="xpath")

    def tap_add_to_bag_btn(self):
        Actions(self._context).scroll_until_element(self.add_to_bag_btn)
        Actions(self._context).tap_on_element(self.add_to_bag_btn)

    def verify_added_msg(self):
        r = Actions(self._context).get_element(self.popup, locatorType="xpath")
        if r is not None:
            return True
        else:
            return False
