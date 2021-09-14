from appium.webdriver.common.mobileby import MobileBy
from pages.main_page import BasePage


class OtherPage(BasePage):
    entrance_field = (MobileBy.ID, 'by.av.client:id/unauthorized')
    username = (MobileBy.ID, 'by.av.client:id/userName')

    def go_to_login_form(self):
        self.logger.info("go to login form")
        self.click(self.entrance_field)

    def get_username(self):
        return self.find_element(self.username).text
