class loginPage:

    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    button_hamburger_id = "react-burger-menu-btn"
    link_logout_id = "logout_sidebar_link"


    def __init__(self,driver):
        self.driver  = driver

    def setUserName(self,username):
        self.driver.find_element("id",self.textbox_username_id).clear()
        self.driver.find_element("id",self.textbox_username_id).send_keys(username)

    def setUserPassword(self,password):
        self.driver.find_element("id",self.textbox_password_id).clear()
        self.driver.find_element("id",self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("id",self.button_login_id).click()

    def clickLogout(self):
        self.driver.find_element("id",self.button_hamburger_id).click()
        self.driver.find_element("id",self.link_logout_id).click()
