# samsung_name = "Samsung S20 FE 5G"
# samsung_price = 50000
# samsung_qty = 10
# samsung_total_amount = samsung_price * samsung_qty

# iphone_name = "iPhone 14 Pro Max"
# iphone_price = 72000
# iphone_qty = 5
# iphone_total_amount = samsung_price * iphone_qty

# print(f"{iphone_name}: {iphone_price} * {samsung_qty} =  {iphone_total_amount}")

class Product:
    # products = list()

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def calculate_discount():
        pass

    def calcuate_total_amount(self):
        self.total_amount = self.price * self.qty
        return self.total_amount

    def display_product_details(self):
        self.calcuate_total_amount()
        print(f"Product name: {self.name}")
        print(f"Product total amount: {self.total_amount}")


samsung = Product("S20 FE", 50000, 10)
iphone = Product("14 pro max", 72000, 5)

samsung.display_product_details()
samsung.calculate_discount()
