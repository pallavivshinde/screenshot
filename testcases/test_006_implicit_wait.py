import time

from selenium.webdriver.common.by import By
from selenium import webdriver


class Test_006_implicitWait():
    def test_006_implicitWait(self):

        driver = webdriver.Chrome()

        driver.implicitly_wait(40)

        driver.maximize_window()

        driver.get("https://www.google.com")
        time.sleep(3)

        driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("My Internet speed")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@value="Google Search"][1]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,"//div[text()='RUN SPEED TEST']").click()

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_006_implicitWait.png")
        time.sleep(40)

        mesg1 = driver.find_element(By.XPATH,'//p[@jsname="Lk0VKd"]').text
        print("\n ****** SPEED Mbps Download *********** ")
        # print(mesg1 +'MBPS')
        print(mesg1 + 'MBPS')
        time.sleep(15)

        mesg2 = driver.find_element(By.XPATH,'//p[@jsname="dSdcdd"]').text
        print("\n********* SPEED Mbps Upload ******")
        print(mesg1 + 'MBPS')
        time.sleep(15)

        driver.close()

