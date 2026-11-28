# Day 39 - OOPs Practice 5 - Restaurant Menu System
# Author: shakshi-codes-63
print("--- Day 39 - OOPs Practice: Restaurant ---")

class Dish:
    def __init__(self, name, price, is_veg=True):
        self.name = name
        self.price = price
        self.is_veg = is_veg

    def show(self):
        veg_status = "Veg" if self.is_veg else "Non-Veg"
        print(f"{self.name} ({veg_status}) - Rs. {self.price}")

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
        print(f"{self.name} Restaurant khul gaya!")

    def add_dish(self, dish):
        self.menu.append(dish)
        print(f"Menu me add hua: {dish.name}")

    def show_menu(self):
        print(f"\n--- {self.name} ka Menu ---")
        for dish in self.menu:
            dish.show()

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.ordered_items = []
        print(f"\n{customer_name} ka Order start hua!")

    def add_to_order(self, dish, quantity=1):
        for i in range(quantity):
            self.ordered_items.append(dish)
        print(f"Order hua: {dish.name} x {quantity} (Rs. {dish.price * quantity})")

    def show_bill(self):
        print(f"\n--- {self.customer_name} ka Bill ---")
        total = 0
        for item in self.ordered_items:
            print(f"{item.name} - Rs. {item.price}")
            total = total + item.price

        gst = total * 5 / 100  # 5% GST
        final_bill = total + gst

        print(f"Sub-Total: Rs. {total}")
        print(f"GST (5%): Rs. {gst}")
        print(f"FINAL BILL: Rs. {final_bill}")
        print("Thank You! Phir aana!")

# Restaurant banao
print("\n--- Restaurant Start ---")
res = Restaurant("Shakshi Dhaba")

# Menu banao
paneer = Dish("Paneer Butter Masala", 250, True)
dal = Dish("Dal Tadka", 150, True)
chicken = Dish("Butter Chicken", 350, False)
roti = Dish("Roti", 20, True)

res.add_dish(paneer)
res.add_dish(dal)
res.add_dish(chicken)
res.add_dish(roti)

res.show_menu()

# Order karo
order = Order("Shakshi")
order.add_to_order(paneer, 1)
order.add_to_order(dal, 1)
order.add_to_order(roti, 4)  # 4 Roti

order.show_bill()

# Extra Practice - Tumhara Task
print("\n--- Tumhara Task ka Example ---")
# Ek Hotel class banao jisme Room book ho aur bill bane
class Room:
    def __init__(self, room_no, price_per_night):
        self.room_no = room_no
        self.price = price_per_night
        self.is_booked = False

    def book(self, nights):
        if self.is_booked:
            print(f"Room {self.room_no} pehle se booked hai!")
        else:
            self.is_booked = True
            total = self.price * nights
            print(f"Room {self.room_no} booked! {nights} nights = Rs. {total}")

room1 = Room(101, 2000)
room1.book(3)

print("\n--- Day 39 Complete ---")
