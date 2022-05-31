class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        return self.driver.find_element_by_xpath("/html/body/app-root/app-navbar/div/nav/ul/li[2]/a")
