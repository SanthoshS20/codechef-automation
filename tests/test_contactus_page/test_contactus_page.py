from pages.login_page.login_page import LoginPage
from pages.signup_page.signup_page import SignupPage
from pages.contactus_page.contactus_page import ContactusPage
from pages.dashboard_page.dashboard_page import DashboardPage
from utils.utilities import Utilities
import pytest, logging, constants

@pytest.mark.usefixtures("setup_teardown")
class TestContactusPage:

  def setup_method(self, method):
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.set_logger()
    self.login_page = LoginPage(self.driver)
    self.signup_page = SignupPage(self.driver)
    self.contactus_page = ContactusPage(self.driver)
    self.dashboard_page = DashboardPage(self.driver)
    self.logs.info("Setup is done.")
    self.contactus_page.load_page(constants.URL)
    self.logs.info("Page load is success.")

  @pytest.mark.contactus
  def test_contactus_information_details(self):
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
    self.dashboard_page.click_contactus_button()
    self.logs.info("Clicked contact us button.")
    assert self.contactus_page.get_current_url() == constants.CONTACT_US_URL
    self.contactus_page.verify_all_contact_information_visible()
    self.logs.info("Verified all contact informations.")