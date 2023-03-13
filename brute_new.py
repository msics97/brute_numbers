from itertools import *
import hashlib
#import pandas as pd
import time 

start = time.time() ## точка отсчета времени

def Luhn(card):
    # Здесь храним контрольную сумму
    checksum = 0
    # Переводим номер карточки из строки в массив чисел
    cardcartas = list(map(int, card))
    # Проходимся по каждому числу
    for count, num in enumerate(cardcartas):
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
count=0
cards=[]
carta=[4,1,7,3, 9,8,0,0, 0,0,0,0, 0,0,0,0] # Здесь пишем отправную комбинацию, следите за тем, чтобы была валидное кол-во цифр в наборе
while True:
    for i in range(10):
        carta[15]=carta[15]+1
        if carta[15]==10:
            carta[15]=0
            carta[14]=carta[14]+1
        if carta[14]==10:
            carta[14]=0
            carta[13]=carta[13]+1
        if carta[13]==10:
            carta[13]=0
            carta[12]=carta[12]+1
        if carta[12]==10:
            carta[12]=0
            carta[11]=carta[11]+1
        if carta[11]==10:
            carta[11]=0
            carta[10]=carta[10]+1
        
        if carta[10]==10:
            carta[10]=0
            carta[9]=carta[9]+1
        if carta[9]==10:
            carta[9]=0
            carta[8]=carta[8]+1
        if carta[8]==10:
            carta[8]=0
            carta[7]=carta[7]+1
        if carta[7]==10:
            carta[7]=0
            carta[6]=carta[6]+1
        if carta[6]==10:
            carta[6]=0
            carta[5]=carta[5]+1

        if carta[5]==10:
            carta[5]=0
            carta[4]=carta[4]+1
        if carta[4]==10:
            carta[4]=0
            carta[3]=carta[3]+1
        if carta[3]==10:
            carta[3]=0
            carta[2]=carta[2]+1
        if carta[2]==10:
            carta[2]=0
            carta[1]=carta[1]+1
        if carta[1]==10:
            carta[1]=0
            carta[0]=carta[0]+1
        #if carta[0]==9:
        #    break    

        number = str(carta[0])+str(carta[1])+str(carta[2])+str(carta[3])+str(carta[4])+str(carta[5])+str(carta[6])+str(carta[7])+str(carta[8])+str(carta[9])+str(carta[10])+str(carta[11])+str(carta[12])+str(carta[13])+str(carta[14])+str(carta[15])
        if number == '4280000000000000': # до какого момента генерим карты +1 в последней цифре бина, например бин от 4173 98 до 4279 99, значит в этой строке будет 4280 00 (427999+1=428000 )
            break
        if Luhn(number)==True:
            m = hashlib.sha1()
            num = number.encode()
            m.update(num)
            m.digest()
            a=m.hexdigest()
            cards.append('\n' + str(number) + ' ' + str(a))

            result = ''.join(cards)
            count+=1
            print(number)
            if count%20==0:
                with open('cards1.txt', 'a') as f: # файл сохранится там же, где файл .py, название файла cards1.txt
                    f.write(str(result) + '\n')
                    cards=[]
                    count=0
                    result=[]

end = time.time() - start ## собственно время работы программы

print(end) ## вывод времени
