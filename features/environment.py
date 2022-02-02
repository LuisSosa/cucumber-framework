import time

from appium import webdriver

def before_all(context):
    try:
        desired_cap = {
            "deviceName": "Galaxy Note9",
            "udid": "266a0ad007057ece",
            "automationName": "UiAutomator2",
            "platformName": "Android",
            "platformVersion": "10",
            "appPackage": "mx.com.liverpool.shoppingapp",
            "appActivity": "mx.com.liverpool.shoppingapp.splash.SplashActivity"

        }
        context.driver = webdriver.Remote(
            command_executor="http://localhost:4723/wd/hub",
            desired_capabilities=desired_cap
        )
    except Exception as e:
        print(str(e))


def after_all(context):
    time.sleep(5)
    context.driver.quit()