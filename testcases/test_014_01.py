from selenium import webdriver

class Test_014_add():
    def test_014_add1(self):
        a = 20
        b = 10
        addition = a + b

        if(addition == 30):
            print("\n addition sucessful")
            assert True

        else:
            print("\n addition failed")
            assert False

    def test_002(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()

        driver.get("https://magento.softwaretestingboard.com/?ref=hackernoon.com")

        if(driver.title=="Home Page"):
            print("\n ****** YOU ARE AT HOME PAGE *********")
            driver.save_screenshot(
                "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_011_doubleclick.png")

            driver.close()
            assert True

        else:
            driver.save_screenshot(
                "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_014_01.png")

            print("\n*********YOU ARE ENTERED IN WRONG URL******** ")
            driver.close()
            assert False





