import time

from pages.base_page.base_page import BasePage
from pages.login_page.login_page_locators import LoginPageLocators
from pages.dashboard_page.dashboard_page_locators import DashboardPageLocators
from pages.signup_page.signup_page_locators import SignupPageLocators

class LoginPage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(driver)

  def click_login_tab(self):
    self.click_webelement(LoginPageLocators.LOGIN_TAB)
    self.wait_until_element_should_be_visible(LoginPageLocators.LOGIN_INFO_LABEL, 10)
    self.wait_until_element_should_be_visible(LoginPageLocators.USERNAME_INPUT_FIELD, 10)

  def enter_username(self, username):
    self.send_text(LoginPageLocators.USERNAME_INPUT_FIELD, username)

  def enter_password(self, password):
    self.send_text(LoginPageLocators.PASSWORD_INPUT_FIELD, password)

  def click_login_button(self):
    self.execute_js_code(SignupPageLocators.SCROLL_PAGE_TO_VIEW_ELEMENT, self.get_webelement(LoginPageLocators.PASSWORD_INPUT_FIELD))
    self.click_webelement(LoginPageLocators.LOGIN_BUTTON)

  def wait_for_profile_image(self):
    self.wait_until_element_should_be_visible(DashboardPageLocators.PROFILE_IMAGE, 10)

  def click_forgot_password_link(self):
    self.click_webelement(LoginPageLocators.FORGOT_PASSWORD_LINK)
    self.wait_until_element_should_be_visible(LoginPageLocators.LOGGING_IN_BUTTON, 10)
    self.wait_until_element_should_be_visible(LoginPageLocators.CODECHEF_LOGO, 10)

  def verify_invalid_credentials_message(self):
    self.wait_until_element_should_be_visible(LoginPageLocators.INVALID_CREDENTIALS_ERROR_MESSAGE, 10)
    self.wait_until_element_should_be_visible(LoginPageLocators.FORGETTEN_PASSWORD_LINK, 10)