r"""
Синус, косинус, тангeнс и котангенс
"""

import math

def trigonometric_functions(function: list, type, minus, sum, multiplication, division, radical, degree, logarithm):
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

                if f"{list_operations[i]}" == "^":
                    if len(part) == 1:
                        index_f = function.index(part)
                        list_degree = []
                        column = 0
                        final = False 
                        while final == False:
                            if ")" in function[index_f + 1]:
                                list_degree.append(function[index_f + 1])
                                del function[index_f + 1]
                                column -= 1
                                if column == 0: final = True
                            elif "(" in function[index_f + 1]:
                                list_degree.append(function[index_f + 1])
                                del function[index_f + 1]
                                column += 1
                            else:
                                list_degree.append(function[index_f + 1])
                                del function[index_f + 1]
                        
                        list_degree = [''.join(list_degree)]

                        result_f = degree(function[index_f - 1], list_degree, minus, sum, multiplication, division, radical, logarithm)

                        del function[index_f - 1]
                        function[index_f - 1] =  str(result_f)

                if f"{list_operations[i]}" == "/":
                    if len(part) == 1:
                        index_f = function.index(part)
                        list_division_f = []
                        list_division_s = []
                        index_division = 1
                        stop = False
                        while stop == False:
                            if "(" in function[index_f - index_division]:
                                stop = True
                            else:
                                index_division += 1

                        for i in range(index_division):
                            list_division_f.append(function[index_f - index_division])
                            index_division -= 1

                        column = 0
                        final = False 
                        while final == False:
                            if ")" in function[index_f + 1]:
                                list_division_s.append(function[index_f + 1])
                                del function[index_f + 1]
                                column -= 1
                                if column == 0: final = True
                            elif "(" in function[index_f + 1]:
                                list_division_s.append(function[index_f + 1])
                                del function[index_f + 1]
                                column += 1
                            else:
                                list_division_s.append(function[index_f + 1])
                                del function[index_f + 1]

                        list_division_f = [''.join(list_division_f)]
                        list_division_s = [''.join(list_division_s)]

                        result_f = division(list_division_f, list_division_s, minus, sum, multiplication, degree, radical, logarithm)
                        
                        stop = False
                        index_division = 1
                        while stop == False:
                            if "(" in function[index_f - index_division]:
                                del function[index_f - index_division]
                                function[index_f - index_division] = str(result_f)
                                stop = True
                            else: 
                                del function[index_f - index_division]
                                index_division += 1

                if f"{list_operations[i]}" == "log":
                    if len(part) == 3:
                        index_f = function.index(part)
                        list_logarithm_f = []
                        list_logarithm_s = []
                        stop = False
                        column = 0
                        while stop == False:
                            if ")" in function[index_f + 1]:
                                list_logarithm_f.append(function[index_f + 1])
                                del function[index_f + 1]
                                column -= 1
                                if column == 0: stop = True
                            elif "(" in function[index_f + 1]:
                                list_logarithm_f.append(function[index_f + 1])
                                del function[index_f + 1]
                                column += 1
                            else:
                                list_logarithm_f.append(function[index_f + 1])
                                del function[index_f + 1]
                        
                        stop = False
                        column = 0
                        while stop == False:
                            if ")" in function[index_f + 1]:
                                list_logarithm_s.append(function[index_f + 1])
                                del function[index_f + 1]
                                column -= 1
                                if column == 0: stop = True
                            elif "(" in function[index_f + 1]:
                                list_logarithm_s.append(function[index_f + 1])
                                del function[index_f + 1]
                                column += 1
                            else:
                                list_logarithm_s.append(function[index_f + 1])
                                del function[index_f + 1]

                        result_f = logarithm(list_logarithm_f, list_logarithm_s, "log", minus, sum, multiplication, division, radical, degree)
                        del function[index_f]
                        function.insert(index_f, str(result_f))

                if f"{list_operations[i]}" == "√":
                    if len(part) == 1:
                        index_f = function.index(part)
                        list_radical = []
                        column = 0
                        final = False
                        while final == False:
                            if ")" in function[index_f + 1]:
                                list_radical.append(function[index_f + 1])
                                del function[index_f + 1]
                                column -= 1
                                if column == 0: final = True
                            elif "(" in function[index_f + 1]:
                                list_radical.append(function[index_f + 1])
                                del function[index_f + 1]
                                column += 1
                            else:
                                list_radical.append(function[index_f + 1])
                                del function[index_f + 1]
                        
                        list_radical = [''.join(list_radical)]

                        result_f = radical(list_radical, minus, sum, multiplication, degree, division)
                        del function[index_f - 1]
                        function.insert(index_f - 1, str(result_f))

                if f"{list_operations[i]}" == "*":
                    if len(part) == 1:
                        index_f = function.index(part)
                        result_f = multiplication(function[index_f - 1], function[index_f + 1])
                        del function[index_f - 1]
                        del function[index_f - 1]
                        del function[index_f - 1]
                        function.insert(index_f - 1, str(result_f))

                if f"{list_operations[i]}" == "+":
                    if len(part) == 1:
                        index_f = function.index(part)
                        result_f = sum(function[index_f - 1], function[index_f + 1])
                        del function[index_f - 1]
                        del function[index_f - 1]
                        del function[index_f - 1]
                        function.insert(index_f - 1, str(result_f))
            
                if f"{list_operations[i]}" == "-":
                    if len(part) == 1:
                        index_f = function.index(part)
                        result_f = minus(function[index_f - 1], function[index_f + 1])
                        del function[index_f - 1]
                        del function[index_f - 1]
                        del function[index_f - 1]
                        function.insert(index_f - 1, str(result_f))

    if type == "sin":
        return math.sin(int(function[0]))
    if type == "cos":
        return math.cos(int(function[0]))
    if type == "tg":
        return math.tan(int(function[0]))
    if type == "ctg":
        return math.tan(int(function[0]))