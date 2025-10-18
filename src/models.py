class Product:
    """класс данных о продукте"""

    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут
        self.quantity = quantity

    @classmethod
    def new_product(
        cls, product
    ):  # возвращает экземпляр класса Product на основе данных словаря
        return cls(
            name=product["name"],
            description=product["description"],
            price=product["price"],
            quantity=product["quantity"],
        )

    @property
    def price(self) -> float:  # геттер возвращает значение приватного атрибута цены.

        return self.__price

    @price.setter
    def price(
        self, new_price
    ) -> None:  # сеттер проверки на положительное значение новой цены

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer_user = input("Снизить цену товара? ")
            if answer_user.lower() != "y":
                return
        self.__price = new_price


class Category:
    """класс данных о категориях продуктов"""

    name = str
    description = str
    products = list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products  # приватный атрибут

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """добавляем продукт в список приватных продуктов"""
        self.__products.append(product)

        Category.product_count += 1

    @property
    def products(
        self,
    ) -> str:  # геттер для вывода приватного списка продуктов по заданному формату
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str
