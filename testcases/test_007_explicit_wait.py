import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_007_explicitWait ():
    def test_007_explicit(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.get("https://www.google.com")

        driver.find_element(By.XPATH, '//textarea[@jsname="yZiJbe"]').send_keys("the internet speed test")

        driver.find_element(By.XPATH ,'(//input[@class="gNO89b"])[1]').click()

        driver.find_element(By.XPATH ,"//div[text()='RUN SPEED TEST']").click()

        try:
            wait = WebDriverWait(driver, 30, poll_frequency=0.5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[text()="TEST AGAIN"]')))

            time.sleep(5)

            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_007_SS.pass.png")

            download = driver.find_element(By.XPATH,'//p[@jsname="Lk0VKd"]').text

            print("\n****** Download Speed In Mbps ******")

            print(download + 'Mbps')

            upload = driver.find_element(By.XPATH,'//p[@jsname="dSdcdd"]').text

            print("\n ******* Upload Speed In Mbps *******")

            print(upload + "Mbps")

            driver.close()

            assert True

        except:

            print("\n Some Error Occured..........!")

            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_007_SS.fail.png")

            driver.close()
            assert False
