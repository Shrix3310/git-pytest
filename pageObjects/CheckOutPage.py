class CheckOut:
    def __init__(self, driver, product):
        self.driver = driver
        self.product = product

    def getproducts(self):
        return self.driver.find_elements_by_xpath("//div[@class='card h-100']")

    def getproduct(self):
        return self.product.find_element_by_xpath("div/h4/a")

    def getproductname(self):
        return self.product.find_element_by_xpath("div/button")

    def getcheckout(self):
        return self.driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li/a")

    def getclickcheckout(self):
        return self.driver.find_element_by_xpath("/html/body/app-root/app-shop/div/div/div/table/tbody/tr[3]/td[5]/button")