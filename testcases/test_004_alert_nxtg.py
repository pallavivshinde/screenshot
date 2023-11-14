import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class Test_004_alert():
    def test_004_alert_nxtg(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.get("https://nxtgenaiacademy.com/alertandpopup/")

        driver.find_element(By.XPATH,"//button[@name='alertbox']").click()
        time.sleep(3)

        mesg1 = Alert(driver).text
        print("\n Alert Message = ",mesg1)
        Alert(driver).accept()
        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_003_alert.pass.png")

        driver.close()

    def test_004_confirm_alert(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.get("https://nxtgenaiacademy.com/alertandpopup/")

        driver.find_element(By.XPATH,"//button[@name='confirmalertbox']").click()
        time.sleep(3)

        mesg2 = Alert(driver).text

        print("\n Alert_Confirmation_message = ",mesg2)

        Alert(driver).accept()
        time.sleep(3)

        driver.close()

    def test_prompt_alert(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(3)

        driver.get("https://nxtgenaiacademy.com/alertandpopup/")

        driver.find_element(By.XPATH,"//button[@name='promptalertbox1234']").click()
        time.sleep(3)

        mesg3 = Alert(driver).text

        print("\n Alert Prompt Message = ",mesg3)
        time.sleep(3)

        Alert(driver).send_keys("Hello Pallavi...!")

        Alert(driver).accept()

        prompt = driver.find_element(By.XPATH,"//p[@id='demoone']").text

        print("prompt inserted text=",prompt)
        time.sleep(3)

        # alert = Alert(driver)
        # alert.send_keys("heelo")
        # alert_text = alert.text
        # alert.accept()
        # print("\n ALERT TEXT",alert_text)
        driver.close()






