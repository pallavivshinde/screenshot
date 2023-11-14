import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_002_login():
    def test_002_lumalogin(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com/")

        driver.find_element(By.XPATH,"(//a[contains(text(),'Sign In')])[1]").click()

        driver.find_element(By.XPATH,"//input[@title='Email']").send_keys("shindepallavi506@gamil.com")

        driver.find_element(By.XPATH,"//input[@title='Password']").send_keys("Pallu@123")

        driver.find_element(By.XPATH,"//button[@class='action login primary']").click()

        try:
            driver.find_element(By.XPATH,"//a[@class='logo']//img")

            print("\n ***********LOGIN IS DONE *********")

            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_002_luma.pass.png")

            message1 = driver.find_element(By.XPATH, '//span[@class="logged-in"]').text
            print('\nTEXT=', message1)

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click()
            time.sleep(1)

            driver.find_element(By.XPATH, "(//a[contains(text(), 'Sign Out')])[1]").click()
            time.sleep(1)

            driver.close()

        except:
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_002_luma.fail.png")
            print("\n ********* LOGIN IS FAIL **********")

            time.sleep(5)

            driver.close()







