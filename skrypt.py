from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import Select
import random
import string

class WsbPlCheck(unittest.TestCase):

    # przed kazdym testem
    def setUp(self):
        self.driver = webdriver.Chrome()
        sleep(3)

    # po kazdym tescie
    def tearDown(self):
        self.driver.quit()

    # # test automationpractice.com
    # def testRegistartionForAutomationPractice(self):
    #     # go to the automation practice page
    #     self.driver.get("http://automationpractice.com")
    #     sleep(3)
    #     # click on Sign in
    #     self.driver.find_element_by_class_name("login").click()
    #     sleep(3)
    #
    #     # generate unique email address
    #     mail = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + "@elo.pl"
    #     # add address email
    #     self.driver.find_element_by_id("email_create").send_keys(mail)
    #     sleep(1)
    #     # clcik on Create account
    #     self.driver.find_element_by_id("SubmitCreate").click()
    #     sleep(5)
    #
    #     # FORM
    #     # select Mr. from title
    #     self.driver.find_element_by_id("id_gender1").click()
    #     sleep(1)
    #
    #     # add First name
    #     self.driver.find_element_by_id("customer_firstname").send_keys("Jan")
    #     sleep(2)
    #     self.driver.find_elements_by_xpath("//label[@for='customer_firstname']//parent::div[@class='required form-group form-ok']")
    #     # assertion => check that the first name value was added to field
    #     firstname = self.driver.find_element_by_id("customer_firstname").get_attribute("value")
    #     assert firstname == "Jan"
    #
    #     # add Last name
    #     self.driver.find_element_by_id("customer_lastname").send_keys("Kowalski")
    #     sleep(2)
    #     self.driver.find_elements_by_xpath("//label[@for='customer_lastname']//parent::div[@class='required form-group form-ok']")
    #
    #     # add Password
    #     self.driver.find_element_by_id("passwd").send_keys("admin123")
    #     sleep(2)
    #     self.driver.find_elements_by_xpath("//label[@for='passwd']//parent::div[@class='required form-group form-ok']")
    #
    #     # add Date of Birth
    #     Select(self.driver.find_element_by_id('days')).select_by_visible_text("20  ")
    #     Select(self.driver.find_element_by_id('months')).select_by_visible_text("May ")
    #     Select(self.driver.find_element_by_id('years')).select_by_visible_text("1990  ")
    #
    #     # add First Name
    #     self.driver.find_element_by_id("firstname").send_keys("Jan")
    #     sleep(1)
    #
    #     # add Last Name
    #     self.driver.find_element_by_id("lastname").send_keys("Kowalski")
    #     sleep(1)
    #
    #     # add Company
    #     self.driver.find_element_by_id("company").send_keys("Microsoft")
    #     sleep(1)
    #
    #     # add Address
    #     self.driver.find_element_by_id("address1").send_keys("ul. Legnicka")
    #     sleep(1)
    #
    #     # add City
    #     self.driver.find_element_by_id("city").send_keys("Wroclaw")
    #     sleep(1)
    #
    #     # add State
    #     Select(self.driver.find_element_by_id('id_state')).select_by_visible_text("Texas")
    #
    #     # add Postcode
    #     self.driver.find_element_by_id("postcode").send_keys("00000")
    #     sleep(1)
    #
    #     # add Country
    #     Select(self.driver.find_element_by_id('id_country')).select_by_visible_text("United States")
    #
    #     # add Mobilne Phone
    #     self.driver.find_element_by_id("phone_mobile").send_keys("123456789")
    #     sleep(1)
    #
    #     # add Assign an address alias for future reference.
    #     self.driver.find_element_by_id("alias").send_keys("London")
    #     sleep(1)
    #
    #     # select Mr. from title
    #     self.driver.find_element_by_id("submitAccount").click()
    #     sleep(3)
    #
    #     # correct registartion
    #     self.driver.find_elements_by_xpath("//p[@class='info-account' and contains(., 'Welcome to your account. Here you can manage all of your personal information and orders.')]")

    # test automationpractice.com (empyty first name)
    def testTryToRegistartionForAutomationPractice(self):
        # go to the automation practice page
        self.driver.get("http://automationpractice.com")
        sleep(3)
        # click on Sign in
        self.driver.find_element_by_class_name("login").click()
        sleep(3)

        # generate unique email address
        mail = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + "@elo.pl"
        # add address email
        self.driver.find_element_by_id("email_create").send_keys(mail)
        sleep(1)
        # clcik on Create account
        self.driver.find_element_by_id("SubmitCreate").click()
        sleep(5)

        # FORM
        # select Mr. from title
        self.driver.find_element_by_id("id_gender1").click()
        sleep(1)

        # NOT add First name

        # add Last name
        self.driver.find_element_by_id("customer_lastname").send_keys("Kowalski")
        sleep(2)
        self.driver.find_elements_by_xpath("//label[@for='customer_lastname']//parent::div[@class='required form-group form-ok']")

        # add Password
        self.driver.find_element_by_id("passwd").send_keys("admin123")
        sleep(2)
        self.driver.find_elements_by_xpath("//label[@for='passwd']//parent::div[@class='required form-group form-ok']")

        # add Date of Birth
        Select(self.driver.find_element_by_id('days')).select_by_visible_text("20  ")
        Select(self.driver.find_element_by_id('months')).select_by_visible_text("May ")
        Select(self.driver.find_element_by_id('years')).select_by_visible_text("1990  ")

        # add First Name
        self.driver.find_element_by_id("firstname").send_keys("Jan")
        sleep(1)

        # add Last Name
        self.driver.find_element_by_id("lastname").send_keys("Kowalski")
        sleep(1)

        # add Company
        self.driver.find_element_by_id("company").send_keys("Microsoft")
        sleep(1)

        # add Address
        self.driver.find_element_by_id("address1").send_keys("ul. Legnicka")
        sleep(1)

        # add City
        self.driver.find_element_by_id("city").send_keys("Wroclaw")
        sleep(1)

        # add State
        Select(self.driver.find_element_by_id('id_state')).select_by_visible_text("Texas")

        # add Postcode
        self.driver.find_element_by_id("postcode").send_keys("00000")
        sleep(1)

        # add Country
        Select(self.driver.find_element_by_id('id_country')).select_by_visible_text("United States")

        # add Mobilne Phone
        self.driver.find_element_by_id("phone_mobile").send_keys("123456789")
        sleep(1)

        # add Assign an address alias for future reference.
        self.driver.find_element_by_id("alias").send_keys("London")
        sleep(1)

        # select Mr. from title
        self.driver.find_element_by_id("submitAccount").click()
        sleep(3)

        # NOT correct registartion
        errorMessage = self.driver.find_elements_by_xpath("//div[@class='alert alert-danger']//p[contains(., 'There is 1 error')]")
        assert errorMessage[0].is_displayed()

        errorMessageContent = self.driver.find_elements_by_xpath("//div[@class='alert alert-danger']//li[contains(.,'firstname is required')]")
        assert errorMessageContent[0].is_displayed()
# uruchom test jesli uruchamiamy ten plik
if __name__ == "__main__":
    unittest.main()
