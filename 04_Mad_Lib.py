from random import randint
print('=' * 30)
print("Let's create a story".center(30))
print('=' * 30)

words = randint(0, 5)

build = ['funny!', 'hilarius!', 'nice!', 'horrible!', 'How dare you?', 'this is ugly!']

while True:
    noun = str(input('Enter a noum: '))
    if len(noun) > 0:
        break
while True:
    verb = str(input('Enter a verb: '))
    if len(verb) > 0:
        break
while True:
    adjective = str(input('Enter a adjetive: '))
    if len(adjective) > 0:
        break
while True:
    adverb = str(input('Enter a adverb: '))
    if len(adverb) > 0:
        break

print(f'Do you {verb} your {adjective} {noun} {adverb}? {build[words]}')