import sys


if __name__ == '__main__':
    s = input("Введите предложение: ")
    r = s.count("о") + s.count("О")

    if r == 0:
        print("В этом предложении букв о нет", file=sys.stderr)
    else:
        print("Количество букв О в предложении: ", r)