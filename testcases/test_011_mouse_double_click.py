import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Test_011_mouse_double_click():
    def test_011_doubleclick(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://nxtgenaiacademy.com/mouseevent/")

        double_click = driver.find_element(By.XPATH,'//button[@id="dblclick"]')

        action =ActionChains(driver)

        action.double_click(double_click).perform()

        driver.save_screenshot(
            "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_011_doubleclick.png")

        text = driver.find_element(By.XPATH,"//p[text()='Double Click Action is Performed']").text

        print('\n*********TEXT AFTER DOUBLE CLICK*********')
        print(text)

        driver.close()

