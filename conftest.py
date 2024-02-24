import pytest, os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
  parser.addoption("--browser_name", action="store", default="firefox")

@pytest.fixture(scope="class")
def setup_teardown(request):
  browser_name = request.config.getoption("--browser_name")
  global driver
  if(browser_name == "firefox"):
    # Setup headless mode
    options = Options()
    options.headless = True
    # Add geckodriver executable in the system's PATH environment variable
    os.environ['PATH'] += ':/driver/geckodriver'
    driver = webdriver.Firefox(options=options)
  elif(browser_name == "chrome"):
    driver = webdriver.Chrome()
  driver.maximize_window()
  request.cls.driver = driver
  yield
  driver.quit()
