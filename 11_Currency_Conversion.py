print('=' * 30)
print("Currency Conversion". center(30))
print('=' * 30)


def euro_dollar(cash):
    dollar = float(cash) / 0.8623
    return dollar


def real_dollar(cash):
    dollar = float(cash) / 5.21164
    return dollar


def euro_real(cash):
    real = float(cash) / 0.165233
    return real


def dollar_real(cash):
    real = float(cash) / 0.191880
    return real


def dollar_euro(cash):
    euro = float(cash) / 1.16137
    return euro


def real_euro(cash):
    euro = float(cash) / 6.05270
    return euro


def is_money(cash):
    try:
        float(cash)
        return cash
    except ValueError:
        return False


converts = {1: "euro to dollar", 2: "real to dollar",
            3: "euro to real", 4: "dollar to real",
            5: "dollar to euro", 6: "real to euro"}

for k, v in converts.items():
    print(f'{k} - {v}')
print('-' * 30)

while True:
    money = input('amount money to convert: ')
    if is_money(money) and int(money) > 1:
        break
while True:
    option = input("Enter with a valid option: ")
    if option.isnumeric() and 0 < int(option) < 7:
        break


if "1" in option:
    print(f'With €{money} you buy ${euro_dollar(money):.3f}')
elif "2" in option:
    print(f'With R${money} you buy ${real_dollar(money):.3f}')
elif "3" in option:
    print(f'With €{money} you buy R${euro_real(money):.3f}')
elif "4" in option:
    print(f'With ${money} you buy R${dollar_real(money):.3f}')
elif "5" in option:
    print(f'With ${money} you buy €{dollar_euro(money):.3f}')
elif "6" in option:
    print(f'With R${money} you buy €{real_euro(money):.3f}')