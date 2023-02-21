class Product:
    # class variable
    discount_rate = 0.2

    # constructor
    def __init__(self, name: str, price: float = 60000, qty: int = 10):
        # instance variables
        self.name = name
        self.price = price
        self.qty = qty

    def calculate_discount(self):
        self.discount_amount = self.price * self.discount_rate
        return self.discount_amount

    # instance method
    # python passes the object itself as a first argument
    def calculate_total_price(self):
        self.calculate_discount()
        self.total_amount = (self.price - self.discount_amount) * self.qty
        return self.total_amount

    def display_total_price(self):
        # calling instance method
        self.calculate_total_price()
        print(self.total_amount)

    def display_product_details(self):
        print(
            f"Product name: {self.name}, price: {self.price}, qty: {self.qty}")


samsung = Product("Samsung S20 FE 5G", 50000, 5)
samsung.display_product_details()
samsung.display_total_price()
print(samsung.discount_rate)

iPhone = Product("iPhone 14 Pro Max")
# Product.discount_rate = 0.5
iPhone.discount_rate = 0.5
iPhone.display_product_details()
iPhone.display_total_price()
print(iPhone.discount_rate)


onePlus = Product("OnePlus Nord 2T", 20000, 8)
print(onePlus.discount_rate)
