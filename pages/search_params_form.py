from appium.webdriver.common.mobileby import MobileBy

from pages.main_page import BasePage


class SearchParamsForm(BasePage):
    dropdowns = {'brandDropdown': (MobileBy.XPATH, "(//*[@resource-id='by.av.client:id/button'])[1]"),
                 'modelDropdown': (MobileBy.XPATH, "(//*[@resource-id='by.av.client:id/button'])[2]")}
    results = (MobileBy.ID, 'by.av.client:id/showButton')

    def search_for_brand(self, brand):
        self.click(self.dropdowns['brandDropdown'])
        self.scrollDownClick(brand)

    def search_for_model(self, model):
        self.click(self.dropdowns['modelDropdown'])
        self.scrollDownClick(model)

    def show_results(self):
        self.click(self.results)
