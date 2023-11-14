import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_001_lumareg():
    def test_001_luma_registration(self):

        # initialize the webdriver
        driver = webdriver.Chrome()
        time.sleep(3)

        driver.maximize_window()
        time.sleep(3)

        driver.get("https://magento.softwaretestingboard.com/?ref=hackernoon.com")
        time.sleep(5)

        driver.find_element(By.XPATH,"(//a[normalize-space()='Create an Account'])[1]").click()
        time.sleep(3)

        driver.find_element(By.XPATH,"//input[@id='firstname']").send_keys("pallavi")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@id="lastname"]').send_keys("shinde")
        time.sleep(3)

        driver.find_element(By.XPATH,"//input[@title='Email']").send_keys("shindepallavi506@gamil.com")
        time.sleep(3)

        driver.find_element(By.XPATH,"//input[@title='Password']").send_keys("Pallu@123")
        time.sleep(3)

        driver.find_element(By.XPATH,"//input[@title='Confirm Password']").send_keys("Pallu@123")
        time.sleep(3)

        driver.find_element(By.XPATH,"//button[@title='Create an Account']").click()
        time.sleep(3)

        driver.close()
