import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class WsbPlSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def testSearchTesterPhrase(self):
        # go to the google
        self.driver.get("https://google.com")

        query = self.driver.find_element_by_name("q")
        query.send_keys("tester")
        query.submit()

        results = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"g")))

        for result in results:
            print(result.text + "\n") 

    def tearDown(self):
        self.driver.quit()

# uruchom test jesli uruchamiamy ten plik
if __name__ == "__main__":
    unittest.main()
