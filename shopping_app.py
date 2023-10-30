class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = {}

    def add_to_cart(self, product, quantity):
        if product.product_id in self.cart:
            self.cart[product.product_id] += quantity
        else:
            self.cart[product.product_id] = quantity

    def remove_from_cart(self, product, quantity):
        if product.product_id in self.cart:
            self.cart[product.product_id] -= quantity
            if self.cart[product.product_id] <= 0:
                del self.cart[product.product_id]

    def print_cart(self, product_catalog):
        print("\nItems in Cart:")   
        for key in self.cart:
            for product in product_catalog:
                if key == product.product_id:
                    print("Product:", product.name, "Quantity:", self.cart[key])

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_product(self, product_catalog, product):
        product_catalog.append(product)

    def remove_product(self, product_catalog, product_id):
         for product in product_catalog:
            if product.product_id == product_id:
                product_catalog.remove(product)

    def add_category(self, categories, new_category):
        categories.append(new_category)

    def remove_category(self, categories, category_to_remove):
        categories.remove(category_to_remove)

def create_admin(admins):
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    new_admin = Admin(username, password)
    admins.append(new_admin)
    print(f"Admin created with username: {username} and password: {password}")

def create_user(users):
    username = input("Enter user username: ")
    password = input("Enter user password: ")
    new_user = User(username, password)
    users.append(new_user)
    print(f"User created with username: {username} and password: {password}")

def admin_login(admins, product_catalog, categories):
    while True:
        username = input("Enter admin username: ").lower()
        password = input("Enter admin password: ")

        for admin in admins:
            if admin.username.lower() == username and admin.password == password:
                print("Admin login successful!")
                print_product_catalog(product_catalog)
                admin_tasks(admin, product_catalog, categories)
                return

        print("Admin login failed.")
        break

def user_login(users, product_catalog):
    while True:
        username = input("Enter user username: ").lower()
        password = input("Enter user password: ")

        for user in users:
            if user.username.lower() == username and user.password == password:
                print("User login successful!")
                print_product_catalog(product_catalog)
                user_tasks(user, product_catalog)
                return

        print("User login failed.")
        break

