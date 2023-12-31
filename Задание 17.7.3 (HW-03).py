#Предусловие:
##Перечень банков - исходные данные
bank1 = 'ТКБ'
bank2 = 'СКБ'
bank3 = 'ВТБ'
bank4 = 'СБЕР'
##Перечень процентных ставок в соответствующих банках
percent1 = 5.6
percent2 = 5.9
percent3 = 4.28
percent4 = 4.0
##Словарь с распределением процентных ставок по вкладам в указанных банках
per_cent = {bank1: percent1, bank2: percent2, bank3: percent3, bank4: percent4}
##Вывод предусловия на экран:
print("Распределение процентных ставок по вкладам в банках,%:\nper_cent =", per_cent)

#Ввод исходных данных для расчёта с клавиатуры:
money = input("Введите сумму вклада,руб.: ")

#Список deposit значений (накопленные средства за год вклада в каждом из банков)
deposit = [int(float(money)*percent1/100),int(float(money)*percent2/100), int(float(money)*percent3/100), int(float(money)*percent4/100)]
#Вывод списка deposit значений на экран:
print("Накопленные средства за год вклада в каждом из банков составят,руб.:\ndeposit =", deposit)

#Поиск максимального значения среди элементов в списке deposit:
i = max(deposit)
#Вывод на экран максимального значения среди элементов в списке deposit:
print("Максимальная сумма, которую вы можете заработать,руб. -", i)

#Завершение программы (форматирование):
end = "_"
print(end*70)