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
    list_operations = ["^","sin","cos","tg","ctg","√","log","ln","/","*","+","-"]
    for i in range(len(list_operations)):
        for part in start_equation:
            if f"{list_operations[i]}" in part:
                index = start_equation.index(part)

                if f"{list_operations[i]}" == "^":
                    if len(part) == 1:
                        list_degree = [start_equation[index + 1]]
                        result = degree(start_equation[index - 1], list_degree, minus, sum, multiplication, division, division_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                        del start_equation[index + 1]
                        del start_equation[index - 1]
                        del start_equation[index - 1]
                        start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                if f"{list_operations[i]}" == "sin" or f"{list_operations[i]}" == "cos" or f"{list_operations[i]}" == "tg":
                    if list_operations[i] == "sin" or list_operations[i] == "cos": len_t = 3
                    else: len_t = 2
                    if len(part) == len_t:
                        list_trigonometric = [start_equation[index + 1]]
                        result = trigonometric_functions(list_trigonometric, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, logarithm, log_calculating, ln_calculating)
                        del start_equation[index + 1]
                        del start_equation[index]
                        start_equation.insert(index, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "√":
                    if len(part) == 1:
                        list_radical = [start_equation[index + 1]]
                        result = radical(list_radical, minus, sum, multiplication, degree, degree_calculating, division, division_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                        del start_equation[index + 1]
                        del start_equation[index]
                        start_equation.insert(index, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "log":
                    if len(part) == 3:
                        list_logarithm_f = [start_equation[index + 1]]
                        list_logarithm_s = [start_equation[index + 2]]
                        result = logarithm(list_logarithm_f, list_logarithm_s, "log", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                        del start_equation[index + 1]
                        del start_equation[index]
                        del start_equation[index]
                        start_equation.insert(index, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "ln":
                    if len(part) == 2:
                        list_logarithm_f = [start_equation[index + 1]]
                        result = logarithm(list_logarithm_f, None, "lg", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                        del start_equation[index + 1]
                        del start_equation[index]
                        start_equation.insert(index, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "/":
                    if len(part) == 1:
                        list_division_f = [start_equation[index - 1]]
                        list_division_s = [start_equation[index + 1]]
                        result = division(list_division_f, list_division_s, minus, sum,multiplication, degree, degree_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                        del start_equation[index + 1]
                        del start_equation[index - 1]
                        del start_equation[index - 1]
                        start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "*":
                    if len(part) == 1:
                        result = multiplication(start_equation[index - 1], start_equation[index + 1])
                        if result != None:
                            del start_equation[index + 1]
                            del start_equation[index - 1]
                            del start_equation[index - 1]
                            start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "-":
                    if len(part) == 1:
                        result = minus(start_equation[index - 1], start_equation[index + 1])
                        if result != None:
                            del start_equation[index + 1]
                            del start_equation[index - 1]
                            del start_equation[index - 1]
                            start_equation.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "+":
                    if len(part) == 1:
                        result = sum(start_equation[index - 1], start_equation[index + 1])
                        if result != None:
                            del start_equation[index + 1]
                            del start_equation[index - 1]
                            del start_equation[index - 1]
                            start_equation.insert(index - 1, str(result))

    print(start_equation)