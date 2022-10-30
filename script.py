per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))
d_new = list(per_cent.values())
deposit = max([i * money for i in d_new])
print('Максимальная сумма, которую вы можете заработать — ', deposit)