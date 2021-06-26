# Task 2

# Write a class Product that has three attributes:
# -type
# -name
# -price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:

# - add(product, amount) - adds a specified quantity of a single product with a predefined price premium
# for your store(30 percent)
# - set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products
# specified by input identifiers (type or name). The discount must be specified in percentage
# - sell_product(product_name, amount) - removes a particular amount of products from the store if available,
# in other case raises an error. It also increments income if the sell_product method succeeds.
# - get_income() - returns amount of many earned by ProductStore instance.
# - get_all_products() - returns information about all available products in the store.
# - get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

class Product:
    def __init__(self, prod_type, name, price):
        self.type = prod_type
        self.name = name
        self.price = price


class StoreItem:
    def __init__(self, product, amount, discount=0):
        self.product_info = product
        self.amount = amount
        self.discount = discount

    def get_price(self):
        return self.product_info.price - (self.product_info.price * self.discount / 100)

    def print_product_info(self):
        if self.discount > 0:
            text = f'(with discount {self.discount}%)'
        else:
            text = ''
        print(
            f'Type: {self.product_info.type}, Name: {self.product_info.name},'
            f' Amount: {self.amount}, Price: {self.get_price()}$ {text}'
        )


class ProductStore:

    def __init__(self, name):
        self.name = name
        self.storage = []
        self.income = 0

    def add(self, product, amount):
        for item in self.storage:
            if item.product_info.name == product.name and item.product_info.type == product.type:
                item.amount += amount
                item.print_product_info()
                return

        p = StoreItem(product, amount)
        self.storage.append(p)  # self.storage.append(StoreItem(product, amount))
        p.print_product_info()

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            for item in self.storage:
                if item.product_info.name == identifier:
                    item.discount = percent
                    item.print_product_info()
        elif identifier_type == 'type':
            for item in self.storage:
                if item.product_info.type == identifier:
                    item.discount = percent
                    item.print_product_info()

    def sell_product(self, product_name, amount):
        for item in self.storage:
            if item.product_info.name == product_name:
                if amount <= item.amount:
                    item.amount -= amount
                    new_income = item.get_price() * amount
                    self.income += new_income
                    print(f"Sold {amount} items of {item.product_info.name} for {new_income}$")
                else:
                    raise ValueError('Unable selling')

    def get_income(self):
        return self.income

    def get_all_products(self):
        print('Available products:')
        for item in self.storage:
            item.print_product_info()

    def get_product_info(self, product):
        for item in self.storage:
            if product == item.product_info.name:
                return item.product_info.name, item.amount
        raise ValueError('wrong product name')


product_1 = Product('Sport', 'Football T-Shirt', 100)                   # create object of class Product
product_2 = Product('Food', 'Pringles', 5)

Super_sport = ProductStore('Super sport')                               # create object of class ProductStore
Good_Food = ProductStore('Good Food')

Super_sport.add(product_1, 100)                                         # add product in stores
Good_Food.add(product_2, 300)
Good_Food.add(product_2, 400)

Super_sport.set_discount('Football T-Shirt', 15)                        # discount
Good_Food.set_discount('Pringles', 5)


Super_sport.sell_product('Football T-Shirt', 50)                        # sell items
Good_Food.sell_product('Pringles', 500)
Good_Food.sell_product('Pringles', 100)

print(f'"{Good_Food.name}" total income: {Good_Food.get_income()}$')    # income
print(f'"{Super_sport.name}" total income: {Super_sport.get_income()}$')

Good_Food.get_all_products()                                            # get all product

assert Good_Food.get_product_info('Pringles') == ('Pringles', 100)      # product info by name
