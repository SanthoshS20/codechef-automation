from pages.base_page.base_page import BasePage
from pages.account_page.account_page_locators import AccountPageLocators

class AccountPage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(driver)

  def verify_username_in_account_page(self):
    self.wait_until_element_should_be_visible(AccountPageLocators.USERNAME_VALUE, 10)

  def verify_user_country_in_account_page(self):
    self.wait_until_element_should_be_visible(AccountPageLocators.COUNTRY_VALUE, 10)