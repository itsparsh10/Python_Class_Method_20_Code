#WAP to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] -= quantity
            if self.items[item_name]['quantity'] <= 0:
                del self.items[item_name]

    def calculate_total(self):
        total_price = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total_price

    def display_cart(self):
        print("Shopping Cart:")
        for item_name, item_info in self.items.items():
            print(f"{item_name} - Price: {item_info['price']}, Quantity: {item_info['quantity']}")
        print("Total Price:", self.calculate_total())

def main():
    shop = ShoppingCart()
    while True:
        print("\n1)Add Items")
        print("2)Remove Items")
        print("3)View Cart")
        print("4)Calculate Price")
        print("5)Checkout")
        print('6)Exit shop\n')
        choice = int(input("What do you want to do? "))
        if choice == 1:
            a=input("Enter name of product: ")
            b=float(input("Enter price: "))
            c=int(input("Enter quantity: "))
            shop.add_item(a,b,c)
        elif choice == 2:
            a=input("Enter name of product to remove: ")
            c=int(input("Enter quantity to remove: "))
            shop.remove_item(a,c)
        elif choice==3:
            shop.display_cart()
        elif choice == 4:
            print("Total:" ,shop.calculate_total())
        elif choice == 5:
            print(f"Checking out...\nRs.{shop.calculate_total()} debited from your account\nYour items will be delivered shortly.")
            break
        elif choice == 6:
            print("Thank you for shopping with us!")
            exit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()