r"""
Модуль
"""
from .plus_and_minus_calculation import sun_and_minus_calculating

def module_calculating(index, list, minus, sum, 
           multiplication, division, division_calculating, 
           radical, radical_calculating, degree_calculating, degree, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating):
    
    list_module = []
    final = False 
    list_module.append(list[index])
    while final == False:
        if "|" in list[index + 1]:
            list_module.append(list[index + 1])
            del list[index + 1]
            final = True
        else:
            list_module.append(list[index + 1])
            del list[index + 1]
    
    list_module = [''.join(list_module)]

    result_f = module(list_module, minus, sum, 
           multiplication, division, division_calculating, 
           radical, radical_calculating, degree_calculating, degree, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating)

    del list[index]
    list.insert(index - 1, str(result_f))

    return list

def module(function: list, minus, sum, 
           multiplication, division, division_calculating, 
           radical, radical_calculating, degree_calculating, degree, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating):
    result = 1
    list_operations = ["^","/","√","*","+","-","(",")","|"]
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
    
    del (function[0])
    del (function[-1])

    list_operations = ["^","sin","cos","tg","ctg","√","log","ln","/","(","*","+","-"]
    for i in range(len(list_operations)):
        for part in function:
            if f"{list_operations[i]}" in part:

                if f"{list_operations[i]}" == "^":
                    if len(part) == 1:
                        index_f = function.index(part)
                        function = degree_calculating(index_f, function, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating)
                
                if f"{list_operations[i]}" == "sin" or f"{list_operations[i]}" == "cos" or f"{list_operations[i]}" == "tg":
                    if list_operations[i] == "sin" or list_operations[i] == "cos": len_t = 3
                    else: len_t = 2
                    if len(part) == len_t:
                        index_f = function.index(part)
                        function = trigonimetric_functions_calculating(index_f, function, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, logarithm, log_calculating, ln_calculating, bracket_calculating)

                if f"{list_operations[i]}" == "/":
                    if len(part) == 1:
                        index_f = function.index(part)
                        function = division_calculating(index_f, function, f"{list_operations[i]}", minus, sum,multiplication, degree, degree_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating)
                
                if f"{list_operations[i]}" == "log":
                    if len(part) == 3:
                        index_f = function.index(part)
                        function = log_calculating(index_f, function, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating)

                if f"{list_operations[i]}" == "ln":
                    if len(part) == 2:
                        index_f = function.index(part)
                        function = ln_calculating(index_f, function, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating)

                if f"{list_operations[i]}" == "√":
                    if len(part) == 1:
                        index_f = function.index(part)
                        function_f = radical_calculating(index_f, function_f, f"{list_operations[i]}", minus, sum, multiplication, degree, degree_calculating, division, division_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating)

                if f"{list_operations[i]}" == "(":
                    list_bracket = [function[index_f]]
                    result = bracket_calculating(list_bracket, degree, degree_calculating, division, division_calculating, logarithm, log_calculating, trigonometric_functions, trigonimetric_functions_calculating, ln_calculating, radical, radical_calculating, minus, sum, multiplication, bracket_calculating)
                    if result != None:
                        del function[index_f]
                        function.insert(index_f, str(result))

                if f"{list_operations[i]}" == "*":
                    if len(part) == 1:
                        index_f = function.index(part)
                        list_multiplication = []
                        if index_f - 2 >= 0:
                            if function[index_f - 2] == "-":
                                list_multiplication.append(function[index_f - 2])
                        list_multiplication.append(function[index_f - 1])
                        result = multiplication(list_multiplication, function[index_f + 1])
                        if result != None:
                            del function[index_f + 1]
                            del function[index_f - 1]
                            del function[index_f - 1]
                            function.insert(index_f - 1, str(result))

    function = sun_and_minus_calculating(function, sum, minus)

    function = [''.join(function)]

    if "-" in function[0]:
        result = function[0].replace("-","")
        return result
    result = function[0]
    return result