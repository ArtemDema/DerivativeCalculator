r"""
Проверка, и проведение действий в скобочках
"""

def bracket_calculating(function, degree, degree_calculating, division, division_calculating, 
                        logarithm, log_calculating, trigonometric_functions, trigonimetric_functions_calculating, 
                        ln_calculating, radical, radical_calculating, minus, sum, 
                        multiplication):
    
    list_operations = ["^","/","√","*","+","-","(",")"]
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

    list_operations = ["^","sin","cos","tg","ctg","√","log","ln","/","*","+","-"]
    for i in range(len(list_operations)):
        for part in function:
            if f"{list_operations[i]}" in part:
                index = function.index(part)

                if f"{list_operations[i]}" == "^":
                    if len(part) == 1:
                        result = degree_calculating(index, function, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                #----------------------------------------------------------------------------------
                if f"{list_operations[i]}" == "sin" or f"{list_operations[i]}" == "cos" or f"{list_operations[i]}" == "tg":
                    if list_operations[i] == "sin" or list_operations[i] == "cos": len_t = 3
                    else: len_t = 2
                    if len(part) == len_t:
                        result = trigonimetric_functions_calculating(index, function, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, logarithm, log_calculating, ln_calculating)
                        del function[index + 1]
                        del function[index]
                        function.insert(index, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "√":
                    if len(part) == 1:
                        result = radical_calculating(index, function, f"{list_operations[i]}", minus, sum, multiplication, degree, degree_calculating, division, division_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                        del function[index + 1]
                        del function[index]
                        function.insert(index, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "log":
                    if len(part) == 3:
                        result = log_calculating(index, function, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "ln":
                    if len(part) == 2:
                        result = ln_calculating(index, function, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "/":
                    if len(part) == 1:
                        result = division_calculating(index, function, f"{list_operations[i]}", minus, sum,multiplication, degree, degree_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "*":
                    if len(part) == 1:
                        result = multiplication(function[index - 1], function[index + 1])
                        if result != None:
                            del function[index + 1]
                            del function[index - 1]
                            del function[index - 1]
                            function.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "-":
                    if len(part) == 1:
                        result = minus(function[index - 1], function[index + 1])
                        if result != None:
                            del function[index + 1]
                            del function[index - 1]
                            del function[index - 1]
                            function.insert(index - 1, str(result))
                #----------------------------------------------------------------------------------
                elif f"{list_operations[i]}" == "+":
                    if len(part) == 1:
                        result = sum(function[index - 1], function[index + 1])
                        if result != None:
                            del function[index + 1]
                            del function[index - 1]
                            del function[index - 1]
                            function.insert(index - 1, str(result))

    return function[0]