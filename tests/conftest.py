import logging
import os
from datetime import datetime

import pytest
from appium import webdriver


@pytest.fixture(scope="class")
def driver(get_logger):
    logger = get_logger
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion":"11",
        "app": f"{os.getcwd()}/app_binaries/av_by.apk"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    logger.info("initiating driver")
    yield driver
    logger.handlers.clear()
    driver.quit()


@pytest.fixture(scope='class')
def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.FileHandler(
        rf"logs/{os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split('[')[0]}{datetime.now().strftime('%H%M%S_%d%m%Y')}.log",
        mode='w')
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', '%m/%d/%Y %I:%M:%S %p')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    if request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['driver']
            take_screenshot(driver, request.node.nodeid)


def take_screenshot(driver, nodeid):
    driver.save_screenshot(
        "screenshots\\" + f"{nodeid}".split('::')[-1].split("[")[0] + f"_{datetime.now().strftime('%H%M%S_%d%m%Y')}.png")
