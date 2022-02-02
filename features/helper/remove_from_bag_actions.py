import time
from features.helper.actions import Actions
import unidecode


class RemoveFromBag:

    def __init__(self, context):
        self._context = context

    # Locators
    bag_btn = "mx.com.liverpool.shoppingapp:id/btn_header_bag"
    product_title = "mx.com.liverpool.shoppingapp:id/childSkuDisplayName"
    product_text = "Apple iphone xr de 64gb lcd 6.1 pulgadas desbloqueado"
    menu_item = "mx.com.liverpool.shoppingapp:id/menu_item_shopping_bag"
    empty_bag = "//*[@text='No has seleccionado ningún producto para comprar']"
    layout = "//*[@resource-id='mx.com.liverpool.shoppingapp:id/llWithoutProducts']/android.widget.TextView"
    no_products_txt = "No has seleccionado ningun producto para comprar"

    def verify_product_added(self):

        Actions(self._context).tap_on_element(self.bag_btn)

        text = Actions(self._context).get_attribute("text", self.product_title)
        if text == self.product_text:
            return True
        else:
            return False

    def tap_delete_button(self):
        Actions(self._context).tap_on_element(self.menu_item)
        time.sleep(4)
        Actions(self._context).tap_by_coordinates(286, 607)

    def verify_product_removed(self):

        text = ""
        r = Actions(self._context).get_attribute("text", self.layout, locatorType="xpath")
        if r is not None:
            text = unidecode.unidecode(r)
            text = text.replace('\r', '').replace('\n', '')

        if text == self.no_products_txt:
            return True
        else:
            return False
