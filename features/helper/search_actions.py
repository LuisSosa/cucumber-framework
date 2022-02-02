from features.helper.actions import Actions


class SearchTests:

    def __init__(self, context):
        self._context = context

    # Locators
    myAccount_btn = "Mi cuenta"
    search_bar = "mx.com.liverpool.shoppingapp:id/edt_header_searchbar_old"
    search_bar_2 = "mx.com.liverpool.shoppingapp:id/edt_header_searchbar"
    deny_permission_btn = "com.android.permissioncontroller:id/permission_deny_button"
    close_location_btn = "mx.com.liverpool.shoppingapp:id/imgClose"
    close_market_btn = "mx.com.liverpool.shoppingapp:id/btnClose"
    home_btn = "Inicio"
    login_opt = "//*[@text='Inicia sesión']"
    myProduct = "//*[@text='Apple iPhone XR de 64GB LCD 6.1 Pulgadas Desbloqueado']"

    def verify_home_screen_selected(self):

        Actions(self._context).tap_on_element(self.deny_permission_btn)

        Actions(self._context).tap_on_element(self.close_location_btn)

        Actions(self._context).tap_on_element(self.close_market_btn)

        return Actions(self._context).get_attribute("selected", self.home_btn, locatorType="accid")

    def enter_search_criteria(self, product):

        Actions(self._context).tap_on_element(self.search_bar)

        Actions(self._context).send_keys(product, self.search_bar_2)

        Actions(self._context).do_an_enter()

    def tap_on_myAccount_button(self):

        Actions(self._context).tap_on_element(self.myAccount_btn, locatorType="accid")

    def tap_on_login_opt(self):

        Actions(self._context).tap_on_element(self.login_opt, locatorType="xpath")

    def enter_email(self, data):

        Actions(self._context).send_keys(data, self.email_inp, locatorType="id")

    def search_product(self):
        x = Actions(self._context).scroll_until_element(self.myProduct, locatorType="xpath")
        if x:
            return True
        else:
            return False
