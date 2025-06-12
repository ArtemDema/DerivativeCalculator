r"""
Логарифм
"""
import math

def log_calculating(index, list, type, minus, sum, 
              multiplication, division, division_calculating, radical, radical_calculating, 
              degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating):
    list_logarithm_f = []
    list_logarithm_s = []
    stop = False
    column = 0
    while stop == False:
        if ")" in list[index + 1]:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: stop = True
        elif "(" in list[index + 1]:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
    
    stop = False
    column = 0
    while stop == False:
        if ")" in list[index + 1]:
            list_logarithm_s.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: stop = True
        elif "(" in list[index + 1]:
            list_logarithm_s.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_logarithm_s.append(list[index + 1])
            del list[index + 1]

    result_f = logarithm(list_logarithm_f, list_logarithm_s, "log", minus, sum, 
              multiplication, division, division_calculating, radical, radical_calculating, 
              degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating)
    del list[index]
    list.insert(index, str(result_f))

def ln_calculating(index, list, type, minus, sum, 
              multiplication, division, division_calculating, radical, radical_calculating, 
              degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating):
    list_logarithm_f = []
    column = 0
    final = False 
    while final == False:
        if ")" in list[index + 1]:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: final = True
        elif "(" in list[index + 1]:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
    
    list_logarithm_f = [''.join(list_logarithm_f)]

    result_f = logarithm(list_logarithm_f, None, "ln", minus, sum, 
              multiplication, division, division_calculating, radical, radical_calculating, 
              degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating)

    del list[index]
    list.insert(index, str(result_f))

