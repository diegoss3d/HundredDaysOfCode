from datetime import datetime

print('=' * 40)
print("WHEN YOU SHOULD TO RETIRE?".center(40))
print('=' * 40)

now = datetime.now().year
age = int(input('Your current age: '))
agePlans = int(input('When do you like to retire: '))
left = agePlans - age
when = now + left

if age > 65:
    print('You already should to be retired!')
else:
    print(f'You have {left} years left until you can retire!')
    print(f"It's {now}, so you can retire in {when}")

