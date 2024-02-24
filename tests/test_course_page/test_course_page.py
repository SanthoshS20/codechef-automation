from utils.utilities import Utilities
from pages.course_page.course_page import CoursePage
from pages.signup_page.signup_page import SignupPage
from pages.login_page.login_page import LoginPage
import pytest, logging, constants


@pytest.mark.usefixtures("setup_teardown")
class TestCoursePage:

  def setup_method(self, method):
    self.driver.delete_all_cookies()
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.set_logger()
    self.login_page = LoginPage(self.driver)
    self.signup_page = SignupPage(self.driver)
    self.course_page = CoursePage(self.driver)
    self.logs.info("Setup is done.")
    self.login_page.load_page(constants.URL)
    self.logs.info("Page load is success.")

  @pytest.mark.course
  def test_view_popular_course_list(self):
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
    self.course_page.click_course_navigation_item()
    self.logs.info("Clicked course navigation item")


  @pytest.mark.course
  def test_verify_search_course_functionality(self):
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
    self.course_page.click_course_navigation_item()
    self.logs.info("Clicked course navigation item")
    self.course_page.click_browse_all_course_button()
    self.logs.info("Clicked browse all course button.")
    assert constants.COURSES_URL == self.course_page.get_current_url()
    self.course_page.enter_text_in_search_field(constants.COURSE_NAME)
    self.logs.debug(f"Entered {constants.COURSE_NAME} in the search course field.")
    self.course_page.verify_dsa_python_course_visible()
    self.logs.info("Verified the DSA in Python course in the web page.")