print('~' * 30)
print("Let's shopping".center(30))
print('~' * 30)

price_item = []
quantity_item = []


def is_float(preco):
    try:
        float(preco)
        return preco
    except ValueError:
        return False


for c in range(1, 4):
    while True:
        single_price = input(f'Enter the price of item {c}: ')
        if is_float(single_price):
            price_item.append(single_price)
            break
    while True:
        single_quantity = input(f'Enter the quantity of item {c}: ')
        if single_quantity.isnumeric():
            quantity_item.append(single_quantity)
            break

subtotal = 0
for pos in range(len(price_item)):
    soma = float(price_item[pos]) * float(quantity_item[pos])
    subtotal += soma
tax = subtotal * 0.055
total = subtotal + tax
print(f'subtotal: {subtotal:.2f}')
print(f'Tax: {tax:.2f}')
print(f'Total: {total:.2f}')
