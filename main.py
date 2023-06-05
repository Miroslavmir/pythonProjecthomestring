# # 9.38. Дано слово из 12 букв. Поменять местами его трети следующим образом:
# # а) первую треть слова разместить на месте третьей, вторую треть — на месте
# # первой, третью треть — на месте второй;
# text = input('vvod')
# x = input('symbol')
# xLen = len(text)
# if xLen == 12:
#      if x == 'a':
#          print(text[4:8] + text[8:12] + text[:4])
#      elif x == 'b':
#          print(text[8:12] + text[0:4] + text[4:8])
#      else:
#          print('symbol on Englisch, a or b')
# else:
#       print('lenght word not 12 symbols')


# # 9.90. Дано предложение. Все буквы е в нем заменить буквой и
# решение1
# string = input('ведите предложение\n') # new red car
# x = string.replace('e','i')
# print(x)

# решение 2
# string = input('введите текст')
# xLen = len(string)
# x = xLen * (-1)
# while True:
#     if string[x] =='e':
#         print('i', end="")
#     else:
#         print(string[v], end="")
#     x += 1
#     xLen -= 1
#     if xLen == 0:
#         break


# # 9.92. Дано предложение. Все его символы, стоящие на четных местах, заменить
# # буквой ы.
# a = input('введите текст\n')
# b = ''
# for counter in range(len(a)):
#     if counter % 2 == 1:
#         b += 'ы'
# else:
#     b += a[counter]
# print(b)
# #
#
# 9.105. Дано слово из 12-ти букв. Переставить в обратном порядке буквы,
# расположенные между второй и десятой буквами (т. е. с третьей по девятую)
# string = 'еженедельник'
# if len(string) == 12:
#     print(string[0:3] + string[9:2:-1] + string[10:12])
# else:
#     print('error')


# 9.153. Дан текст. Найти наибольшее количество идущих подряд одинаковых символов .
# # символ вводится с клавиатуры

string = input('vvod')
symbol = input('symbol')
xlen = len(string)
c = (xlen * (-1))
summa = 0
summ = 0
while True:
    c = string[c]
    if c == symbol:
        summa += 1
    if summ <= summa:
        summ = summa
    if c != symbol:
        summa *= 0
    c += 1
    xlen -= 1
    if c == 0:
        break
print(summ)
