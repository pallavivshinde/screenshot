import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test_008_drop_down():
    def test_008_dd(self):

        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()

        driver.get("https://www.careinsurance.com/rhicl/proposalcp/renew/index-care")

        driver.find_element(By.XPATH,'//input[@id="policynumber"]').send_keys("12347777")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@id="dob"]').click()

        month = Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]'))
        month.select_by_visible_text("Dec")
        time.sleep(5)

        year = Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-year"]'))
        year.select_by_value("1999")
        time.sleep(5)

        driver.find_element(By.XPATH,'//a[text()="4"]').click()

        driver.find_element(By.XPATH,'//input[@id="alternative_number"]').send_keys("7758980000")

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_008_dropDown.pass.png")

        driver.close()








