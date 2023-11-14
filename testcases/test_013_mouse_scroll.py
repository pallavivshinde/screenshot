from selenium import webdriver

class Test_013_mouse_scroll():
    def test_013_mouse_scroll(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://www.bbc.com/news")

        driver.save_screenshot(
            "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_013_beforescrollby_pass.png")

        driver.execute_script("window.scrollBy(0,1000)")

        driver.save_screenshot(
            "C:\\Users\\lenovo\\PycharmProjects\\REVISION\\screenshot\\test_013_afterscrollby_pass.png")

        driver.close()
