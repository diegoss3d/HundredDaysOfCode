def sum(num1, num2):
    sumres = num1 + num2
    return sumres


def diff(num1, num2):
    sumres = num1 - num2
    return sumres


def prod(num1, num2):
    sumres = num1 * num2
    return sumres


def quot(num1, num2):
    sumres = num1 / num2
    return sumres


while True:
    n1 = input('First number: ')
    if n1.isnumeric():
        break
while True:
    n2 = input('Second number: ')
    if n2.isnumeric():
        break

n1 = int(n1)
n2 = int(n2)

print(f'{n1} + {n2} = {sum(n1, n2)}\n'
      f'{n1} - {n2} = {diff(n1, n2)}\n'
      f'{n1} * {n2} = {prod(n1, n2)}\n'
      f'{n1} / {n2} = {quot(n1, n2)}')

