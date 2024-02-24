from pages.signup_page.signup_page import SignupPage
from utils.utilities import Utilities
import pytest, constants, logging

@pytest.mark.usefixtures('setup_teardown')
class TestSignupPage:

  def setup_method(self, method):
    self.driver.delete_all_cookies()
    self.utils = Utilities(__name__, logging.DEBUG)
    self.signup = SignupPage(self.driver)
    self.log = self.utils.set_logger()
    self.log.debug("Setting up....")
    self.signup.load_page(constants.URL)
    self.log.info("Page is loaded successfully.")

  def test_signup_with_valid_credentials(self):
    self.log.info("Test - Signup with invalid credentials.")
    self.signup.click_signup_button()
    assert constants.URL in self.signup.get_current_url()
    assert constants.TITLE in self.signup.get_page_title()
    self.signup.click_signup_tab()
    self.log.info("Clicked Signup Tab.")
    self.signup.enter_username(constants.USERNAME)
    self.log.debug(f"Entered {constants.USERNAME} in the username field.")
    self.signup.enter_email(constants.EMAIL)
    self.log.debug(f"Entered {constants.EMAIL} in the email address field.")
    self.signup.enter_password(constants.PASSWORD)
    self.log.debug(f"Entered {constants.PASSWORD} in the password field.")
    self.signup.select_country(constants.COUNTRY)
    self.log.debug(f"Selected {constants.COUNTRY} in the country checkbox field.")
    self.signup.click_agree_checkbox()
    self.log.debug("Agree checkbox is checked.")
    self.signup.click_register_button()
    self.log.debug("Register button is clicked.")
    assert self.signup.get_current_url() == constants.VERIFICATION_URL
    assert self.signup.get_user_email_attribute_value() == constants.EMAIL

  @pytest.mark.signup
  def test_check_username_already_exists(self):
    self.log.info("Test - Signup with invalid credentials.")
    self.signup.click_signup_button()
    assert constants.URL in self.signup.get_current_url()
    assert constants.TITLE in self.signup.get_page_title()
    self.signup.click_signup_tab()
    self.log.info("Clicked Signup Tab.")
    self.signup.enter_username(constants.USERNAME)
    self.log.debug(f"Entered {constants.USERNAME} in the username field.")
    self.signup.press_tab_key()
    self.log.info("Pressed tab key.")
    self.signup.verify_username_already_taken_message_shows()
    self.log.info("Error message shown in UI.")

  @pytest.mark.signup
  def test_check_email_already_exists(self):
    self.log.info("Test - Signup with invalid credentials.")
    self.signup.click_signup_button()
    assert constants.URL in self.signup.get_current_url()
    assert constants.TITLE in self.signup.get_page_title()
    self.signup.click_signup_tab()
    self.log.info("Clicked Signup Tab.")
    self.signup.enter_email(constants.EMAIL)
    self.log.debug(f"Entered {constants.EMAIL} in the username field.")
    self.signup.press_tab_key()
    self.log.info("Pressed tab key.")
    self.signup.verify_email_already_taken_message_shows()
    self.log.info("Error message shown in UI.")
