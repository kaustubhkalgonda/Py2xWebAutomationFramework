import os

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen

class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @allure.title("Verify Homepage title")
    @allure.testcase("TC001")
    @allure.tag("Smoke")
    def test_homePageTitle(self, setup):
        try:
            self.logger.info("****** Verifying Homepage title ******")
            self.driver = setup
            self.driver.get(self.baseURL)
            assert self.driver.title == "Your store. Login"
            self.logger.info("****** Homepage title test is passed ******")
            self.driver.quit()
        except AssertionError:
            allure.attach(self.driver.get_screenshot_as_png(), name='Incorrect Homepage',
                          attachment_type=AttachmentType.PNG)
            self.logger.error("****** Homepage title test is failed ******")
            self.driver.quit()
            assert False

    @allure.title("Verify Login functionality")
    @allure.testcase("TC002")
    @allure.tag("Smoke")
    def test_login(self, setup):
        try:
            self.logger.info("****** Verifying login test ******")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            assert self.driver.title == "Dashboard / nopCommerce administration"
            self.logger.info("****** Login test passed ******")
            self.driver.close()
        except AssertionError:
            allure.attach(self.driver.get_screenshot_as_png(), name='Incorrect Credentials',
                          attachment_type=AttachmentType.PNG)
            self.logger.error("****** Login test is failed ******")
            self.driver.close()
            assert False
