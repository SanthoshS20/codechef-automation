from selenium.common.exceptions import ElementNotInteractableException
from pages.base_page.base_page import BasePage
from pages.signup_page.signup_page_locators import SignupPageLocators
import time


class SignupPage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(self.driver)

  def click_signup_tab(self):
    self.click_webelement(SignupPageLocators.SIGNUP_TAB)
    self.wait_until_element_should_be_visible(SignupPageLocators.CREATE_ACCOUNT_LABEL, 10)

  def enter_username(self, username):
    self.send_text(SignupPageLocators.USERNAME_INPUT_FIELD, username)

  def enter_email(self, email):
    self.send_text(SignupPageLocators.EMAIL_INPUT_FIELD, email)

  def enter_password(self, password):
    self.send_text(SignupPageLocators.PASSWORD_INPUT_FIELD, password)

  def click_agree_checkbox(self):
    self.execute_js_code(SignupPageLocators.SCROLL_PAGE_TO_VIEW_ELEMENT, self.get_webelement(SignupPageLocators.TERMS_AND_AGREEMENTS_CHECKBOX))
    time.sleep(2)
    # self.wait_until_element_should_be_enabled(SignupPageLocators.TERMS_AND_AGREEMENTS_CHECKBOX, 10)
    self.click_webelement(SignupPageLocators.TERMS_AND_AGREEMENTS_CHECKBOX)

  def select_country(self, country):
    self.select_option(SignupPageLocators.COUNTRY_DROPDOWN_FIELD, country)

  def click_register_button(self):
    self.click_webelement(SignupPageLocators.REGISTER_BUTTON)
    self.wait_until_element_should_be_visible(SignupPageLocators.REGISTERING_BUTTON, 10)
    self.wait_until_element_should_be_visible(SignupPageLocators.EMAIL_VERIFICATION_LABEL, 20)
    self.wait_until_element_should_be_visible(SignupPageLocators.ENTER_CODE_INPUT_FIELD, 10)

  def get_user_email_attribute_value(self):
    return self.get_element_attribute_value(SignupPageLocators.EMAIL_LABEL_FIELD, "value")

  def click_signup_button(self):
    self.click_webelement(SignupPageLocators.SIGNUP_BUTTON)
    try:
      self.click_webelement(SignupPageLocators.COOKIE_BUTTON)
    except ElementNotInteractableException:
      pass
    self.wait_until_element_should_be_visible(SignupPageLocators.SIGNUP_TAB, 10)

  def verify_email_already_taken_message_shows(self):
    self.wait_until_element_should_be_visible(SignupPageLocators.EMAIL_ALREADY_TAKEN_MESSAGE, 10)

  def verify_username_already_taken_message_shows(self):
    self.wait_until_element_should_be_visible(SignupPageLocators.USERNAME_ALREADY_TAKEN_MESSAGE, 10)