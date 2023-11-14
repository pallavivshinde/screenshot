import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_003_luma_details():
    def test_003_account_details(self):

        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(3)

        driver.find_element(By.XPATH,"(//a[contains(text(),'Sign In')])[1]").click()
        time.sleep(3)

        driver.find_element(By.XPATH,"//input[@title='Email']").send_keys("shindepallavi506@gamil.com")
        time.sleep(3)

        driver.find_element(By.XPATH,"//input[@title='Password']").send_keys("Pallu@123")
        time.sleep(3)

        driver.find_element(By.XPATH,"//button[@class='action login primary']").click()
        time.sleep(3)

        if(driver.title == "Home Page"):

            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_003_accountDetails.pass.png")

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click();

            driver.find_element(By.XPATH,"(//a[normalize-space()='My Account'])[1]").click()

            mesg1 = driver.find_element(By.XPATH,"//p[contains(text(),'pallavi shinde')]").text
            print("\n MyName =",mesg1 )

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click();

            driver.find_element(By.XPATH,"(//a[normalize-space()='Sign Out'])[1]").click()

            driver.close()

            assert True;

        else:
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_003_accountDetails.pass.png")

            driver.close()

            assert False;

