from selenium.webdriver.common.by import By
from pages.base_page.base_page_locators import BasePageLocators

class SignupPageLocators(BasePageLocators):
  HOME_PAGE_LABEL = (By.XPATH, '//h1[text()="Start your coding journey today"]')
  COOKIE_BUTTON = (By.CLASS_NAME, "button.grey.tiny")
  CREATE_ACCOUNT_LABEL = (By.XPATH, '//h2[text()="Create Your CodeChef Account"]')
  SIGNUP_TAB = (By.ID, 'signup')
  USERNAME_INPUT_FIELD = (By.ID, 'edit-username')
  EMAIL_INPUT_FIELD = (By.NAME, 'mail')
  PASSWORD_INPUT_FIELD = (By.ID, 'edit-password')
  COUNTRY_DROPDOWN_FIELD = (By.ID, 'edit-geolocation')
  TERMS_AND_AGREEMENTS_CHECKBOX = (By.XPATH, '//input[@name="code_of_conduct"]')
  REGISTER_BUTTON = (By.XPATH, '//input[@value="Register"]')
  REGISTERING_BUTTON = (By.XPATH, '//input[@value="Registering..."]')
  USERNAME_FIELD_REQUIRED_WARNING = (By.XPATH, '//div[@id="edit-username-wrapper"]//div[@class="l-card-hint"]')
  EMAIL_FIELD_REQUIRED_WARNING = (By.XPATH, '//div[@id="edit-mail-wrapper"]//div[@class="l-card-hint"]')
  PASSWORD_FIELD_REQUIRED_WARNING = (By.XPATH, '//div[@id="edit-password-wrapper"]//div[@class="l-card-hint"]')
  CODE_OF_CONDUCT_REQUIRED_WARNING = (By.XPATH, '//div[@id="edit-code-of-conduct-wrapper"]//div[@class="l-card-hint"]')
  EMAIL_VERIFICATION_LABEL = (By.XPATH, '//h1[text()="Email Verification"]')
  ENTER_CODE_INPUT_FIELD = (By.ID, 'edit-code')
  VERIFY_BUTTON = (By.ID, 'edit-submit-button')
  EMAIL_LABEL_FIELD = (By.ID, 'user-email')
  SIGNUP_BUTTON = (By.XPATH, '//button[text()="Sign Up"]')
  SCROLL_PAGE_TO_VIEW_ELEMENT = "arguments[0].scrollIntoView();"
  USERNAME_ALREADY_TAKEN_MESSAGE = (By.XPATH, '//div[text()="Username is already taken."]')
  EMAIL_ALREADY_TAKEN_MESSAGE = (By.XPATH, '//div[text()="Email already taken"]')


