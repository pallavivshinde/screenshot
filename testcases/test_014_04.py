import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_014_04_div():
    def test_014_04(self):
        a=10
        b=2
        div=a/b
        if(div == 5):
            print("\n***** division is done *****")
            print("result= ",div)
            assert True

        else:
            print("\n ***** invalid operation *****")
            assert False

    def test_014_02_basic_details(self):

        driver = webdriver.Chrome()

        driver.implicitly_wait(5)

        driver.maximize_window()

        driver.get("https://magento.softwaretestingboard.com/")

        driver.find_element(By.XPATH,'//a[@title="Fusion Backpack"]').click()
        time.sleep(3)

        if(driver.title == "Fusion Backpack"):

         driver.save_screenshot(
            "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_014_04.pass.png")

         text1 = driver.find_element(By.XPATH, '(//div[@class="value"])[2]').text
         print('\n*********PRODUCT DESCRIPTION********')
         print(text1)

         driver.close()
         assert True;

        else:

            driver.save_screenshot(
                "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_014_04.fail.png")

            print('\n*********SORRY, NOT ABLE TO PROCESS OUR REQUEST**********')
            driver.close()

            assert False;







