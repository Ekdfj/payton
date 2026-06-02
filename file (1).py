from models import Product

# Създаване на продукти
products = [
    Product("Лаптоп", 1999.99, 10),
    Product("Телефон", 899.99, 25),
    Product("Слушалки", 149.99, 50),
    Product("Таблет", 649.99, 15),
    Product("Монитор", 499.99, 8),
]

print("=== СКЛАДОВА НАЛИЧНОСТ ===")
for p in products:
    p.display_info()

# Сортиране по цена
print("\n=== СОРТИРАНИ ПО ЦЕНА (низходящо) ===")
sorted_products = sorted(products, key=lambda p: p.price, reverse=True)
for p in sorted_products:
    p.display_info()

# Продажби
print("\n=== ПРОДАЖБИ ===")
products[0].sell(3)
products[1].sell(30)  # няма достатъчно

# Зареждане
print("\n=== ЗАРЕЖДАНЕ ===")
products[2].restock(20)

# Намаление
print("\n=== НАМАЛЕНИЯ (10%) ===")
for p in products:
    p.apply_discount(10)

# Филтриране на евтини продукти
print("\n=== ПРОДУКТИ ПОД 500 ЛВ. ===")
cheap = [p for p in products if p.price < 500]
for p in cheap:
    p.display_info()

# Общa стойност на склада
print("\n=== ОБЩА СТОЙНОСТ НА СКЛАДА ===")
total = sum(p.price * p.quantity for p in products)
print(f"Обща стойност: {round(total, 2)} лв.")