def user_tasks(user, product_catalog):
    while True:
        print("\nUser Tasks Menu:")
        print("1. Add Product to Cart")
        print("2. Remove Product to Cart")
        print("3. Review Cart and Checkout")
        print("4. Exit to Main Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nAdding Product to Cart")
            added_product_name = input("Enter product name to be added: ").lower()
            added_quantity = int(input("Enter quantity of item to be added to cart: "))
            valid_product = False
            for product in product_catalog:
                if product.name.lower() == added_product_name:
                    print("\nAdding to Cart:", product.name)      
                    user.add_to_cart(product, added_quantity)
                    user.print_cart(product_catalog)
                    valid_product = True
                    break
            if valid_product is False:                
                print("Product not in catalog")
        elif choice == "2":
            print("\nRemoving Product from Cart")
            removed_product_name = input("Enter product name to be removed: ").lower()
            removed_quantity = int(input("Enter quantity of item to be removed from cart: "))
            valid_product = False
            for product in product_catalog:
                if product.name.lower() == removed_product_name:
                    print("\nRemoving from Cart:", product.name)
                    user.remove_from_cart(product, removed_quantity)
                    user.print_cart(product_catalog)
                    valid_product = True
                    break
            if valid_product is False:                
                print("Product not in cart")   
        elif choice == "3":
            user.print_cart(product_catalog)
            while True:
                print("\nSelect an Option")
                print("1. Proceed to Checkout")
                print("2. Modify Order")
                print("3. Exit to Main Menu")

                choice = input("Enter your choice (1-3): ")

                if choice == "1":
                    process_payment()
                    break
                elif choice == "2":
                    break
                elif choice == "3":
                    break
                else:
                    print("Invalid choice. Please select a valid option.")

        elif choice == "4":
            print("Exiting user tasks.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def admin_tasks(admin, product_catalog, categories):
    while True:
        print("\nAdmin Tasks Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Add Category")
        print("4. Remove Category")
        print("5. Exit to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\nCreating New Product")
            new_product_name = input("Enter new product name: ")
            print("Available Categories:")
            for category in categories:
                print(category)
            while True:
                new_product_category = input("Enter product category from available categories: ")
                if new_product_category in categories:
                    valid = True
                    break
                else: 
                    print("Not a valid category")
                    valid = False
                    break
            if valid is False:
                continue
            new_product_price = input("Enter new product price: ")
            new_product_id = product_catalog[-1].product_id + 1
            new_product = Product(new_product_id, new_product_name, new_product_category, new_product_price)
            admin.add_product(product_catalog, new_product)
            print_product_catalog(product_catalog)
        elif choice == "2":
            valid_product = False
            removed_product_name = input("Enter product to be removed: ").lower()
            for product in product_catalog:
                if product.name.lower() == removed_product_name:
                    print("\nRemoving", product.name)      
                    admin.remove_product(product_catalog, product.product_id)
                    print_product_catalog(product_catalog)
                    valid_product = True
                    break
            if valid_product is False:                
                print("Product not in catalog")   
        elif choice == "3":
            print("\nCreating New Category")
            new_category = input("Enter new category name: ")
            if new_category in categories:
                print("Category already exists")
            else:
                admin.add_category(categories, new_category)
            print("\nList of categories:")
            for category in categories:
                print(category)
        elif choice == "4":            
            removed_category = input("Enter category name to remove: ")     
            if removed_category not in categories:
                print("Category does not exist")
            else:
                print("\nRemoving", removed_category)
                products_to_remove = []
                for product in product_catalog:
                    if product.category == removed_category:
                        products_to_remove.append(product)

                for product in products_to_remove:
                    product_catalog.remove(product)

                admin.remove_category(categories, removed_category)
                print("\nList of categories:")
                for category in categories:
                    print(category)
                print_product_catalog(product_catalog)
        elif choice == "5":
            print("Exiting admin tasks.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def print_product_catalog(product_catalog):
    print("\nDemo Product Catalog:")
    sorted_catalog = sorted(product_catalog, key=lambda x: (x.category, x.name))
    current_category = None

    for product in sorted_catalog:
        if product.category != current_category:
            current_category = product.category
            print(f"\nCategory: {product.category}")
        print(f"Product: {product.name} {product.price}")

def add_products(product_catalog):
    product1 = Product(1, "Sneakers", "Footwear", 50.0)
    product2 = Product(2, "Pumps", "Footwear", 40.0)
    product3 = Product(3, "Jeans", "Clothing", 45.0)
    product4 = Product(4, "Sweater", "Clothing", 35.0)
    product5 = Product(5, "iPhone", "Electronics", 500.0)
    product6 = Product(6, "TV", "Electronics", 100.0) 
    product_catalog.extend([product1, product2, product3, product4, product5, product6])
    
def display_menu():
    print("\nSelect an option:")
    print("1. Create Admin")
    print("2. Create User")
    print("3. Admin Login")
    print("4. User Login")
    print("5. Exit")

def process_payment():        
    while True:
            print("\nSelect an Option")
            print("1. Pay By Credit or Debit Card")
            print("2. Pay By PayPal")
            print("3. Exit to Main Menu")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                print("Card purchase successful!")
                break
            elif choice == "2":
                print("PayPal purchase successful!")
                break
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please select a valid option.")

def main():
    print("Welcome to the Demo Marketplace")
    product_catalog = []
    categories = ["Footwear", "Clothing", "Electronics"]
    users = []
    admins = []
    add_products(product_catalog)

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # Option to create an admin
            create_admin(admins)
        elif choice == "2":
            # Option to create a user
            create_user(users)
        elif choice == "3":
            # Option for admin login
            admin_login(admins, product_catalog, categories)
        elif choice == "4":
            # Option for user login
            user_login(users, product_catalog)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    main()
