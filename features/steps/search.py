from behave import *
from features.helper.search_actions import SearchTests

@given('the user is in Home screen')
def step_impl(context):

  assert SearchTests(context).verify_home_screen_selected() == "true"

@when('entering a product in the search bar')
def step_impl(context):

  SearchTests(context).enter_search_criteria("iphone")

@then('the product is displayed')
def step_imp(context):

  assert SearchTests(context).search_product() == True
