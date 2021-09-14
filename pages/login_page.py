from pages.main_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(BasePage):
    entrance_via_mail_or_login = (MobileBy.ID, 'by.av.client:id/chipEmailBg')
    mail_or_login_field = (MobileBy.ID, 'by.av.client:id/emailEditView')
    pass_field = (MobileBy.ID, 'by.av.client:id/passwordEditView')
    login_button = (MobileBy.ID, 'by.av.client:id/loginButton')

    def login_into_app_by_email(self, email, password):
        self.logger.info("choose login type - 'by email'")
        self.click(self.entrance_via_mail_or_login)
        self.logger.info("filling up email and password fields")
        self.send_keys(email, self.mail_or_login_field)
        self.send_keys(password, self.pass_field)
        self.logger.info("Click on login button")
        self.click(self.login_button)
