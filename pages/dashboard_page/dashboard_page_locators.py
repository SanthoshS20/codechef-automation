from selenium.webdriver.common.by import By
import constants
from pages.base_page.base_page_locators import BasePageLocators

class DashboardPageLocators(BasePageLocators):
  PROFILE_IMAGE = (By.XPATH, '//img[@alt="user profile"]')
  PROFILE_USERNAME = (By.XPATH, '//span[text()="{username}"]')
  ACCOUNT_PAGE_LINK = (By.XPATH, '//p[text()="Account"]')
  LOGOUT_BUTTON = (By.XPATH, '//button[text()="Logout"]')
  CONTACT_US_LINK = (By.LINK_TEXT, 'Contact Us')
