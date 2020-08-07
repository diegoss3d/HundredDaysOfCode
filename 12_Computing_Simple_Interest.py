print('-' * 30)
print("Computing Simple Interest".center(30))
print('-' * 30)


def is_float(n):
    try:
        float(n)
        return n
    except ValueError:
        return False


while True:
    p = input('Enter the principal value: ')
    if is_float(p) and float(p) >= 1:
        break
while True:
    r = input('Enter the rate of interest: ')
    if is_float(r) and float(r) > 0:
        break
while True:
    t = input('Enter the number of years: ')
    if t.isnumeric() and int(t) > 0:
        break

r = float(r) / 100
a = float(p) * (1 + float(r) * int(t))
print(f'After {t} years at {r}, the investment will be worth ${a:.2f}')
