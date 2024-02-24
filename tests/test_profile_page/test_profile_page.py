from pages.signup_page.signup_page import SignupPage
from pages.login_page.login_page import LoginPage
from pages.dashboard_page.dashboard_page import DashboardPage
from pages.profile_page.profile_page import ProfilePage
from utils.utilities import Utilities
import pytest, constants, logging

@pytest.mark.usefixtures("setup_teardown")
class TestContestPage:

  def setup_method(self, method):
    self.driver.delete_all_cookies()
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.set_logger()
    self.login_page = LoginPage(self.driver)
    self.signup_page = SignupPage(self.driver)
    self.dashboard_page = DashboardPage(self.driver)
    self.profile_page = ProfilePage(self.driver)
    self.logs.info("Initial Setup done.")
    self.profile_page.load_page(constants.URL)
    self.logs.info("Page load is success.")

  @pytest.mark.profile
  def test_update_account_name(self):
    self.signup_page.click_signup_button()
    self.logs.info("Signup button is clicked.")
    self.login_page.click_login_tab()
    self.logs.info("Login tab is clicked.")
    self.login_page.enter_username(constants.USERNAME1)
    self.logs.info(f"Entered {constants.USERNAME1} in the username field.")
    self.login_page.enter_password(constants.PASSWORD)
    self.logs.info(f"Entered {constants.PASSWORD} in the password field.")
    self.login_page.click_login_button()
    self.login_page.wait_for_profile_image()
    self.logs.info("Clicked login button.")
    self.logs.debug("Verified the elements in the codechef dashboard.")
    assert constants.DASHBOARD_URL == self.login_page.get_current_url()
    self.dashboard_page.click_profile_image(constants.USERNAME1)
    self.logs.info("Clicked profile image.")
    self.profile_page.click_edit_profile_button()
    self.logs.info("Clicked edit profile button.")
    assert constants.EDIT_PROFILE_URL.format(username=constants.USERNAME1) == self.profile_page.get_current_url()
    self.profile_page.click_general_Tab()
    self.logs.info("Clicked general tab.")
    self.profile_page.update_name(constants.NEW_NAME)
    self.logs.debug(f"Entered {constants.NEW_NAME} in the name field.")
    self.profile_page.click_save_button_in_general_tab()
    self.logs.info("Clicked save button.")
    assert self.profile_page.get_name_attribute_value() == constants.NEW_NAME
    self.profile_page.close_success_popup()

  @pytest.mark.profile
  def test_update_user_email(self):
    self.signup_page.click_signup_button()
    self.logs.info("Signup button is clicked.")
    self.login_page.click_login_tab()
    self.logs.info("Login tab is clicked.")
    self.login_page.enter_username(constants.USERNAME1)
    self.logs.info(f"Entered {constants.USERNAME1} in the username field.")
    self.login_page.enter_password(constants.PASSWORD)
    self.logs.info(f"Entered {constants.PASSWORD} in the password field.")
    self.login_page.click_login_button()
    self.login_page.wait_for_profile_image()
    self.logs.info("Clicked login button.")
    self.logs.debug("Verified the elements in the codechef dashboard.")
    assert constants.DASHBOARD_URL == self.login_page.get_current_url()
    self.dashboard_page.click_profile_image(constants.USERNAME1)
    self.logs.info("Clicked profile image.")
    self.profile_page.click_edit_profile_button()
    self.logs.info("Clicked edit profile button.")
    assert constants.EDIT_PROFILE_URL.format(username=constants.USERNAME1) == self.profile_page.get_current_url()
    self.profile_page.click_personal_tab()
    self.logs.info("Clicked personal tab.")
    self.profile_page.update_email(constants.EMAIL1)
    self.logs.debug(f"Entered {constants.EMAIL1} in the name field.")
    self.profile_page.click_save_button_in_personal_tab()
    self.logs.info("Clicked save button.")
    assert constants.EMAIL1 == self.profile_page.get_email_attribute_value()
    self.logs.debug(f"Assert {constants.EMAIL1} with {self.profile_page.get_email_attribute_value()}")
    self.profile_page.close_success_popup()

  @pytest.mark.profile
  def test_update_account_password(self):
    self.signup_page.click_signup_button()
    self.logs.info("Signup button is clicked.")
    self.login_page.click_login_tab()
    self.logs.info("Login tab is clicked.")
    self.login_page.enter_username(constants.USERNAME1)
    self.logs.info(f"Entered {constants.USERNAME1} in the username field.")
    self.login_page.enter_password(constants.PASSWORD)
    self.logs.info(f"Entered {constants.PASSWORD} in the password field.")
    self.login_page.click_login_button()
    self.login_page.wait_for_profile_image()
    self.logs.info("Clicked login button.")
    self.logs.debug("Verified the elements in the codechef dashboard.")
    assert constants.DASHBOARD_URL == self.login_page.get_current_url()
    self.dashboard_page.click_profile_image(constants.USERNAME1)
    self.logs.info("Clicked profile image.")
    self.profile_page.click_edit_profile_button()
    self.logs.info("Clicked edit profile button.")
    assert constants.EDIT_PROFILE_URL.format(username=constants.USERNAME1) == self.profile_page.get_current_url()
    self.profile_page.click_login_tab()
    self.logs.info("Clicked login tab.")
    self.profile_page.update_password(constants.PASSWORD, constants.NEW_PASSWORD)
    self.logs.debug(f"Updated old password {constants.PASSWORD} with {constants.NEW_PASSWORD}")
    self.profile_page.click_update_password_button()
    self.logs.info("Clicked update password button.")

