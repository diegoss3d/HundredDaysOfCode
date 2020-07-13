while True:
    ask = str(input('What is the quote? '))
    if len(ask) > 0:
        break
while True:
    who = str(input('Who said it? '))
    if len(who) > 0:
        break
print(f'{who} says: "{ask}."')