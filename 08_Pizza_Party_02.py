print('-' * 30)
print('Sharing pizza'.center(30))
print('-' * 30)

while True:
    people = input('How many people: ')
    if people.isnumeric():
        break
while True:
    eat = input('How many pieces each person wants: ')
    if eat.isnumeric():
        break

people = int(people)
eat = int(eat)

pieces = people * eat
pizza = 8
pizzas = 1
while pizza < pieces:
    pizza += 8
    pizzas += 1

leftover = pizza - pieces

print(f'Each person wants {eat} pieces of pizza.')
print(f'We need to purchase {pizzas} full pizzas.')
print(f'there are {leftover} pieces of pizzas leftovers.')



