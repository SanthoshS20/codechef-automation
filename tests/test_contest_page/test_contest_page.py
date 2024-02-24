from pages.contest_page.contest_page import ContestPage
from pages.signup_page.signup_page import SignupPage
from pages.login_page.login_page import LoginPage
from utils.utilities import Utilities
import pytest, constants, logging

@pytest.mark.usefixtures("setup_teardown")
class TestContestPage:

  def setup_method(self, method):
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.set_logger()
    self.login_page = LoginPage(self.driver)
    self.signup_page = SignupPage(self.driver)
    self.contest_page = ContestPage(self.driver)
    self.logs.info("Initial Setup done.")
    self.contest_page.load_page(constants.URL)
    self.logs.info("Page load is success.")

  @pytest.mark.contest
  def test_view_ongoing_contest(self):
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
    self.contest_page.click_complete_button()
    self.logs.debug("Clicked compete button.")
    assert self.contest_page.get_current_url() == constants.CONTEST_URL
    self.contest_page.verify_default_contest_list()
    self.logs.info("Verified default contest page.")
    self.contest_page.click_show_all_contests_switch()
    self.logs.info("Enabled show all contests switch.")
    self.contest_page.verify_ongoing_contest_list()
    self.logs.info("Verified ongoing contest.")
