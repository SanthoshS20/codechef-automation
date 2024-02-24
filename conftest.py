import pytest
from selenium import webdriver


def pytest_addoption(parser):
  parser.addoption("--browser_name", action="store", default="firefox")

import os


@pytest.fixture(scope="class")
def setup_teardown(request):
  browser_name = request.config.getoption("--browser_name")
  global driver
  if(browser_name == "firefox"):
    # options = webdriver.FirefoxOptions()
    # webdriver_path = ':/driver/geckodriver'
    os.environ['PATH'] += ':/driver/geckodriver'
    # options.add_argument(f'--webdriver.gecko.driver={webdriver_path}')
    driver = webdriver.Firefox()
  elif(browser_name == "chrome"):
    driver = webdriver.Chrome()
  driver.maximize_window()
  request.cls.driver = driver
  yield
  driver.quit()
