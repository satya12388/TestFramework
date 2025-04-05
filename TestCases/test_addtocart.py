import pytest
from PageObjects.loginPage import loginPage
from PageObjects.addToCart import AddToCart
from Utilities.utils import ReadConfig,LogInfo

class Test_Add_To_Cart:

    baseURL = ReadConfig.get_url()
    useremail = ReadConfig.get_user()
    password = ReadConfig.get_pwd()
    logger = LogInfo.loginfo()

    @pytest.mark.Regression
    def test_add_to_cart(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(self.baseURL)

        lp = loginPage(self.driver)
        self.logger.info("--- Testing add to cart for items ---")
        lp.setUserName(self.useremail)
        self.logger.info("Username Entered")
        lp.setUserPassword(self.password)
        self.logger.info("Password Entered")
        lp.clickLogin()
        self.logger.info("Logged int website")

        cart_page = AddToCart(self.driver)
        cart_page.add_back_pack()
        self.logger.info("Added Backpack")
        cart_page.add_tshirt()
        self.logger.info("Added Tshirt")
        cart_page.check_cart()
        self.logger.info("Clicked on cart")