r"""
Главная вычислительная обработка
"""

from .cut_function import cut_function
from .Arithmetic_operations import *

def start_power(equation, button9):
    start_equation = equation._text
    equal_C = button9.equal_C
    list = [f"{start_equation}"]
    start_equation = cut_function(list)
    list_operations = ["^","*","/","+","-"]
    for i in range(len(list_operations)):
        for part in start_equation:
            if f"{list_operations[i]}" in part:
                index = start_equation.index(part)

                if f"{list_operations[i]}" == "^":
                    stop = False
                    list_degree = []
                    index_degree = 0
                    while stop == False:
                        if ")" in start_equation[index + 1 + index_degree]:
                            list_degree.append(start_equation[index + 1 + index_degree])
                            stop = True
                        else:
                            list_degree.append(start_equation[index + 1 + index_degree])
                            index_degree += 1
                    result = degree(start_equation[index - 1], list_degree)
                    stop = False
                    index_degree = 0
                    while stop == False:
                        if ")" in start_equation[index + index_degree]:
                            del start_equation[index + index_degree]
                            start_equation[index - 1] = str(result)
                            stop = True
                        else:
                            del start_equation[index + index_degree]

                elif f"{list_operations[i]}" == "/":
                    stop = False
                    list_division = []
                    index_division = 0
                    while stop == False:
                        if ")" in start_equation[index + index_division]:
                            list_division.append(start_equation[index + index_division])
                            stop = True
                        else:
                            list_division.append(start_equation[index + index_division])
                            index_division += 1
                    result = division(start_equation[index - 1], list_division)

                elif f"{list_operations[i]}" == "*":
                    result = multiplication(start_equation[index - 1], start_equation[index + 1])
                    if result == None:
                        break

                elif f"{list_operations[i]}" == "-":
                    result = minus(start_equation[index - 1], start_equation[index + 1])
                    if result == None:
                        break

                elif f"{list_operations[i]}" == "+":
                    result = sum(start_equation[index - 1], start_equation[index + 1])
                    if result == None:
                        break

    print(start_equation)
    