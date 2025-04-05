class AddToCart:

    back_pack_id = "add-to-cart-sauce-labs-backpack"
    jacket_id = "add-to-cart-sauce-labs-fleece-jacket"
    T_Shirt = "add-to-cart-sauce-labs-bolt-t-shirt"
    cart_id = "shopping_cart_container"

    def __init__(self,driver):
        self.driver = driver

    def add_back_pack(self):
        self.driver.find_element("id",self.back_pack_id).click()
    
    def add_jacket(self):
        self.driver.find_element("id",self.jacket_id).click()

    def add_tshirt(self):
        self.driver.find_element("id",self.T_Shirt).click()

    def check_cart(self):
        self.driver.find_element("id",self.cart_id).click()