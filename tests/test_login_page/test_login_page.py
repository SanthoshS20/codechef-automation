from pages.login_page.login_page import LoginPage
from pages.signup_page.signup_page import SignupPage
import constants, logging, pytest
from utils.utilities import Utilities

@pytest.mark.usefixtures("setup_teardown")
class TestLoginPage:

  def setup_method(self):
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.set_logger()
    self.login_page = LoginPage(self.driver)
    self.signup_page = SignupPage(self.driver)
    self.driver.delete_all_cookies()
    self.login_page.load_page(constants.URL)
    self.logs.debug("Page is loaded successfully.")

  @pytest.mark.login
  def test_login_with_valid_credentials(self):
    self.signup_page.click_signup_button()
    self.logs.info("Signup button is clicked.")
    self.login_page.click_login_tab()
    self.logs.info("Login tab is clicked.")
    self.login_page.enter_username(constants.USERNAME)
    self.logs.info(f"Entered {constants.USERNAME} in the username field.")
    self.login_page.enter_password(constants.PASSWORD)
    self.logs.info(f"Entered {constants.PASSWORD} in the password field.")
    self.login_page.click_login_button()
    self.login_page.wait_for_profile_image()
    self.logs.info("Clicked login button.")
    self.logs.debug("Verified the elements in the codechef dashboard.")
    self.logs.info("Test Case is successful.")

  @pytest.mark.login
  def test_login_with_invalid_credentials(self):
    self.signup_page.click_signup_button()
    self.logs.info("Signup button is clicked.")
    self.login_page.click_login_tab()
    self.logs.info("Login tab is clicked.")
    self.login_page.enter_username(constants.USERNAME)
    self.logs.info(f"Entered {constants.USERNAME} in the username field.")
    self.login_page.enter_password(constants.WRONG_PASSWORD)
    self.logs.info(f"Entered {constants.WRONG_PASSWORD} in the password field.")
    self.login_page.click_login_button()
    self.logs.info("Clicked login button.")
    self.login_page.verify_invalid_credentials_message()
    self.logs.info("Login failed due to incorrect credentials.")

  @pytest.mark.login
  def test_login_with_old_password(self):
    self.signup_page.click_signup_button()
    self.logs.info("Signup button is clicked.")
    self.login_page.click_login_tab()
    self.logs.info("Login tab is clicked.")
    self.login_page.enter_username(constants.USERNAME)
    self.logs.info(f"Entered {constants.USERNAME1} in the username field.")
    self.login_page.enter_password(constants.PASSWORD)
    self.logs.info(f"Entered {constants.PASSWORD} in the password field.")
    self.login_page.click_login_button()
    self.logs.info("Clicked login button.")
    self.login_page.verify_invalid_credentials_message()
    self.logs.info("Login failed due to incorrect credentials.")

  @pytest.mark.login
  def test_login_with_old_email(self):
    self.signup_page.click_signup_button()
    self.logs.info("Signup button is clicked.")
    self.login_page.click_login_tab()
    self.logs.info("Login tab is clicked.")
    self.login_page.enter_username(constants.EMAIL1)
    self.logs.info(f"Entered {constants.EMAIL1} in the username field.")
    self.login_page.enter_password(constants.PASSWORD)
    self.logs.info(f"Entered {constants.PASSWORD} in the password field.")
    self.login_page.click_login_button()
    self.logs.info("Clicked login button.")
    self.login_page.verify_invalid_credentials_message()
    self.logs.info("Login failed due to incorrect credentials.")