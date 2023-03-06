class Product:
    # class variable
    discount_rate = 0.2
    all = list()

    # constructor
    def __init__(self, name: str, price: float = 60000, qty: int = 10):
        # instance variables
        self.name = name
        self.price = price
        self.qty = qty

        Product.all.append(self)

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

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.qty})"

    @classmethod
    def from_string(cls, data):
        # "Redmi Note 5-20000-10"
        name, price, qty = data.split("-")
        price = float(price)
        qty = int(qty)

        return cls(name, price, qty)


samsung = Product("Samsung S20 FE 5G", 50000, 5)
# samsung.display_product_details()
# samsung.display_total_price()
# print(samsung.discount_rate)

iPhone = Product("iPhone 14 Pro Max")
# Product.discount_rate = 0.5
# iPhone.discount_rate = 0.5
# iPhone.display_product_details()
# iPhone.display_total_price()
# print(iPhone.discount_rate)


onePlus = Product("OnePlus Nord 2T", 20000, 8)
# onePlus.display_product_details()

# for product in Product.all:
#     print(product)


redmi_data = "Redmi Note 5-20000-10"
oppo_data = "Oppo F9-34000-5"

redmi = Product.from_string(redmi_data)
redmi.display_product_details()
# redmi_details = redmi_data.split("-")
# redmi_product_price = float(redmi_details[1])
# redmi_prodcuct_qty = float(redmi_details[2])

# redmi = Product(redmi_details[0], redmi_product_price, redmi_prodcuct_qty)
# redmi.display_product_details()
# print(redmi_details)
# print(redmi_product_price)

# name, price, qty = redmi_data.split("-")

# print(name)
# print(price)
# print(qty)
