from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomersListPage:
    btn_addNew_xpath = "//a[@href='/Admin/Customer/Create']"
    textbox_email_id = "SearchEmail"
    textbox_firstname_id = "SearchFirstName"
    textbox_lastname_id = "SearchLastName"
    button_search_id = "search-customers"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']/tbody/tr"

    def __init__(self, driver):
        self.driver = driver

    def clickAddNewButtton(self):
        self.driver.find_element(By.XPATH, self.btn_addNew_xpath).click()

    def enterEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def enterFirstName(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)

    def enterLastName(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def clickSearchButton(self):
        self.driver.find_element(By.ID, self.button_search_id).click()

    def getNoOfRows(self):
       return len(self.driver.find_elements(By.XPATH, "//table[@id='customers-grid']/tbody/tr"))

    def findCustomerByEmail(self, email):
        result = False
        for i in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            email_text = table.find_element(By.XPATH,
                                               "//table[@id='customers-grid']/tbody/tr[" + str(i) + "]/td[2]").text
            if email_text == email:
                result = True
                break
        return result
