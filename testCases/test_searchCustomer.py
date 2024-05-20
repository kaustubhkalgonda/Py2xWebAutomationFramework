import os
import random
import string
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.CustomersListPage import CustomersListPage
from pageObjects.DashboardPage import DashboardPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen
from selenium.webdriver.support import expected_conditions as EC


class Test_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @allure.title("Verify Search Customer by Email")
    @allure.testcase("TC004")
    @allure.tag("Smoke")
    def test_searchCustomer(self, setup):
        try:
            self.logger.info("****** Verifying add customer test ******")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            self.logger.info("****** Login successful******")
            self.dp = DashboardPage(self.driver)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.dp.link_customers_xpath)))
            self.dp.clickCustomersLink()
            self.dp.clickCustomersListLink()
            self.logger.info("****** navigating to customers list page ******")
            self.clp = CustomersListPage(self.driver)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.clp.button_search_id)))
            self.clp.enterEmail("admin@yourStore.com")
            self.clp.clickSearchButton()
            time.sleep(3)
            assert self.clp.findCustomerByEmail("admin@yourStore.com")
            self.logger.info("****** customer found successfully. ******")
            self.driver.quit()
        except AssertionError:
            allure.attach(self.driver.get_screenshot_as_png(), name='Customer not found',
                          attachment_type=AttachmentType.PNG)
            self.logger.error("****** Find Customer by email test failed ******")
            self.driver.quit()
            assert False
