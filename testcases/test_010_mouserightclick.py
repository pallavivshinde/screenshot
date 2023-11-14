import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Test_010_mouse_right_click():
    def test_010_right_click(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://nxtgenaiacademy.com/mouseevent/")
        time.sleep(3)

        action = ActionChains(driver)

        rightclickme = driver.find_element(By.XPATH,"//button[normalize-space()='Right Click Me']")
        time.sleep(3)

        action.context_click(rightclickme).perform()
        time.sleep(3)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_010_MouseRightClick.pass.png")

        driver.find_element(By.XPATH,"//a[text()='Registration Form']").click()

        message = driver.find_element(By.XPATH,'//h3[text()="Register For Demo"]').text

        print("\n **** TEXT AFTER RIGHT CLICK *******")

        print(message)

        driver.close()