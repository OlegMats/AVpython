from appium.webdriver.common.mobileby import MobileBy
from pages.main_page import BasePage


class SearchPage(BasePage):
    search_with_params = (MobileBy.ID, 'by.av.client:id/collapseContainer')

    def go_to_search_with_params(self):
        self.click(self.search_with_params)
