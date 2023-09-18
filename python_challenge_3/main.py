from product import Product
from inventory import Inventory


def run():
    inventory = Inventory()
    menu = """
        ==================  Inventario DaCodes ==================

        Options:
        1. Show inventory
        2. Add a new product
        3. Update the quantity of an existing product
        4. Delete a product from the inventory
        5. Exit
        
        ==========================================================
        """

    while True:
        print(menu)

        option = input("Select an option: ")

        if option == "1":
            inventory.show_inventory()

        elif option == "2":
            print("Add a new product")
            name = input("Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            product = Product(name=name, price=price, quantity=quantity)
            inventory.add_product(product)
            print("Product added successfully")

        elif option == "3":
            print("Update the quantity of an existing product")
            product_id = input("Product ID: ")
            quantity = int(input("New quantity: "))
            inventory.update_product(product_id, quantity)
            print("Product updated successfully")

        elif option == "4":
            print("Delete a product from the inventory")
            product_id = input("Product ID: ")
            inventory.delete_product(product_id)
            print("Product deleted successfully")

        elif option == "5":
            print("Exiting from Dacodes Inventory...")
            break


if __name__ == "__main__":
    run()
