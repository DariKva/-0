upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']


def move(symb, num):
    if symb in upper:
        pos = (ord(symb) - ord('A'))
        return chr((pos + num) % 26 + ord('A'))
    if symb in lower:
        pos = (ord(symb) - ord('a'))
        return chr((pos + num) % 26 + ord('a'))


def cesar(str1, num):
    exstr = []
    str1 = list(str1)
    for i in str1:
        exstr.append(move(i, num))
    return "".join(exstr)


str1 = input()
num = int(input())


def cesardec(str1, num):
    return cesar(str1, -num)


print(cesardec(str1, num))
