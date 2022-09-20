import logging
import logging.config
import os
import pytest
import sys
from datetime import datetime
from utils.utils import read_config_file
from selenium import webdriver
from pages.page_factory import PageFactory
from setup.setup import Setup
from constants import Constants
from webdriver_manager.chrome import ChromeDriverManager

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))


def pytest_addoption(parser):
    parser.addoption('--si', '--settings', required=False,
                     default='{}/properties/settings.ini'.
                     format(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                     help="Path for config file")
    parser.addoption('--logger', required=False, default='root', help='Logger level')


@pytest.fixture(scope='session', autouse=True)
def logger(request):
    logging.config.fileConfig(request.config.getoption("--settings"))
    log = logging.getLogger(request.config.getoption('--logger'))
    return log


@pytest.fixture(scope='session')
def setup(request):
    config_ini = read_config_file(request.config.getoption("--settings"))
    return Setup(setup=config_ini)


@pytest.fixture
def div_driver(setup):
    path = ChromeDriverManager().install()
    driver = webdriver.Chrome(executable_path=path)
    driver.get(setup.url)
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def page(div_driver, logger):
    page = PageFactory(driver=div_driver, logger=logger)
    return page


@pytest.fixture(scope='session')
def email_for_test(logger):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    timestamp = timestamp % 1
    email = '{}{}{}'.format(Constants.email_prefix, timestamp, Constants.email_postfix)
    logger.info('Email for test:{}'.format(email))
    yield email
