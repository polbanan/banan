
def palindrom(s):
    return s[::-1] == s

while True:
    s = input('Введите слово: ')
    print(f'{s} являеться палиндромом' if palindrom(s) else 'Не палиндром')

