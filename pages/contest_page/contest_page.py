from pages.contest_page.contest_page_locators import ContestPageLocators
from pages.base_page.base_page import BasePage

class ContestPage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(self.driver)

  def click_complete_button(self):
    self.click_webelement(ContestPageLocators.COMPETE_NAVIGATION_ITEM)
    self.wait_until_element_should_be_visible(ContestPageLocators.ONGOING_CONTEST_LABEL, 10)
    self.wait_until_element_should_be_visible(ContestPageLocators.SHOW_ALL_CONTEST_SWTCH, 10)

  def verify_default_contest_list(self):
    self.wait_until_element_should_be_visible(ContestPageLocators.NO_CONTESTS_AVAILABLE_LABEL_IN_ONGOING_CONTEST, 10)

  def click_show_all_contests_switch(self):
    self.click_webelement(ContestPageLocators.SHOW_ALL_CONTEST_SWTCH)
    self.wait_until_element_should_not_be_visible(ContestPageLocators.NO_CONTESTS_AVAILABLE_LABEL_IN_ONGOING_CONTEST, 10)

  def verify_ongoing_contest_list(self):
    self.wait_until_element_should_be_visible(ContestPageLocators.OPC_CONTEST_CODE, 10)