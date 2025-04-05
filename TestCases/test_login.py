import pytest
from PageObjects.loginPage import loginPage
from Utilities.utils import ReadConfig,LogInfo

class Test_login:

    baseURL = ReadConfig.get_url()
    useremail = ReadConfig.get_user()
    password = ReadConfig.get_pwd()
    logger = LogInfo.loginfo()

    @pytest.mark.Regression
    def test_title(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(self.baseURL)
        self.logger.info("--- Testing_title ---")
        assert self.driver.title == 'Swag Labs'
        self.logger.info("Testing title has passed")

    @pytest.mark.Sanity
    def test_login(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(self.baseURL)
        lp = loginPage(self.driver)
        self.logger.info("--- Testing loging Functionality ---")
        lp.setUserName(self.useremail)
        self.logger.info("Username Entered")
        lp.setUserPassword(self.password)
        self.logger.info("Password Entered")
        lp.clickLogin()
        self.logger.info("Logged int website")
        # lp.clickLogout()

        if self.driver.title == 'Swag Labs':
            assert True
            self.logger.info("Title Verified")
            
        else:
            self.driver.save_screenshot('./Screenshots/'+'test_login_failed.png')
            self.logger.error("OOps, Title Mismatch!!")
            assert False
