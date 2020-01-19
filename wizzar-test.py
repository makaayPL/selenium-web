import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys

class WsbPlSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def testSearchTesterPhrase(self):
        # go to Wizzair
        self.driver.get("https://wizzair.com/pl-pl#/")
        # wait for menu
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,"navigation__item")))
        # click sign in
        signin = self.driver.find_element_by_xpath("//button[@data-test='navigation-menu-signin']")
        signin.click()

        # wait for modal
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//h2[@data-test='modal-title' and contains(text(), 'Zaloguj się')]")))
        # click sign in
        registration = self.driver.find_element_by_xpath("//button[@class='content__link1' and contains(text(),'Rejestracja')]")
        registration.click()

        # wait for modal
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//h2[@data-test='modal-title' and contains(text(), 'Zarejestruj się')]")))
        # add first name
        self.driver.find_element_by_xpath("//input[@data-test='registrationmodal-first-name-input']").send_keys("Marcin")
        # add last name
        self.driver.find_element_by_xpath("//input[@data-test='registrationmodal-last-name-input']").send_keys("Test")

        # click on modal title
        modalTitle = self.driver.find_element_by_xpath("//h2[@data-test='modal-title' and contains(text(), 'Zarejestruj się')]")
        modalTitle.click()

        # select gender
        gender = self.driver.find_element_by_xpath("//span[@class= 'rf-switch__label__inner' and contains(text(), 'Mężczyzna')]")
        gender.click()

        # select country code
        countryCode = self.driver.find_element_by_xpath("//div[@class='phone-number__calling-code-selector__empty']")
        countryCode.click()
        addCountryCode = self.driver.find_element_by_xpath("//input[@name='phone-number-country-code']").send_keys("Polska")
        elementForCountry = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='phone-number__calling-code-selector__dropdown__item__country' and contains(text(), 'Polska')]")))
        elementForCountry.click()

        # add phone number
        self.driver.find_element_by_xpath("//input[@data-test='check-in-step-contact-phone-number']").send_keys("123456789")

        # add address mail
        self.driver.find_element_by_xpath("//input[@data-test='booking-register-email']").send_keys("marcinTester12@test.pl")

        # add password
        # self.driver.find_element_by_xpath("//input[@data-test='booking-register-password']").send_keys("marcinTester123")

        # add citizenship
        self.driver.find_element_by_xpath("//input[@data-test='booking-register-country']").send_keys("Polska")
        self.driver.find_element_by_xpath("//label[@class='register-form__country-container__location' and contains(., 'Polska')]").click()

        # privacy policy
        self.driver.find_element_by_xpath("//label[@data-test='registration-privacy-policy-checkbox']").click()

        # register button
        self.driver.find_element_by_xpath("//button[@data-test='booking-register-submit']").click()

        # Wyszukuję wszystkie błędy
        errors_notices = self.driver.find_elements_by_xpath('//div[@class="rf-input__error" and not(contains(@style, "display: none;"))]')
        # Zapisuję widoczne błędy do listy visible_error_notices
        visible_error_notices = []
        for error in errors_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        # Sprawdzam, czy widoczny jest tylko jeden błąd
        assert len(visible_error_notices) == 1
        # Sprawdzam treść widocznego błędu
        print(visible_error_notices[0].get_attribute("innerText"))

        #
        # # Sprawdzam, czy widoczny jest tylko jeden błąd
        # assert len(visible_error_notices) == 1
        # # Sprawdzam treść widocznego błędu
        # error_text = visible_error_notices[0].get_attribute("innerText")
        # assert error_text == "Nieprawidłowy adres e-mail"



# uruchom test jesli uruchamiamy ten plik
if __name__ == "__main__":
    unittest.main()
