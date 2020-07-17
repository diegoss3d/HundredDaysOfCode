print('-' * 30)
print('Sharing pizza'.center(30))
print('-' * 30)

while True:
    people = input('How many people: ')
    if people.isnumeric():
        break
while True:
    pizza = input('How many pizzas: ')
    if pizza.isnumeric():
        break
piece = int(pizza) * 8
eat = piece // int(people)
leftover = int(piece) % int(people)

print(f'{people} people with {pizza} pizzas.')
if eat < 2:
    print(f'Each person gets {eat} piece of pizza.')
else:
    print(f'Each person gets {eat} pieces of pizza.')
print(f'There are {leftover} leftover pieces.')



