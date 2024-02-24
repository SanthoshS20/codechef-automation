from pages.account_page.account_page import AccountPage
from pages.login_page.login_page import LoginPage
from pages.signup_page.signup_page import SignupPage
from pages.dashboard_page.dashboard_page import DashboardPage
from utils.utilities import Utilities
import pytest, constants, logging

@pytest.mark.usefixtures("setup_teardown")
class TestAccountPage:

  def setup_method(self, method):
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.set_logger()
    self.login_page = LoginPage(self.driver)
    self.signup_page = SignupPage(self.driver)
    self.account_page = AccountPage(self.driver)
    self.dashboard_page = DashboardPage(self.driver)
    self.logs.info("Setup is done.")
    self.login_page.load_page(constants.URL)
    self.logs.info("Page load is success.")

  @pytest.mark.account
  def test_verify_user_account_details(self):
    self.logs.info("Verify user account details.")
    self.signup_page.click_signup_button()
    self.logs.info("Clicked signup button")
    self.login_page.click_login_tab()
    self.logs.info("Click login tab.")
    self.login_page.enter_username(constants.USERNAME)
    self.logs.debug(f"Entered {constants.USERNAME} into username field.")
    self.login_page.enter_password(constants.PASSWORD)
    self.logs.debug(f"Entered {constants.PASSWORD} into password field.")
    self.login_page.click_login_button()
    self.login_page.wait_for_profile_image()
    self.logs.info("Clicked login button.")
    assert self.login_page.get_current_url() == constants.DASHBOARD_URL
    self.logs.debug("Asserted current url.")
    self.dashboard_page.click_profile_image(constants.USERNAME)
    self.logs.info("Clicked profile image.")
    self.dashboard_page.click_account_button()
    self.logs.info("Clicked account button.")
    self.account_page.verify_username_in_account_page()
    self.logs.debug("Verified username in the account page.")
    self.account_page.verify_user_country_in_account_page()
    self.logs.debug("Verified user country in the account page.")
    assert self.account_page.get_current_url() == constants.ACCOUNT_URL
    self.logs.debug("Asserted current url.")
