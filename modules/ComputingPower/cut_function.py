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
    list_operations = ["^","/","√","*","+","-","log","lg","(",")"]
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
                        if split_f[0] == "": 
                            del split_f[0]
                        if len(split_f) == 3:
                            if split_f[2] == "": 
                                del split_f[2]
                        for i in range(len(split_f)):
                            function.insert(index_f + i, split_f[i])
        if number == 0: final = True

    column = 0
    for part in function:
        if "(" in part:
            column += 1
            index_f = function.index(part)
            final = False
            while final == False:
                if ")" in function[index_f + 1]:
                    function[index_f] = str(function[index_f]) + str(function[index_f + 1])
                    del function[index_f + 1]
                    column -= 1
                    if column == 0: final = True
                elif "(" in function[index_f + 1]:
                    function[index_f] = str(function[index_f]) + str(function[index_f + 1])
                    del function[index_f + 1]
                    column += 1
                else:
                    function[index_f] = str(function[index_f]) + str(function[index_f + 1])
                    del function[index_f + 1]

    return function
