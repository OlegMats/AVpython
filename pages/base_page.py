from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CustomCall:

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        tmp = self.i
        self.i += 1
        return tmp


class BasePage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def find_element(self, locator, n=3):
        wait = WebDriverWait(self.driver, 10)

        x = iter(CustomCall())
        while n > 1:
            try:
                wait.until(expected_conditions.visibility_of_element_located(locator))
                return self.driver.find_element(*locator)
            except Exception as e:
                self.logger.error(f"element failed attempt {next(x)} - {locator}")
                n -= 1
                if n == 1: raise NoSuchElementException("Could not locate element with value: %s" % str(locator))

    def click(self, locator, n=3):
        BasePage.find_element(self, locator, n).click()

    def send_keys(self, text, locator):
        BasePage.find_element(self, locator).clear()
        BasePage.find_element(self, locator).send_keys(text)

    def scrollDownClick(self, text):
        try:
            self.driver.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(\"" + text + "\").instance(0))").click()
        except NoSuchElementException:
            self.logger.error(f"Could not locate an element against the page with the following text value: {text}")
