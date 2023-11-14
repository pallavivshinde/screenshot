import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

class Test_010_rightclick3():
    def test_010_right_click3(self):

        driver = webdriver.Chrome()

        driver.implicitly_wait(5)

        driver.maximize_window()

        driver.get("https://demo.guru99.com/test/simple_context_menu.html")

        right_click = driver.find_element(By.XPATH,"//span[text()='right click me']")

        action = ActionChains(driver)

        action.context_click(right_click).perform()

        driver.save_screenshot(
            "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_010_MouseRightClick3_guru.png")

        driver.find_element(By.XPATH, '//span[text()="Edit"]').click()

        alerttext=Alert(driver).text
        print('\n*********TEXT AFTER RIGHT CLICK*********')
        print(alerttext)

        Alert(driver).accept()

        driver.close()





