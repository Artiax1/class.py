class Supermarket:
    def __init__(self):
        self.products = {
            'Apple': {'price': 1.00, 'quantity': 100},
            'Banana': {'price': 0.50, 'quantity': 150},
            'Orange': {'price': 0.75, 'quantity': 120},
            'Milk': {'price': 1.50, 'quantity': 80},
            'Bread': {'price': 2.00, 'quantity': 50},
            'Eggs': {'price': 2.50, 'quantity': 60}
        }

    def show_products(self):
        print("Available Products in the Supermarket:")
        for item, details in self.products.items():
            print(f"{item} - Price: ${details['price']:.2f} | Available: {details['quantity']} units")
        print("\n")

    def update_product_quantity(self, product, quantity):
        if product in self.products:
            self.products[product]['quantity'] -= quantity
        else:
            print(f"{product} is not available in the supermarket.\n")

    def generate_receipt(self, cart):
        total_cost = 0
        print("\nReceipt:")
        print("------------------------------")
        for item, quantity in cart.items():
            if item in self.products:
                cost = self.products[item]['price'] * quantity
                print(f"{item}: {quantity} x ${self.products[item]['price']:.2f} = ${cost:.2f}")
                total_cost += cost
            else:
                print(f"{item} is not available.")
        print("------------------------------")
        print(f"Total: ${total_cost:.2f}")
        print("\n")
        return total_cost


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = {}

    def add_to_cart(self, product, quantity, supermarket):
        if product in supermarket.products and supermarket.products[product]['quantity'] >= quantity:
            if product in self.cart:
                self.cart[product] += quantity
            else:
                self.cart[product] = quantity
            supermarket.update_product_quantity(product, quantity)
            print(f"{product} ({quantity} units) added to {self.name}'s cart.\n")
        else:
            print(f"Sorry, {product} is not available or there is insufficient stock.\n")

    def checkout(self, supermarket):
        return supermarket.generate_receipt(self.cart)


def simulate_shopping():
    # Create the supermarket and customers
    supermarket = Supermarket()
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    # Show available products
    supermarket.show_products()

    # Customer 1 adds items to cart
    customer1.add_to_cart('Apple', 3, supermarket)
    customer1.add_to_cart('Milk', 2, supermarket)
    customer1.add_to_cart('Eggs', 1, supermarket)

    # Customer 2 adds items to cart
    customer2.add_to_cart('Banana', 5, supermarket)
    customer2.add_to_cart('Bread', 2, supermarket)

    # Customer 1 checkout
    print(f"{customer1.name}'s Checkout:")
    customer1.checkout(supermarket)

    # Customer 2 checkout
    print(f"{customer2.name}'s Checkout:")
    customer2.checkout(supermarket)

simulate_shopping()
