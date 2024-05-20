from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerPage:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_firstname_id = "FirstName"
    textbox_lastname_id = "LastName"
    radiobox_genderMale_id = "Gender_Male"
    radiobox_genderFemale_id = "Gender_Female"
    textbox_dateofbirth_id = "DateOfBirth"
    textbox_companyname_id = "Company"
    checkbox_taxexempt_id = "IsTaxExempt"
    dropdown_newsletter_xpath = "//select[@id='SelectedNewsletterSubscriptionStoreIds']"
    dropdown_customerroles_xpath = "//select[@id='SelectedCustomerRoleIds']"
    dropdown_managerofvendors_xpath = "//select[@id='VendorId']"
    checkbox_active_id = "Active"
    textbox_adminComment_id = "AdminComment"
    button_save_name="save"
    alert_success_xpath="//div[contains(@class,'alert-success')]"

    def __init__(self, driver):
        self.driver = driver

    def enterEmail(self, emailId):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(emailId)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def enterFirstName(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)

    def enterLastName(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def clickGenderMaleRadiobox(self):
        self.driver.find_element(By.ID, self.radiobox_genderMale_id).click()

    def clickGenderFemaleRadiobox(self):
        self.driver.find_element(By.ID, self.radiobox_genderFemale_id).click()

    def enterDateOfBirth(self, dateOfBirth):
        self.driver.find_element(By.ID, self.textbox_dateofbirth_id).send_keys(dateOfBirth)

    def enterCompanyName(self, companyName):
        self.driver.find_element(By.ID, self.textbox_companyname_id).send_keys(companyName)

    def clickTaxExemptCheckbox(self):
        self.driver.find_element(By.ID, self.checkbox_taxexempt_id).click()

    def selectNewsletter(self, newsletter):
        select = Select(self.driver.find_element(By.XPATH,self.dropdown_newsletter_xpath))
        select.select_by_value(newsletter)

    def selectCustomerRoles(self, customerRole):
        select = Select(self.driver.find_element(By.XPATH,self.dropdown_customerroles_xpath))
        select.select_by_visible_text(customerRole)

    def selectManagerOfVendors(self, managerOfVendors):
        select = Select(self.driver.find_element(By.XPATH,self.dropdown_managerofvendors_xpath))
        select.select_by_value(managerOfVendors)

    def clickActiveCheckbox(self):
        self.driver.find_element(By.ID, self.checkbox_active_id).click()

    def enterAdminComment(self, adminComment):
        self.driver.find_element(By.ID, self.textbox_adminComment_id).send_keys(adminComment)

    def clickSaveButton(self):
        self.driver.find_element(By.NAME, self.button_save_name).click()