count=int(input('Введите количество билетов:'))
price=0
for i in range(count):
    print('Введите возраст поситителя №', i+1, ':')
    z=int(input())
    if z<18:
	    price+=0 
    elif 18<=z<=25:
        price+=990
    elif z>25:
        price+=1390
if count>3:        
   print('Сумма к оплате с учетом скидки 10%:', price*0.9)
else:
    print('Сумма к оплате:', price)