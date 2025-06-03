r"""
Разделение функции на елементы и числа
"""

#Объяснение как это работает:
#перебираем список с нашей функцией. Если там будет знак, который мы сейчас перебираем то
#мы получаем местоположение этого арифметического действия по индексу.
#Потом мы удаляем елемент, где находился это знак.
#Дальше сплитим место, где мы напши знак(что бы по окончанию сплита получить "2", "2". или например "5*4/2","8")
#И по середине этого сплита добавляем наш знак, по которому мы сплитили
#Если есть пустые елементы - удаляем
#И наконец, на место удалённого индекса мы ставим наш список. Можно сказать просто заменяем его
#Весь этот цикл мы повторяем пока все арифметические действия не будут в своих елементах(если они будут не одни, то потом будет
#невозможно продолжать решение функции)

def cut_function(function: list):
    list_operations = ["^","/","*","+","-","log","lg"]
    final = False
    while final == False:
        number = 0
        for i in range(len(list_operations)):
            for part in function:
                if f"{list_operations[i]}" in part:
                    if len(part) > 1:
                        number += 1
                        index_f = function.index(part)
                        del function[index_f]
                        split_f= part.split(f"{list_operations[i]}", 1)
                        split_f.insert(1, f"{list_operations[i]}")
                        for i in range(len(split_f)):
                            function.insert(index_f + i, split_f[i])
        if number == 0: final = True
    return function