import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_014_02_sub():

    def test_014_02(self):

        a=22
        b=11
        sub = a-b

        if(sub == 11):
            print("\n ***** substraction is done ********")
            print("result =",sub)
            assert True

        else:
            print("\n ***** invalid operation *****")
            assert False

    def test_014_02_pr(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com/")

        driver.find_element(By.XPATH,"(//a[contains(text(),'Sign In')])[1]").click()

        driver.find_element(By.XPATH,'//input[@id="email"]').send_keys("shindepallavi506@gamil.com")

        driver.find_element(By.XPATH,'//input[@title="Password"]').send_keys("Pallu@123")

        driver.find_element(By.XPATH,"(//span[contains(text(),'Sign In')])[1]").click()

        # try:
        #     # driver.find_element(By.XPATH, '(//span[@class="logged-in"])[1]' )
        #
        #     driver.save_screenshot(
        #         "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_014_02.pass.png")
        #
        #     print("\n ******* LOGIN SUCESSFULL ********")
        #
        #     driver.find_element(By.XPATH,"div[class='panel header'] span[class='logged-in']").click()
        #
        #     driver.find_element(By.XPATH,"(//a[normalize-space()='Sign Out'])[1]").click()
        #
        #     driver.close()
        #
        #     assert True
        #
        # except:
        # #     driver.save_screenshot(
        # #         "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_014_02.fail.png")
        # #
        #     print('\n********LOGIN UNSUCCESSFUL********')
        # #
        # #     driver.close()
        # #
        #     assert False
        #

        try:
            driver.find_element(By.XPATH, '(//span[@class="logged-in"])[1]' ) ;

            driver.save_screenshot(
                    "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_014_02.pass.png")

            print("\n*********LOGIN SUCCESSFUL*******") ;

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click() ;

            driver.find_element(By.XPATH, '(//a[contains(text(),"Sign Out")])[1]').click() ;

            driver.close();

            assert True ;

        except:
            driver.save_screenshot(
                    "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_014_02.fail.png")

            print('\n********LOGIN UNSUCCESSFUL********') ;

            driver.close();

            assert False ;






