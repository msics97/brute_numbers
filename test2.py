from itertools import *
import hashlib
import pandas as pd

def Luhn(card):
    # Здесь храним контрольную сумму
    checksum = 0
    # Переводим номер карточки из строки в массив чисел
    cardnumbers = list(map(int, card))
    # Проходимся по каждому числу
    for count, num in enumerate(cardnumbers):
        # Если index чётный, значит число стоит на нечётной позиции
        # Так получается потому что считаем с нуля
        if count % 2 == 0:
            buffer = num * 2
            # Если удвоенное число больше 9, то вычитаем из него 9 и прибавляем к контрольной сумме
            if buffer > 9:
                buffer -= 9
            # Если нет, то сразу прибавляем к контрольной сумме
            checksum += buffer
        # Если число стоит на чётной позиции, то прибавляем его к контрольной сумме
        else:
            checksum += num
    # Если контрольная сумма делится без остатка на 10, то номер карты правильный
    return checksum % 10 == 0


cards=[]
count=0
for i in product('0123456789', repeat=12):
    number = '4276' + i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + i[7] + i[8] + i[9]+i[10]+i[11]
    print(number)
    if Luhn(number)==True:
        m = hashlib.sha1()
        num = number.encode()
        m.update(num)
        m.digest()
        a=m.hexdigest()
        cards.append('\n' + str(number) + ' ' + str(a))

        result = ''.join(cards)
        count+=1
        if count%20==0:
            with open('cards.txt', 'a') as f:
                f.write(str(result) + '\n')
                cards=[]
                count=0
                result=[]