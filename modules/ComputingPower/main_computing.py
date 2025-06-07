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

                # if f"{list_operations[i]}" == "^":
                #     list_degree = [start_equation[index + 1]]
                #     result = degree(start_equation[index - 1], list_degree, minus, sum, multiplication, division)
                #     del start_equation[index + 1]
                #     del start_equation[index - 1]
                #     del start_equation[index - 1]
                #     start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                if f"{list_operations[i]}" == "sin" or f"{list_operations[i]}" == "cos" or f"{list_operations[i]}" == "tg":
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
                    result = radical(start_equation[index + 1], minus, sum, multiplication)
                    del start_equation[index + 1]
                    del start_equation[index - 1]
                    del start_equation[index - 1]
                    start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "/":
                    list_division_f = [start_equation[index - 1]]
                    list_division_s = [start_equation[index + 1]]
                    result = division(list_division_f, list_division_s, minus, sum, multiplication, degree)
                    del start_equation[index + 1]
                    del start_equation[index - 1]
                    del start_equation[index - 1]
                    start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "*":
                    result = multiplication(start_equation[index - 1], start_equation[index + 1])
                    if result != None:
                        del start_equation[index + 1]
                        del start_equation[index - 1]
                        del start_equation[index - 1]
                        start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "-":
                    result = minus(start_equation[index - 1], start_equation[index + 1])
                    if result != None:
                        del start_equation[index + 1]
                        del start_equation[index - 1]
                        del start_equation[index - 1]
                        start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "+":
                    result = sum(start_equation[index - 1], start_equation[index + 1])
                    if result != None:
                        del start_equation[index + 1]
                        del start_equation[index - 1]
                        del start_equation[index - 1]
                        start_equation.insert(index - 1, str(result))

    print(start_equation)
    