import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test_008_FBdropDown():
    def test_008_fb(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(10)

        driver.get("https://www.facebook.com/")

        driver.find_element(By.XPATH, '//a[@rel="async"]').click() ;
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys("hyung")
        time.sleep(2)

        driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys("kimung")
        time.sleep(2)

        driver.find_element(By.XPATH,'//input[@name="reg_email__"]').send_keys("kimtae3095@gmail.com")
        time.sleep(2)

        driver.find_element(By.XPATH,'//input[@id="password_step_input"]').send_keys("12345678")

        day = Select(driver.find_element(By.XPATH,'//select[@id="day"]'))
        day.select_by_value("30")
        time.sleep(2)

        Select(driver.find_element(By.XPATH,'//select[@id="month"]')).select_by_visible_text("Dec")
        time.sleep(2)

        Select(driver.find_element(By.XPATH,'//select[@id="year"]')).select_by_value("1995")

        driver.find_element(By.XPATH,"//input[@value='2']").click()
        time.sleep(2)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_008_FBdrpdwn.pass.png")

        driver.close()






