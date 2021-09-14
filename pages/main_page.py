from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class MainPage(BasePage):
    other = (MobileBy.ID, 'by.av.client:id/navigation_other')
    dialogs = (MobileBy.ID, 'by.av.client:id/navigation_dialogs')
    advertisement = (MobileBy.ID, 'by.av.client:id/navigation_adverts_collection')
    bookmark = (MobileBy.ID, 'by.av.client:id/navigation_bookmarks_collection')
    search = (MobileBy.ID, 'by.av.client:id/navigation_primary')

    def go_to_other(self):
        self.logger.info("Find and click on 'other' tab")
        self.click(self.other)

    def go_to_dialogs(self):
        self.click(self.dialogs)

    def go_to_advertisement(self):
        self.click(self.advertisement)

    def go_to_bookmark(self):
        self.click(self.bookmark)

    def go_to_search(self):
        self.click(self.search)
