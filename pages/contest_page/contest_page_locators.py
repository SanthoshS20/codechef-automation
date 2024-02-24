from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class ContestPageLocators(BasePageLocators):
  COMPETE_NAVIGATION_ITEM = (By.XPATH, '//div[@class="_headerRightContainer_1v77f_4314"]//parent::a[@href="/contests"]')
  ONGOING_CONTEST_LABEL = (By.XPATH, '//p[text()="Ongoing Contests"]')
  SHOW_ALL_CONTEST_SWTCH = (By.XPATH, '//span[@class="MuiIconButton-label"]')
  OPC_CONTEST_CODE = (By.XPATH, '//p[text()="IARCSJUD"]')
  NO_CONTESTS_AVAILABLE_LABEL_IN_ONGOING_CONTEST = (By.XPATH, '//p[text()="Ongoing Contests"]//ancestor::div[@class="_table__container_1c9os_331 _dark_1c9os_272"]//p[text()="No contests available"]')
