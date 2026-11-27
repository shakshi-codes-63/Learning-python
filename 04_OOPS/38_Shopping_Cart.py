# Day 38 - OOPs Practice 4 - Shopping Cart
# Author: shakshi-codes-63
print("--- Day 38 - OOPs Practice: Shopping Cart ---")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name} - Rs. {self.price}")

class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []  # List me Product ke Objects aayenge
        print(f"{self.owner} ki Cart ban gayi!")

    def add_item(self, product):
        self.items.append(product)
        print(f"Add hua: {product.name} (Rs. {product.price})")

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"Remove hua: {item.name}")
                return
        print(f"'{name}' cart me nahi hai.")

    def show_cart(self):
        print(f"\n--- {self.owner} ki Cart ---")
        if len(self.items) == 0:
            print("Cart khali hai!")
            return
        for item in self.items:
            item.show()
        print(f"Total Items: {len(self.items)}")
        print(f"Total Bill: Rs. {self.get_total()}")

    def get_total(self):
        total = 0
        for item in self.items:
            total = total + item.price
        return total

    def apply_discount(self, percent):
        total = self.get_total()
        discount = total * percent / 100
        final_bill = total - discount
        print(f"\nDiscount {percent}% lag gaya!")
        print(f"Purana Bill: Rs. {total}")
        print(f"Discount: Rs. {discount}")
        print(f"FINAL BILL: Rs. {final_bill}")

# Products banao
print("\n--- Shopping Start ---")
laptop = Product("Laptop", 55000)
phone = Product("Phone", 15000)
mouse = Product("Mouse", 500)
keyboard = Product("Keyboard", 1000)

# Cart banao
my_cart = Cart("Shakshi")
my_cart.add_item(laptop)
my_cart.add_item(phone)
my_cart.add_item(mouse)
my_cart.add_item(keyboard)

my_cart.show_cart()

# Kuch remove karo
print("\n--- Item Remove ---")
my_cart.remove_item("Mouse")
my_cart.show_cart()

# Discount lagao
my_cart.apply_discount(10)

# Extra Practice - Tumhara Task
print("\n--- Tumhara Task ka Example ---")
# Ek Car class banao jisme Car ka naam, model, price ho aur show() method ho
class Car:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def show(self):
        print(f"{self.name} {self.model} - Rs. {self.price}")

car1 = Car("Swift", "2024", 800000)
car1.show()

print("\n--- Day 38 Complete ---")
