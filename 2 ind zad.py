if __name__ == '__main__':
    s = input("Введите предложение: ")
    r = ''
    for i, x in enumerate(s):
        if i % 2 == 1:
            r += str('ы')
        else:
            r += x
    print(r)
