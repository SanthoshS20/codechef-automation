from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class LoginPageLocators(BasePageLocators):
  LOGIN_TAB = (By.ID, 'login')
  USERNAME_INPUT_FIELD = (By.XPATH, '//input[@id="edit-name" and @maxlength="128"]')
  PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@id="edit-pass" and @data="1"]')
  LOGIN_INFO_LABEL = (By.XPATH, '//h2[text()="Already have an account?"]')
  LOGIN_BUTTON = (By.XPATH, '//input[@id="edit-submit-button" and @value="Login"]')
  FORGOT_PASSWORD_LINK = (By.CLASS_NAME, 'm-list__link.m-forgot-password')
  LOGGING_IN_BUTTON = (By.XPATH, '//input[@value="Logging In..."]')
  CODECHEF_LOGO = (By.XPATH, '//img[contains(@src, "cc-logo-mobile")]')
  FORGETTEN_PASSWORD_LINK = (By.LINK_TEXT, 'Have you forgotten your password?')
  INVALID_CREDENTIALS_ERROR_MESSAGE = (By.XPATH, '//div[text()="Sorry, unrecognized credentials. "]')
