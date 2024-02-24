from pages.base_page.base_page import BasePage
from pages.course_page.course_page_locators import CoursePageLocators

class CoursePage(BasePage):

  def __init(self, driver):
    self.driver = driver
    super().__init__(self.driver)

  def click_course_navigation_item(self):
    self.click_webelement(CoursePageLocators.COURSES_NAVIGATION_ITEM)
    self.wait_until_element_should_be_visible(CoursePageLocators.COURSE_POPUP_LIST, 10)
    self.wait_until_element_should_be_visible(CoursePageLocators.BROWSE_ALL_COURSES_BUTTON, 10)
    self.wait_until_element_should_be_visible(CoursePageLocators.POPULAR_LIST_LABEL, 10)

  def click_browse_all_course_button(self):
    self.click_webelement(CoursePageLocators.BROWSE_ALL_COURSES_BUTTON)
    self.wait_until_element_should_be_visible(CoursePageLocators.COURSES_CATALOG_LABEL, 10)
    self.wait_until_element_should_be_visible(CoursePageLocators.BROWSE_COURSES_SEARCH_FIELD, 10)

  def enter_text_in_search_field(self, course_name):
    self.send_text(CoursePageLocators.BROWSE_COURSES_SEARCH_FIELD, course_name)

  def verify_dsa_python_course_visible(self):
    self.wait_until_element_should_be_visible(CoursePageLocators.DSA_IN_PYTHON_COURSE, 10)
