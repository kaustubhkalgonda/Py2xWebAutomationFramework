import os
import random
import string

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


class Test_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def generate_random_name(self):
        random_name = ''.join(random.choices(string.ascii_lowercase +
                                             string.digits, k=8))
        return random_name

    @allure.title("Verify Add Customer")
    @allure.testcase("TC003")
    @allure.tag("Smoke")
    def test_addCustomer(self, setup):
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
                EC.presence_of_element_located((By.XPATH, self.clp.btn_addNew_xpath)))
            self.clp.clickAddNewButtton()
            self.logger.info("****** navigating to add customer page ******")
            self.acp = AddCustomerPage(self.driver)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.acp.textbox_email_id)))
            self.acp.enterEmail(self.generate_random_name() + "@test.com")
            self.acp.enterPassword("Admin12")
            self.acp.enterFirstName("tom")
            self.acp.enterLastName("moody")
            self.acp.clickGenderMaleRadiobox()
            self.acp.enterDateOfBirth("06/20/1980")
            self.acp.enterCompanyName("youtube")
            self.acp.clickTaxExemptCheckbox()
            self.acp.selectNewsletter("1")
            self.acp.selectCustomerRoles("Vendors")
            self.acp.selectManagerOfVendors("2")
            self.acp.clickActiveCheckbox()
            self.acp.enterAdminComment("This is test admin comment.")
            self.acp.clickSaveButton()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.acp.alert_success_xpath)))
            assert self.driver.find_element(By.XPATH, self.acp.alert_success_xpath).is_displayed()
            self.logger.info("****** customer added successfully. ******")
            self.driver.quit()
        except AssertionError:
            allure.attach(self.driver.get_screenshot_as_png(), name='Customer not added',
                          attachment_type=AttachmentType.PNG)
            self.logger.error("****** Add Customer test failed ******")
            self.driver.quit()
            assert False
