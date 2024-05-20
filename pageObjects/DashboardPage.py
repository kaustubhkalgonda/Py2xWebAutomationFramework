from selenium import webdriver
from selenium.webdriver.common.by import By


class DashboardPage:
    link_customers_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customersList_xpath="//a[@href='/Admin/Customer/List']//p"

    def __init__(self,driver):
        self.driver = driver

    def clickCustomersLink(self):
        self.driver.find_element(By.XPATH,self.link_customers_xpath).click()

    def clickCustomersListLink(self):
        self.driver.find_element(By.XPATH, self.link_customersList_xpath).click()

