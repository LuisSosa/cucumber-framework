from behave import *
from features.helper.remove_from_bag_actions import RemoveFromBag


@given('the user added a product to the bag')
def step_impl(context):
    assert RemoveFromBag(context).verify_product_added() == True


@when('tapping the delete button')
def step_impl(context):
    RemoveFromBag(context).tap_delete_button()


@then('the product is removed successfully')
def step_impl(context):
    assert RemoveFromBag(context).verify_product_removed() == True
