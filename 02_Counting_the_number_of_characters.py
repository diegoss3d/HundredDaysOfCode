while True:
    word = str(input('Write your input string: '))
    size = int(len(word))
    if size != 0:
        break
print(f'{word} has {len(word)} characters!')