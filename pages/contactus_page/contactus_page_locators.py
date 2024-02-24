from pages.base_page.base_page_locators import  BasePageLocators
from selenium.webdriver.common.by import By

class ContactusPageLocators(BasePageLocators):

  HELP_EMAIL = (By.LINK_TEXT, 'help@codechef.com')
  PROBLEMS_EMAIL= (By.LINK_TEXT, 'problems@codechef.com')
  PHONE_NUMBER = (By.XPATH, '//p[text()="+91 98212 99918"]')
  CONTESTS_EMAIL = (By.LINK_TEXT, 'contests@codechef.com')
  COLLEGE_EMAIL = (By.LINK_TEXT, 'colleges@codechef.com')
  CONTACTUS_LABEL = (By.XPATH, '//h2[text()="Contact us"]')