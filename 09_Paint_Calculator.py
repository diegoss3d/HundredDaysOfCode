print('~' * 30)
print("Painting The Room".center(30))
print('~' * 30)


def is_number_l(leng):
    try:
        float(leng)
        return leng
    except ValueError:
        return False


def is_number_w(wid):
    try:
        float(wid)
        return wid
    except ValueError:
        return False


while True:
    length = input("Wall's length in meters: ")
    if is_number_l(length):
        break
while True:
    width = input("wall's width in meters: ")
    if is_number_w(width):
        break

length = float(length)
width = float(width)
measure = length * width
paint = 9
bucket = 1

while paint < measure:
    paint += 9
    bucket += 1

print(f'You have {measure:.2f} meters of wall \n'
      f'and will need purchase {bucket} can of paint')

