from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class CoursePageLocators(BasePageLocators):
  COURSES_NAVIGATION_ITEM = (By.XPATH, '//div[starts-with(@class,"_headerRightContainer")]//parent::span[text()="Courses"]')
  COURSE_POPUP_LIST = (By.XPATH, '//div[@class="_m-dropdown_cetlo_287 _l-username-dropdown_cetlo_583 "]')
  POPULAR_LIST_LABEL = (By.XPATH, '//div[starts-with(@class,"_headerRightContainer")]//parent::span[text()="Popular Topics"]')
  BROWSE_ALL_COURSES_BUTTON = (By.LINK_TEXT, 'Browse All Courses')
  COURSES_CATALOG_LABEL = (By.XPATH, '//h2[text()="All Courses Catalog"]')
  BROWSE_COURSES_SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Browse Courses"]')
  DSA_IN_PYTHON_COURSE = (By.XPATH, '//span[text()="Beginner DSA in Python"]')
