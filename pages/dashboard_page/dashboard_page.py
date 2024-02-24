from pages.base_page.base_page import BasePage
from pages.dashboard_page.dashboard_page_locators import DashboardPageLocators
from pages.signup_page.signup_page_locators import SignupPageLocators
from pages.account_page.account_page_locators import AccountPageLocators
from pages.contactus_page.contactus_page_locators import ContactusPageLocators
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(driver)

  def click_profile_image(self, username):
    self.click_webelement(DashboardPageLocators.PROFILE_IMAGE)
    username_xpath = DashboardPageLocators.PROFILE_USERNAME[1].format(username=username)
    PROFILE_USERNAME_XPATH = (By.XPATH, username_xpath)
    self.wait_until_element_should_be_visible(PROFILE_USERNAME_XPATH, 10)

  def click_logout_button(self):
    self.click_webelement(DashboardPageLocators.LOGOUT_BUTTON)
    self.wait_until_element_should_be_visible(SignupPageLocators.SIGNUP_BUTTON, 10)
    self.wait_until_element_should_be_visible(SignupPageLocators.HOME_PAGE_LABEL, 10)

  def click_account_button(self):
    self.click_webelement(DashboardPageLocators.ACCOUNT_PAGE_LINK)
    self.wait_until_element_should_be_visible(AccountPageLocators.USERNAME_LABEL, 10)
    self.wait_until_element_should_be_visible(AccountPageLocators.COUNTRY_LABEL, 10)
    self.wait_until_element_should_be_visible(AccountPageLocators.CODECHEF_RATING_LABEL, 10)

  def click_contactus_button(self):
    self.click_webelement(DashboardPageLocators.CONTACT_US_LINK)
    self.wait_until_element_should_be_visible(ContactusPageLocators.CONTACTUS_LABEL, 10)


