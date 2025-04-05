import pytest
from PageObjects.loginPage import loginPage
from PageObjects.addToCart import AddToCart
from PageObjects.checkout import Checkout
from Utilities.utils import ReadConfig,LogInfo

class Test_Add_To_Cart:

    baseURL = ReadConfig.get_url()
    useremail = ReadConfig.get_user()
    password = ReadConfig.get_pwd()
    logger = LogInfo.loginfo()

    @pytest.mark.Sanity
    def test_checkout(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(self.baseURL)

        lp = loginPage(self.driver)
        self.logger.info("--- Testing Checkout of Items ---")
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

        checkout_page = Checkout(self.driver)
        checkout_page.click_checkout()
        self.logger.info("Clicked on checkout")
        checkout_page.enter_fname("Satya")
        self.logger.info("Entered First Name")
        checkout_page.enter_lname("Kota")
        self.logger.info("Entered Last name")
        checkout_page.enter_postcode("hello")
        self.logger.info("Entered Postal code")
        checkout_page.click_continue()
        total = checkout_page.get_total()
        self.logger.info(total)