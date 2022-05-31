class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    def getcountryinput(self):
        return self.driver.find_element_by_xpath("//*[@id='country']")

    def getcountryname(self):
        return self.driver.find_element_by_link_text("India")

    def getcheckoutradio(self):
        return self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")

    def getsubmitbutton(self):
        return self.driver.find_element_by_css_selector("[type='submit']")

    def getsuccesstext(self):
        return self.driver.find_element_by_class_name("alert-success")