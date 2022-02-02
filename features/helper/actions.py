import os.path

from appium.webdriver.common.mobileby import MobileBy
import logging
import features.helper.customLogger as cl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from datetime import datetime

class Actions:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, context):
        self._context = context

    def get_by_type(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "accid":
            return MobileBy.ACCESSIBILITY_ID
        if locatorType == "id":
            return MobileBy.ID
        elif locatorType == "name":
            return MobileBy.NAME
        elif locatorType == "xpath":
            return MobileBy.XPATH
        elif locatorType == "css":
            return MobileBy.CSS_SELECTOR
        elif locatorType == "class":
            return MobileBy.CLASS_NAME
        elif locatorType == "link":
            return MobileBy.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def get_element(self, locator, locatorType="id",wait_time=10):
        try:
            element = None
            locatorType = locatorType.lower()
            ltype = self.get_by_type(locatorType)
            wait = WebDriverWait(self._context.driver, wait_time)
            element = wait.until(EC.visibility_of_element_located((ltype, locator)))
            self.log.info("get_element - Element found with locator: " + locator + " Type: " + locatorType)
            return element

        except Exception as e:
            self.log.error("get_element - Element not found with locator: " + locator + " Type: " + locatorType)
            self.take_screenshot("get_element")
            return element

    def tap_on_element(self, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            if element is not None:
                element.click()
                self.log.info("tap_on_element - Tap on element: " + locator + " Type: " + locatorType)
                return True

        except Exception as e:
            self.log.error("tap_on_element - Can not tap on element: " + locator + " Type: " + locatorType)
            self.take_screenshot("tap_on_element")
            return False

    def tap_by_coordinates(self,x1,y1):
        try:
            TouchAction(self._context.driver).tap(x=x1, y=y1).perform()
            self.log.info("Tapping on coordinates x: " + str(x1) + " y: " + str(y1))

        except Exception as e:
            self.take_screenshot("tap_by_coordinates")
            self.log.error("An error has occurred when tapping on coordinates x:" + str(e))

    def send_keys(self, data, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            if element is not None:
                element.send_keys(data)
                self.log.info("Data sent to element: " + locator + " Type: " + locatorType)
        except Exception as e:
            self.take_screenshot("send_keys")
            self.log.error("Can not send data to element: " + locator + " Type: " + locatorType)

    def get_attribute(self, attrib, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            if element != None:
                res = element.get_attribute(attrib)
                self.log.info("Getting attribute: " + locator + " Type: " + locatorType)
            return res

        except Exception as e:
            self.take_screenshot("get_attribute")
            self.log.error("Can not get attribute: " + locator + " Type: " + locatorType)

    def switch_to_alert(self, opt="getText"):
        try:
            alert_obj = self._context.driver.switch_to.alert
            if opt == "dismiss":
                alert_obj.dismiss()
                self.log.info("Dismissing Modal")
            elif opt == "accept":
                alert_obj.accept()
                self.log.info("Accepting Modal")
            else:
                msg = alert_obj.text
                return alert_obj

        except Exception as e:
            self.take_screenshot("switch_to_alert")
            self.log.error("An error has occurred when dismissing/accepting modal " + str(e))

    def do_an_enter(self):
        try:
            self._context.driver.execute_script("mobile: performEditorAction", {'action': 'search'})
            self.log.info("Doing an Enter")

        except Exception as e:
            self.take_screenshot("do_an_enter")
            self.log.error("An error has occurred when doing an Enter")

    def scroll_until_element(self,locator, locatorType="id"):
        try:
            element_found = None
            inc = 1
            while inc != 20:
                element_found = self.get_element(locator, locatorType,wait_time=3)
                if element_found is not None:
                    return True
                    break
                else:
                    touch = TouchAction(self._context.driver)
                    touch.press(x=333, y=1000).wait(500).move_to(x=339, y=470).release().perform()
                    inc = inc + 1

        except Exception as e:
            self.take_screenshot("scroll_until_element")
            self.log.error("An error has occurred while scrolling " + str(e))
            return False

    def take_screenshot(self,resultMessage):

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        fileName = resultMessage + "." + current_time + ".png"
        screenshotDirectory = "../screenshots/temp/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory,relativeFileName)
        destinationDirectory = os.path.join(currentDirectory,screenshotDirectory)
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self._context.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except Exception as e:
            self.log.error("An error has occurred while taking the screenshot: " + str(e))