class Checkout:
    checkout_id = "checkout"
    first_name_id = "first-name"
    last_name_id = "last-name"
    postal_code_id = "postal-code"
    continue_id = "continue"
    total_xpath = "//div[@class = 'summary_total_label']"


    def __init__(self,driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element("id",self.checkout_id).click()

    def enter_fname(self,fname):
        self.driver.find_element("id",self.first_name_id).send_keys(fname)

    def enter_lname(self,lname):
        self.driver.find_element("id",self.last_name_id).send_keys(lname)

    def enter_postcode(self,postcode):
        self.driver.find_element("id",self.postal_code_id).send_keys(postcode)

    def click_continue(self):
        self.driver.find_element("id",self.continue_id).click()

    def get_total(self):
        total = self.driver.find_element("xpath",self.total_xpath).text
        return total

    
