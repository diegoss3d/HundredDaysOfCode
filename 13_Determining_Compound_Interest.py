print('-' * 30)
print("COMPOUND INTEREST".center(30))
print('-' * 30)

def is_float(money):
    try:
        float(money)
        return money
    except ValueError:
        return False


while True:
    principal = input('Enter the principal: ')
    if is_float(principal) and float(principal) >= 1:
        principal = float(principal)
        break
while True:
    rate = input('Enter the rate of interest: ')
    if is_float(rate) and float(rate) > 0:
        rate = float(rate) / 100
        break

while True:
    year = input('Enter the number of years: ')
    if year.isnumeric() and int(year) > 0:
        year = int(year)
        break
while True:
    times = input('Enter the number of times: ')
    if times.isnumeric() and int(times) > 0:
        times = int(times)
        break

# rate = rate / 100

amount = principal * (1 + rate / times) ** (times * year)
print(f'${principal} invested at {rate/100} for {year} years \n'
      f'compounded {times} times per year is ${amount:.2f}')
