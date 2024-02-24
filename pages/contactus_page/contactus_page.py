from pages.base_page.base_page import BasePage
from pages.contactus_page.contactus_page_locators import ContactusPageLocators

class ContactusPage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(self.driver)

  def verify_all_contact_information_visible(self):
    self.wait_until_element_should_be_visible(ContactusPageLocators.HELP_EMAIL, 10)
    self.wait_until_element_should_be_visible(ContactusPageLocators.PHONE_NUMBER, 10)
    self.wait_until_element_should_be_visible(ContactusPageLocators.COLLEGE_EMAIL, 10)
    self.wait_until_element_should_be_visible(ContactusPageLocators.CONTESTS_EMAIL,10)
    self.wait_until_element_should_be_visible(ContactusPageLocators.PROBLEMS_EMAIL, 10)
    