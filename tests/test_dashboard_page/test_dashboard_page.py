from utils.utilities import Utilities
from pages.dashboard_page.dashboard_page import DashboardPage
import pytest, logging, constants
from pages.login_page.login_page import LoginPage
from pages.signup_page.signup_page import SignupPage

@pytest.mark.usefixtures("setup_teardown")
class TestDashboardPage:

  def setup_method(self, method):
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.set_logger()
    self.login_page = LoginPage(self.driver)
    self.dashboard_page = DashboardPage(self.driver)
    self.signup_page = SignupPage(self.driver)
    self.logs.info("Setup is done.")
    self.login_page.load_page(constants.URL)
    self.logs.info("Page is loaded successfully.")

  @pytest.mark.dashboard
  def test_logout_from_current_account(self):
    self.logs.info("Logout from current account test case.")
    self.signup_page.click_signup_button()
    self.logs.info("Signup button is clicked.")
    self.login_page.click_login_tab()
    self.logs.info("Clicked login tab.")
    self.login_page.enter_username(constants.USERNAME)
    self.logs.debug(f"Entered {constants.USERNAME} value in username field.")
    self.login_page.enter_password(constants.PASSWORD)
    self.logs.debug(f"Entered {constants.PASSWORD} value in password field.")
    self.login_page.click_login_button()
    self.login_page.wait_for_profile_image()
    self.logs.info("Login button is clicked.")
    assert self.dashboard_page.get_current_url() == constants.DASHBOARD_URL
    self.logs.info("Login success.")
    self.dashboard_page.click_profile_image(constants.USERNAME)
    self.logs.info("Clicked profile image.")
    self.dashboard_page.click_logout_button()
    self.logs.info("Clicked logout button.")
    self.logs.debug("Logout success.")
    assert self.dashboard_page.get_current_url() == constants.URL
