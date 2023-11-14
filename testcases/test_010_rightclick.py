import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

class Test_010_right_click():
    def test_010_rightclick(self):

        driver = webdriver.Chrome()

        driver.implicitly_wait(5)

        driver.maximize_window()

        driver.get("https://nxtgenaiacademy.com/mouseevent/")

        action = ActionChains(driver)

        rightclick = driver.find_element(By.XPATH,"//button[@id='rightclick']")

        action.context_click(rightclick).perform()

        driver.save_screenshot(
            "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_010_MouseRightClick2.pass.png")

        driver.find_element(By.XPATH,"//a[text()='Alert Popup']").click()

        driver.find_element(By.XPATH,"//button[@name='alertbox']").click()

        alter = Alert(driver).text

        print("\n****** MESSAGE AFTER RIGHT CLICK *****")
        print(alter)
        Alert(driver).accept()

        driver.close()

