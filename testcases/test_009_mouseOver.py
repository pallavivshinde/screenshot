import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Test_009_MouseAction():
    def test_009_MouseOver(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.get("https://www.google.co.in/")

        driver.find_element(By.XPATH,'//textarea[@title="Search"]').send_keys("vtiger")

        driver.find_element(By.XPATH,'(//input[@value="Google Search"])[2]').click()

        driver.find_element(By.XPATH,"(//h3[contains(text(),'CRM Software: Customer Relationship Management | V')])[1]").click()
        time.sleep(5)

        action1 = ActionChains(driver)
        resource = driver.find_element(By.XPATH,"//a[contains(text(),'Resources')]")

        action1.move_to_element(resource).perform()

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_009_MouseOver.pass.png")

        driver.find_element(By.XPATH,"(//a[@class='list-link'][normalize-space()='Contact Us'])[1]").click()

        message = driver.find_element(By.XPATH, "(//div[@class='text-reset text-decoration-none'])[2]").text

        print("\n ******* CONTACT NUMBER *********")
        print(message)

        driver.close()