def logarithm(function_f: list, function_s: list, type, minus, sum, 
              multiplication, division, division_calculating, radical, radical_calculating, 
              degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating):
    list_operations = ["^","/","√","*","+","-","(",")"]
    final = False
    while final == False:
        number = 0
        for i in range(len(list_operations)):
            for part in function_f:
                if f"{list_operations[i]}" in part:
                    if len(part) > 1:
                        number += 1
                        index_f = function_f.index(part)
                        del function_f[index_f]
                        split_f= part.split(f"{list_operations[i]}", 1)
                        split_f.insert(1, f"{list_operations[i]}")
                        if split_f[0] == "": 
                            del split_f[0]
                        if len(split_f) == 3:
                            if split_f[2] == "": 
                                del split_f[2]
                        for i in range(len(split_f)):
                            function_f.insert(index_f + i, split_f[i])
        if number == 0: final = True

    del (function_f[0])
    del (function_f[-1])
    #----------------------------------------------------------------------------------
    if function_s != None:
        final = False
        while final == False:
            number = 0
            for i in range(len(list_operations)):
                for part in function_s:
                    if f"{list_operations[i]}" in part:
                        if len(part) > 1:
                            number += 1
                            index_f = function_s.index(part)
                            del function_s[index_f]
                            split_f= part.split(f"{list_operations[i]}", 1)
                            split_f.insert(1, f"{list_operations[i]}")
                            if split_f[0] == "": 
                                del split_f[0]
                            if len(split_f) == 3:
                                if split_f[2] == "": 
                                    del split_f[2]
                            for i in range(len(split_f)):
                                function_s.insert(index_f + i, split_f[i])
            if number == 0: final = True

        del (function_s[0])
        del (function_s[-1])
    #----------------------------------------------------------------------------------
    list_operations = ["^","sin","cos","tg","ctg","√","log","ln","/","*","+","-"]
    for i in range(len(list_operations)):
        for part in function_f:
            if f"{list_operations[i]}" in part:

                if f"{list_operations[i]}" == "^":
                    if len(part) == 1:
                        index_f = function_f.index(part)
                        function_f = degree_calculating(index_f, function_f, f"{list_operations[i]}", minus, sum, multiplication, division, radical, degree, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                
                if f"{list_operations[i]}" == "sin" or f"{list_operations[i]}" == "cos" or f"{list_operations[i]}" == "tg":
                    if list_operations[i] == "sin" or list_operations[i] == "cos": len_t = 3
                    else: len_t = 2
                    if len(part) == len_t:
                        index_f = function_f.index(part)
                        function_f = trigonimetric_functions_calculating(index_f, function_f, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, logarithm, log_calculating, ln_calculating)

                if f"{list_operations[i]}" == "/":
                    if len(part) == 1:
                        index_f = function_f.index(part)
                        function_f = division_calculating(index_f, function_f, type, minus, sum,multiplication, degree, degree_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)

                if f"{list_operations[i]}" == "√":
                    if len(part) == 1:
                        index_f = function_f.index(part)
                        function_f = radical_calculating(index_f, function_f, f"{list_operations[i]}", minus, sum, multiplication, division, radical, degree, trigonometric_functions, trigonimetric_functions_calculating)

                if f"{list_operations[i]}" == "*":
                    if len(part) == 1:
                        index_f = function_f.index(part)
                        result_f = multiplication(function_f[index_f - 1], function_f[index_f + 1])
                        del function_f[index_f - 1]
                        del function_f[index_f - 1]
                        del function_f[index_f - 1]
                        function_f.insert(index_f - 1, str(result_f))

                if f"{list_operations[i]}" == "+":
                    if len(part) == 1:
                        index_f = function_f.index(part)
                        result_f = sum(function_f[index_f - 1], function_f[index_f + 1])
                        del function_f[index_f - 1]
                        del function_f[index_f - 1]
                        del function_f[index_f - 1]
                        function_f.insert(index_f - 1, str(result_f))
            
                if f"{list_operations[i]}" == "-":
                    if len(part) == 1:
                        index_f = function_f.index(part)
                        result_f = minus(function_f[index_f - 1], function_f[index_f + 1])
                        del function_f[index_f - 1]
                        del function_f[index_f - 1]
                        del function_f[index_f - 1]
                        function_f.insert(index_f - 1, str(result_f))
    #----------------------------------------------------------------------------------
    if function_s != None:
        list_operations = ["^","sin","cos","tg","ctg","√","log","ln","/","*","+","-"]
        for i in range(len(list_operations)):
            for part in function_s:
                if f"{list_operations[i]}" in part:

                    if f"{list_operations[i]}" == "^":
                        if len(part) == 1:
                            index_f = function_s.index(part)
                            function_s = degree_calculating(index_f, function_s, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)

                    if f"{list_operations[i]}" == "sin" or f"{list_operations[i]}" == "cos" or f"{list_operations[i]}" == "tg":
                        if list_operations[i] == "sin" or list_operations[i] == "cos": len_t = 3
                        else: len_t = 2
                        if len(part) == len_t:
                            index_f = function_s.index(part)
                            function_s = trigonimetric_functions_calculating(index_f, function_s, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, logarithm, log_calculating, ln_calculating)

                    if f"{list_operations[i]}" == "/":
                        if len(part) == 1:
                            index_f = function_s.index(part)
                            function_s = division_calculating(index_f, function_s, type, minus, sum,multiplication, degree, degree_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)

                    if f"{list_operations[i]}" == "√":
                        if len(part) == 1:
                            index_f = function_s.index(part)
                            function_s = radical_calculating(index_f, function_s, f"{list_operations[i]}", minus, sum, multiplication, degree, degree_calculating, division, division_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)

                    if f"{list_operations[i]}" == "*":
                        if len(part) == 1:
                            index_f = function_s.index(part)
                            result_f = multiplication(function_s[index_f - 1], function_s[index_f + 1])
                            del function_s[index_f - 1]
                            del function_s[index_f - 1]
                            del function_s[index_f - 1]
                            function_s.insert(index_f - 1, str(result_f))

                    if f"{list_operations[i]}" == "+":
                        if len(part) == 1:
                            index_f = function_s.index(part)
                            result_f = sum(function_s[index_f - 1], function_s[index_f + 1])
                            del function_s[index_f - 1]
                            del function_s[index_f - 1]
                            del function_s[index_f - 1]
                            function_s.insert(index_f - 1, str(result_f))
                
                    if f"{list_operations[i]}" == "-":
                        if len(part) == 1:
                            index_f = function_s.index(part)
                            result_f = minus(function_s[index_f - 1], function_s[index_f + 1])
                            del function_s[index_f - 1]
                            del function_s[index_f - 1]
                            del function_s[index_f - 1]
                            function_s.insert(index_f - 1, str(result_f))

    if type == "log":
        return int(math.log(int(function_s[0]), int(function_f[0])))
    else:
        return int(math.log10(int(function_f[0])))