class Item:
    all = []
    discount_rate = 0.8

    def __init__(self, name: str, price: float, qty: int = 1):
        self.name = name
        self.price = price
        self.qty = qty

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.qty

    def calculate_discount(self):
        return self.price * self.discount_rate

    def increment_discount(self, discount):
        Item.discount_rate = discount

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.qty})"


phone = Item("Phone", 1000, 2)
laptop = Item("Laptop", 10000, 5)

# phone.increment_discount(0.9)

# print(laptop.discount_rate)
# print(Item.discount_rate)

# laptop.discount_rate = 0.5

# print(laptop.discount_rate)
# print(Item.discount_rate)

# earphone = Item("Earphone", 500, 10)
# smartwatch = Item("Smartwatch", 1000, 2)
# charger = Item("Charger", 700, 4)

# print(Item.all)
