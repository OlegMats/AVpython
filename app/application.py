import os

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.other_page import OtherPage
from pages.search_page import SearchPage
from pages.search_params_form import SearchParamsForm
from pages.search_results_page import SearchResultsPage


class Application:
    def __init__(self, driver, logger):
        print(os.environ.get('PYTEST_CURRENT_TEST'))
        logger.info("Running test case: " + os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0])
        logger.info("Initiating pages")
        self.main_page = MainPage(driver, logger)
        self.other_page = OtherPage(driver, logger)
        self.login_page = LoginPage(driver, logger)
        self.search_page = SearchPage(driver, logger)
        self.search_params_form = SearchParamsForm(driver, logger)
        self.search_results_page = SearchResultsPage(driver, logger)
