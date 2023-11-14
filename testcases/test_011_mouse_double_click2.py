import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Test_011_mouse_double_click2():
    def test_011_doubleclick2(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://demoqa.com/buttons")

        double_click = driver.find_element(By.XPATH,'//button[@id="doubleClickBtn"]')

        action = ActionChains(driver)

        action.double_click(double_click).perform()

        driver.save_screenshot(
            "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_011_doubleclick2.png")


        text = driver.find_element(By.XPATH,"//p[@id='doubleClickMessage']").text

        print("\n ******* TEXT AFTER DOUBLE CLICK ********")
        print(text)

        driver.close()