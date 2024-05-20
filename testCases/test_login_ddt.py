import os

import allure
import openpyxl
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen
from utilities.readDataFromExcel import ReadExcel


class Test_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUsername()
    # password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    file_path = os.getcwd() + "/TestData/login_data.xlsx"

    @pytest.mark.parametrize("user_cred", ReadExcel.read_credentials_from_file(file_path=file_path))
    @allure.title("Verify Login functionality with data driven testing")
    @allure.testcase("TC003")
    @allure.tag("Smoke")
    def test_login_ddt(self, setup, user_cred):
        try:
            username = user_cred["username"]
            password = user_cred["password"]
            self.logger.info("****** Verifying login test ******")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp = LoginPage(self.driver)
            self.lp.setUserName(username)
            self.lp.setPassword(password)
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
