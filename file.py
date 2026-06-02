class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Продукт: {self.name} | Цена: {self.price} лв. | Количество: {self.quantity}")

    def apply_discount(self, percent):
        self.price = round(self.price * (1 - percent / 100), 2)
        print(f"Намалена цена на {self.name}: {self.price} лв.")

    def restock(self, amount):
        self.quantity += amount
        print(f"Заредено количество за {self.name}: {self.quantity} бр.")

    def sell(self, amount):
        if amount > self.quantity:
            print(f"Няма достатъчно количество от {self.name}!")
        else:
            self.quantity -= amount
            print(f"Продадено {amount} бр. от {self.name}. Остатък: {self.quantity} бр.")
