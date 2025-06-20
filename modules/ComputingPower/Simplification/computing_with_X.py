r"""
Не главная, но все важная вычислительная обработка
"""

from .Mathematic_operations.check_x import *
from .cut_function import cut_function

def checks_X(equation: list):
    list = [f"{equation}"]
    # print(equation)
    list_operations = ["^","sin","cos","tg","√","|","log","ln","/","(","*"]
    for i in range(len(list_operations)):
        for part in equation:
            if f"{list_operations[i]}" in part:
                # print(equation)
                index = equation.index(part)

                if f"{list_operations[i]}" == "^":
                    if len(part) == 1:
                        list_degree = [equation[index + 1]]
                        result = degree_x(equation[index - 1], list_degree)
                        if result != None:
                            del equation[index + 1]
                            del equation[index - 1]
                            del equation[index - 1]
                            for i in range(len(result)):
                                equation.insert(index - 1 + i, result[i])
                # #----------------------------------------------------------------------------------
                # if f"{list_operations[i]}" == "sin" or f"{list_operations[i]}" == "cos" or f"{list_operations[i]}" == "tg":
                #     if list_operations[i] == "sin" or list_operations[i] == "cos": len_t = 3
                #     else: len_t = 2
                #     if len(part) == len_t:
                #         list_trigonometric = [equation[index + 1]]
                #         result = trigonometric_functions(list_trigonometric, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, logarithm, log_calculating, ln_calculating, bracket_calculating, module_calculating)
                #         if result != None:
                #             del equation[index + 1]
                #             del equation[index]
                #             equation.insert(index, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "√":
                    if len(part) == 1:
                        list_radical = [equation[index + 1]]
                        result = radical_x(list_radical)
                        if result != None:
                            del equation[index + 1]
                            del equation[index]
                            for i in range(len(result)):
                                equation.insert(index + i, result[i])
                #----------------------------------------------------------------------------------
                # elif f"{list_operations[i]}" == "|":
                #     if "(" not in equation[index]:
                #         list_module = [equation[index]]
                #         result = module(list_module, minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree_calculating, degree, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating)
                #         if result != None:
                #             del equation[index]
                #             equation.insert(index, str(result))
                # #----------------------------------------------------------------------------------
                # elif f"{list_operations[i]}" == "log":
                #     if len(part) == 3:
                #         list_logarithm_f = [equation[index + 1]]
                #         list_logarithm_s = [equation[index + 2]]
                #         result = logarithm(list_logarithm_f, list_logarithm_s, "log", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating, module_calculating)
                #         if result != None:
                #             del equation[index + 1]
                #             del equation[index]
                #             del equation[index]
                #             equation.insert(index, str(result))
                # #----------------------------------------------------------------------------------
                # elif f"{list_operations[i]}" == "ln":
                #     if len(part) == 2:
                #         list_logarithm_f = [equation[index + 1]]
                #         result = logarithm(list_logarithm_f, None, "lg", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating, module_calculating)
                #         if result != None:
                #             del equation[index + 1]
                #             del equation[index]
                #             equation.insert(index, str(result))
                # #----------------------------------------------------------------------------------
                # elif f"{list_operations[i]}" == "/":
                #     if len(part) == 1:
                #         list_division_f = [equation[index - 1]]
                #         list_division_s = [equation[index + 1]]
                #         result = division(list_division_f, list_division_s, minus, sum,multiplication, degree, degree_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating, module_calculating)
                #         if result != None:
                #             del equation[index + 1]
                #             del equation[index - 1]
                #             del equation[index - 1]
                #             equation.insert(index - 1, str(result))
                # #----------------------------------------------------------------------------------
                # elif f"{list_operations[i]}" == "(":
                #     list_bracket = [equation[index]]
                #     result = bracket_calculating(list_bracket, degree, degree_calculating, division, division_calculating, logarithm, log_calculating, trigonometric_functions, trigonimetric_functions_calculating, ln_calculating, radical, radical_calculating, minus, sum, multiplication, module_calculating)
                #     if result != None:
                #         del equation[index]
                #         equation.insert(index, str(result))

    print(equation)