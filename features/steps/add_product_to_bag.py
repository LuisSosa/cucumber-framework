from behave import *
from features.helper.add_to_bag_actions import AddToBag


@given('the user selects a product')
def step_impl(context):
    AddToBag(context).select_product_found()


@when('tapping add to my bag button')
def step_impl(context):
    AddToBag(context).tap_add_to_bag_btn()


@then('the product is added to the bag')
def step_impl(context):
    assert AddToBag(context).verify_added_msg() == True
