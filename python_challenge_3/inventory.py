class Inventory:
    def __init__(self):
        self.inventory = []

    def show_inventory(self):
        print("\n\nCurrent Inventory:")
        print("{:<36} {:<25} {:<10} {:<8}".format("ID", "Name", "Price", "Quantity"))
        print("=" * 85)
        for product in self.inventory:
            print(
                "{:<36} {:<25} {:<10.2f} {:<8}".format(
                    product.id, product.name, product.price, product.quantity
                )
            )
        print("=" * 85)

    def add_product(self, product):
        self.inventory.append(product)

    def update_product(self, product_id, quantity):
        for product in self.inventory:
            if product.id == product_id:
                product.quantity = quantity
                break

    def delete_product(self, product_id):
        for product in self.inventory:
            if product.id == product_id:
                self.inventory.remove(product)
                break
