import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from pageObjects.CheckOutPage import CheckOut
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage


class TestProject(BaseClass):
    def test_end_to_end(self):
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        self.driver.implicitly_wait(10)
        checkoutitems = CheckOut(self.driver, "")
        products = checkoutitems.getproducts()
        for product in products:
            productitems = CheckOut(self.driver, product)
            productsName = productitems.getproduct().text
            if productsName == "Blackberry":
                product = productitems.getproductname()
                product.click()
                break
        checkoutitems.getcheckout().click()
        checkoutitems.getclickcheckout().click()
        countryinput = ConfirmPage(self.driver)
        countryinput.getcountryinput().send_keys("Ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        countryinput.getcountryname().click()
        countryinput.getcheckoutradio().click()
        countryinput.getsubmitbutton().click()
        successText = countryinput.getsuccesstext().text
        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("C:\\Chrome\\chromeself.driver_win32\\screen.png")
