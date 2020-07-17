print('=' * 30)
print("Room feet calculator".center(30))
print('=' * 30)

while True:
    length = input('Length of the room in feet: ')
    if length.isnumeric():
        break
while True:
    width = input('Width of the room in feet: ')
    if width.isnumeric():
        break

res = int(length) * int(width)
metro = res * 0.09290304

print(f'The area in feet is: {res}')
print(f'The area in meters if: {metro}')