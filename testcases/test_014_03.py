import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_014_03_mul():
    def test_014_03(self):
        a=12
        b=9
        mul = a*b
        if(mul == 108):
            print("\n ***** multiplication is done *****")
            print("result=", mul)
            assert True

        else:
            print("\n ***** invalid operation *****")
            assert False

    def test_014_02(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.get("https://magento.softwaretestingboard.com/")

        driver.find_element(By.XPATH,"(//a[contains(text(),'Sign In')])[1]").click()

        driver.find_element(By.XPATH,'//input[@id="email"]').send_keys("shindepallavi506@gamil.com")

        driver.find_element(By.XPATH,'//input[@title="Password"]').send_keys("Pallu@123")

        driver.find_element(By.XPATH,'(//button[@type="submit"])[2]').click()

        driver.find_element(By.XPATH,"(//button[@class='action switch'])[1]").click()

        driver.find_element(By.XPATH,"(//a[normalize-space()='My Account'])[1]").click()

        if ( driver.title == "My Account" ) :

         driver.save_screenshot(
            "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_014_03.pass.png")

         print("\n ******* CONTACT INFORMATION ********")

         print(driver.find_element(By.XPATH,"(//p[contains(text(),'pallavi shinde')])[1]").text)

         text2 = driver.find_element(By.XPATH, '(//div[@class="box-content"])[2]').text
         print("\n**********ADDRESS INFORMATION********")
         print(text2)

         driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click()

         driver.find_element(By.XPATH, '(//a[contains(text(),"Sign Out")])[1]').click()

         driver.close()
         assert True

        else:
            driver.save_screenshot(
                "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_014_03.fail.png")

            print("**********SORRY......!, NOT ABLE TO PRINT ACCOUNT DETAILS")

            driver.close()

            assert False








