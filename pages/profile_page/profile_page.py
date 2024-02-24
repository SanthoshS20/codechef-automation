from pages.profile_page.profile_page_locators import ProfilePageLocators
from pages.base_page.base_page import BasePage

class ProfilePage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(self.driver)

  def click_edit_profile_button(self):
    self.click_webelement(ProfilePageLocators.EDIT_PROFILE_BUTTON)
    #self.wait_until_element_should_be_visible(ProfilePageLocators.LOGIN_INFORMATION_LABEL, 10)

  def click_general_Tab(self):
    self.click_webelement(ProfilePageLocators.GENERAL_TAB)
    self.wait_until_element_should_be_visible(ProfilePageLocators.NAME_FIELD, 10)
    self.wait_until_element_should_be_visible(ProfilePageLocators.SAVE_BUTTON, 10)

  def get_name_attribute_value(self):
    return self.get_element_attribute_value(ProfilePageLocators.NAME_FIELD, "value")

  def update_name(self, name):
    self.clear_text(ProfilePageLocators.NAME_FIELD)
    self.send_text(ProfilePageLocators.NAME_FIELD, name)

  def click_save_button_in_general_tab(self):
    self.click_webelement(ProfilePageLocators.SAVE_BUTTON)
    self.wait_until_element_should_be_visible(ProfilePageLocators.GENERAL_INFORMATION_UPDATE_SUCCESS_MESSAGE, 10)

  def update_email(self, email):
    self.clear_text(ProfilePageLocators.EMAIL_ID_FIELD)
    self.send_text(ProfilePageLocators.EMAIL_ID_FIELD, email)
    
  def click_save_button_in_personal_tab(self):
    self.click_webelement(ProfilePageLocators.PERSONAL_TAB_SAVE_BUTTON)
    self.wait_until_element_should_be_visible(ProfilePageLocators.PERSONAL_INFORMATION_UPDATE_SUCCESS_MESSAGE, 10)

  def close_success_popup(self):
    self.click_webelement(ProfilePageLocators.CLOSE_POPUP_BUTTON)
    self.wait_until_element_should_not_be_visible(ProfilePageLocators.PERSONAL_INFORMATION_UPDATE_SUCCESS_MESSAGE, 10)

  def click_login_tab(self):
    self.click_webelement(ProfilePageLocators.LOGIN_TAB)

  def update_password(self, old_password, new_password):
    self.send_text(ProfilePageLocators.CURRENT_PASSWORD_FIELD, old_password)
    self.send_text(ProfilePageLocators.NEW_PASSWORD_FIELD, new_password)
    self.send_text(ProfilePageLocators.CONFIRM_PASSWORD_FIELD, new_password)

  def click_update_password_button(self):
    self.click_webelement(ProfilePageLocators.UPDATE_PASSWORD_BUTTON)

  def click_personal_tab(self):
    self.click_webelement(ProfilePageLocators.PERSONAL_TAB)
    self.wait_until_element_should_be_visible(ProfilePageLocators.EMAIL_ID_FIELD, 10)

  def get_email_attribute_value(self):
    return self.get_element_attribute_value(ProfilePageLocators.EMAIL_ID_FIELD,"value")