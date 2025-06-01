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
    list_operations = ["*","/","+","-"]
    for i in range(len(list_operations)):
        for part in start_equation:
            if f"{list_operations[i]}" in part:
                index = start_equation.index(part)
                if f"{list_operations[i]}" == "+":
                    result = sum(start_equation[index - 1], start_equation[index + 1])
                elif f"{list_operations[i]}" == "-":
                    result = minus(start_equation[index - 1], start_equation[index + 1])
                elif f"{list_operations[i]}" == "*":
                    result = multiplication(start_equation[index - 1], start_equation[index + 1])
                elif f"{list_operations[i]}" == "/":
                    result = division(start_equation[index - 1], start_equation[index + 1])
                    if result == ValueError:
                        print("Произошло деление на 0")
                        return
                del start_equation[index + 1]
                del start_equation[index]
                start_equation[index - 1] = str(result)

    print(start_equation)
    