r"""
Главная вычислительная обработка
"""

from .cut_function import cut_function
from .Mathematic_operations import *

def start_power(equation, button9):
    start_equation = equation._text
    equal_C = button9.equal_C
    list = [f"{start_equation}"]
    start_equation = cut_function(list)
    # print(start_equation)
    list_operations = ["^","sin","cos","tg","ctg","/","√","*","+","-"]
    for i in range(len(list_operations)):
        for part in start_equation:
            if f"{list_operations[i]}" in part:
                index = start_equation.index(part)

                if f"{list_operations[i]}" == "^":
                    stop = False
                    list_degree = []
                    index_degree = 1
                    while stop == False:
                        if ")" in start_equation[index + index_degree]:
                            list_degree.append(start_equation[index + index_degree])
                            stop = True
                        else:
                            list_degree.append(start_equation[index + index_degree])
                            index_degree += 1
                    result = degree(start_equation[index - 1], list_degree, minus, sum, multiplication)
                    stop = False
                    index_degree = 0
                    while stop == False:
                        if ")" in start_equation[index + index_degree]:
                            del start_equation[index + index_degree]
                            start_equation[index - 1] = str(result)
                            stop = True
                        else:
                            del start_equation[index + index_degree]
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "sin" or f"{list_operations[i]}" == "cos" or f"{list_operations[i]}" == "tg":
                    stop = False
                    list_trigonometric = []
                    index_trigonometric = 0
                    while stop == False:
                        if ")" in start_equation[index + index_trigonometric]:
                            list_trigonometric.append(start_equation[index + index_trigonometric])
                            stop = True
                        else:
                            list_trigonometric.append(start_equation[index + index_trigonometric])
                            index_trigonometric += 1
                    result = trigonometric_functions(list_trigonometric, f"{list_operations[i]}", minus, sum, multiplication)
                    stop = False
                    list_trigonometric = 0
                    while stop == False:
                        if ")" in start_equation[index + list_trigonometric]:
                            start_equation[index + list_trigonometric] = str(result)
                            stop = True
                        else:
                            del start_equation[index + list_trigonometric]
                    print(start_equation)
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "√":
                    list_radical = []
                    stop = False
                    index_radical = 1
                    while stop == False:
                        if ")" in start_equation[index + index_radical]:
                            list_radical.append(start_equation[index + index_radical])
                            stop = True
                        else:
                            list_radical.append(start_equation[index + index_radical])
                            index_radical += 1
                    result = radical(list_radical, minus, sum, multiplication)
                    stop = False
                    while stop == False:
                        if ")" in start_equation[index + 1]:
                            del start_equation[index + 1]
                            stop = True
                        else:
                            del start_equation[index + 1]
                    start_equation[index] = str(int(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "/":
                    stop = False
                    list_division_f = []
                    list_division_s = []
                    index_division = 1
                    while stop == False:
                        if "(" in start_equation[index - index_division]:
                            stop = True
                        else:
                            index_division += 1
                    for i in range(index_division):
                        list_division_f.append(start_equation[index - index_division])
                        index_division -= 1

                    stop = False
                    index_division = 1
                    while stop == False:
                        if ")" in start_equation[index + index_division]:
                            list_division_s.append(start_equation[index + index_division])
                            stop = True
                        else:
                            list_division_s.append(start_equation[index + index_division])
                            index_division += 1
                    result = division(list_division_f, list_division_s, minus, sum, multiplication)
                    stop = False
                    index_division = 1
                    while stop == False:
                        if ")" in start_equation[index + index_division]:
                            del start_equation[index + index_division]
                            stop = True
                        else: del start_equation[index + index_division]
                    stop = False
                    while stop == False:
                        if "(" in start_equation[index - index_division]:
                            del start_equation[index - index_division]
                            start_equation[index - index_division] = str(result)
                            stop = True
                        else: 
                            del start_equation[index - index_division]
                            index_division += 1
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "*":
                    result = multiplication(start_equation[index - 1], start_equation[index + 1])
                    if result == None:
                        break
                    else:
                        del start_equation[index + 1]
                        del start_equation[index - 1]
                        del start_equation[index - 1]
                        start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "-":
                    result = minus(start_equation[index - 1], start_equation[index + 1])
                    if result == None:
                        break
                    else:
                        del start_equation[index + 1]
                        del start_equation[index - 1]
                        del start_equation[index - 1]
                        start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "+":
                    result = sum(start_equation[index - 1], start_equation[index + 1])
                    if result == None:
                        break
                    else:
                        del start_equation[index + 1]
                        del start_equation[index - 1]
                        del start_equation[index - 1]
                        start_equation.insert(index - 1, str(result))

    print(start_equation)
    