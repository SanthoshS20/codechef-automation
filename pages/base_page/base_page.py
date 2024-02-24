import constants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

  def __init__(self, driver):
    self.driver = driver

  def load_page(self, web_url):
    self.driver.get(web_url)

  def navigate_to(self):
    self.driver.navigate().to(constants.URL)

  def reload_page(self):
    self.driver.navigate().refresh()

  def navigate_back(self):
    self.driver.navigate().back()

  def navigate_forward(self):
    self.driver.navigate().forward()

  def get_current_url(self):
    return self.driver.current_url

  def get_page_title(self):
    return self.driver.title

  def click_webelement(self, locator):
    self.driver.find_element(*locator).click()

  def create_action_chains_object(self):
    self.action_chains = ActionChains(self.driver)
    return self.action_chains

  def press_tab_key(self):
    self.action = self.create_action_chains_object()
    self.action.send_keys(Keys.TAB).perform()

  def press_control_click(self, locator):
    self.webelement = self.get_webelement(locator)
    self.action = self.create_action_chains_object()
    self.action.key_down(Keys.CONTROL).click(self.webelement).key_up(Keys.CONTROL).perform()

  def send_text(self, locator, text):
    self.driver.find_element(*locator).send_keys(text)
    
  def clear_text(self, locator):
    self.driver.find_element(*locator).clear()

  def get_webelement(self, locator):
    return self.driver.find_element(*locator)

  def get_element_text(self, locator):
    return self.get_webelement(locator).text

  def get_element_attribute_value(self, locator, attribute):
    return self.get_webelement(locator).get_attribute(attribute)

  def execute_js_code(self, script, elements):
    self.driver.execute_script(script, elements)

  def web_driver_wait(self, seconds):
    self.wait = WebDriverWait(self.driver, seconds)
    return self.wait

  def check_element_is_enabled(self, locator):
    self.get_webelement(locator).is_enabled()

  def select_option(self, locator, option):
    self.dropdown = Select(self.get_webelement(locator))
    self.dropdown.select_by_visible_text(option)

  def wait_until_element_should_be_visible(self, locator, seconds):
    self.wait = self.web_driver_wait(seconds)
    self.wait.until(expected_conditions.visibility_of_element_located(locator))

  def wait_until_element_should_not_be_visible(self, locator, seconds):
    self.wait = self.web_driver_wait(seconds)
    self.wait.until_not(expected_conditions.visibility_of_element_located(locator))

  def wait_until_element_should_be_enabled(self, locator, seconds):
    self.wait = self.web_driver_wait(seconds)
    self.wait.until(expected_conditions.element_to_be_clickable(locator))
