from appium.webdriver.common.mobileby import MobileBy

from pages.main_page import BasePage


class SearchResultsPage(BasePage):
    first_result = (MobileBy.XPATH, "(//*[@resource-id='by.av.client:id/name'])[1]")

    def get_first_search_result(self):
        return self.find_element(self.first_result).text
