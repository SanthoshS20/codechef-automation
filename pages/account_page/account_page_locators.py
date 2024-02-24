from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By
import constants

class AccountPageLocators(BasePageLocators):
  USERNAME_VALUE = (By.XPATH, f'//label[text()="Username:"]//parent::li//span[text()="{constants.USERNAME}"]')
  COUNTRY_VALUE = (By.XPATH, f'//label[text()="Country:"]//parent::li//span[text()="{constants.COUNTRY}"]')
  CODECHEF_RATING_LABEL = (By.XPATH, '//strong[text()="CodeChef Rating"]')
  USERNAME_LABEL = (By.XPATH, '//label[text()="Username:"]')
  COUNTRY_LABEL = (By.XPATH, '//label[text()="Country:"]')


