class Store:
    """This Store class will contain all the instances of the Products class"""

    def __init__(self, products_list):
        self.products_list = products_list

    def add_product(self, product):
        self.products_list.append(product)

    def remove_product(self, product):
        self.products_list.remove(product)

    def get_total_quantity(self) -> int:
        # total_products = 0
        # for product in self.products_list:
        #     total_products += product.quantity
        # return total_products
        return sum(product.quantity for product in self.products_list)

    def get_all_products(self) -> list:
        return [product for product in self.products_list if product.active]

    def order(self, shopping_list) -> float:
        # total_price = 0
        # for Product, quantity in shopping_list:
        #     total_price += Product.price * quantity
        # return total_price
        return sum(Product.price * quantity for Product, quantity in shopping_list)

