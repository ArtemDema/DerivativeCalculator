r"""
Логарифм
"""
import math

def logarithm(function_f: list, function_s: list, type, minus, sum, multiplication, division, radical, degree, trigonometric_functions):
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
                        list_degree = []
                        column = 0
                        final = False 
                        while final == False:
                            if ")" in function_f[index_f + 1]:
                                list_degree.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                                column -= 1
                                if column == 0: final = True
                            elif "(" in function_f[index_f + 1]:
                                list_degree.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                                column += 1
                            else:
                                list_degree.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                        
                        list_degree = [''.join(list_degree)]

                        result_f = degree(function_f[index_f - 1], list_degree, minus, sum, multiplication, division, radical)

                        del function_f[index_f]
                        function_f.insert(index_f, str(result_f))
                
                if f"{list_operations[i]}" == "sin" or f"{list_operations[i]}" == "cos" or f"{list_operations[i]}" == "tg":
                    if list_operations[i] == "sin" or list_operations[i] == "cos": len_t = 3
                    else: len_t = 2
                    if len(part) == len_t:
                        index_f = function_f.index(part)
                        list_trigonometric = []
                        column = 0
                        final = False 
                        while final == False:
                            if ")" in function_f[index_f + 1]:
                                list_trigonometric.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                                column -= 1
                                if column == 0: final = True
                            elif "(" in function_f[index_f + 1]:
                                list_trigonometric.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                                column += 1
                            else:
                                list_trigonometric.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                        
                        list_trigonometric = [''.join(list_trigonometric)]

                        result_f = trigonometric_functions(list_trigonometric, list_operations[i], minus, sum, multiplication, division, radical, degree, logarithm)

                        del function_f[index_f]
                        function_f.insert(index_f, str(result_f))

                if f"{list_operations[i]}" == "/":
                    if len(part) == 1:
                        index_f = function_f.index(part)
                        list_division_f = []
                        list_division_s = []
                        index_division = 1
                        stop = False
                        while stop == False:
                            if "(" in function_f[index_f - index_division]:
                                stop = True
                            else:
                                index_division += 1

                        for i in range(index_division):
                            list_division_f.append(function_f[index_f - index_division])
                            index_division -= 1

                        column = 0
                        final = False 
                        while final == False:
                            if ")" in function_f[index_f + 1]:
                                list_division_s.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                                column -= 1
                                if column == 0: final = True
                            elif "(" in function_f[index_f + 1]:
                                list_division_s.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                                column += 1
                            else:
                                list_division_s.append(function_f[index_f + 1])
                                del function_f[index_f + 1]

                        list_division_f = [''.join(list_division_f)]
                        list_division_s = [''.join(list_division_s)]

                        result_f = division(list_division_f, list_division_s, minus, sum, multiplication, degree, radical, trigonometric_functions)
                        
                        stop = False
                        index_division = 1
                        while stop == False:
                            if "(" in function_f[index_f - index_division]:
                                del function_f[index_f - index_division]
                                function_f[index_f - index_division] = str(result_f)
                                stop = True
                            else: 
                                del function_f[index_f - index_division]
                                index_division += 1

                if f"{list_operations[i]}" == "√":
                    if len(part) == 1:
                        index_f = function_f.index(part)
                        list_radical = []
                        column = 0
                        final = False
                        while final == False:
                            if ")" in function_f[index_f + 1]:
                                list_radical.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                                column -= 1
                                if column == 0: final = True
                            elif "(" in function_f[index_f + 1]:
                                list_radical.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                                column += 1
                            else:
                                list_radical.append(function_f[index_f + 1])
                                del function_f[index_f + 1]
                        
                        list_radical = [''.join(list_radical)]

                        result_f = radical(list_radical, minus, sum, multiplication, degree, division, trigonometric_functions)
                        del function_f[index_f - 1]
                        function_f.insert(index_f - 1, str(result_f))

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
                            list_degree = []
                            column = 0
                            final = False 
                            while final == False:
                                if ")" in function_s[index_f + 1]:
                                    list_degree.append(function_s[index_f + 1])
                                    del function_s[index_f + 1]
                                    column -= 1
                                    if column == 0: final = True
                                elif "(" in function_s[index_f + 1]:
                                    list_degree.append(function_s[index_f + 1])
                                    del function_s[index_f + 1]
                                    column += 1
                                else:
                                    list_degree.append(function_s[index_f + 1])
                                    del function_s[index_f + 1]
                            
                            list_degree = [''.join(list_degree)]

                            result_f = trigonometric_functions(function_s[index_f - 1], list_degree, minus, sum, multiplication, division, radical)

                            del function_s[index_f - 1]
                            function_s[index_f - 1] =  str(result_f)

                    if f"{list_operations[i]}" == "/":
                        if len(part) == 1:
                            index_f = function_s.index(part)
                            list_division_f = []
                            list_division_s = []
                            index_division = 1
                            stop = False
                            while stop == False:
                                if "(" in function_s[index_f - index_division]:
                                    stop = True
                                else:
                                    index_division += 1

                            for i in range(index_division):
                                list_division_f.append(function_s[index_f - index_division])
                                index_division -= 1

                            column = 0
                            final = False 
                            while final == False:
                                if ")" in function_s[index_f + 1]:
                                    list_division_s.append(function_s[index_f + 1])
                                    del function_s[index_f + 1]
                                    column -= 1
                                    if column == 0: final = True
                                elif "(" in function_s[index_f + 1]:
                                    list_division_s.append(function_s[index_f + 1])
                                    del function_s[index_f + 1]
                                    column += 1
                                else:
                                    list_division_s.append(function_s[index_f + 1])
                                    del function_s[index_f + 1]

                            list_division_f = [''.join(list_division_f)]
                            list_division_s = [''.join(list_division_s)]

                            result_f = division(list_division_f, list_division_s, minus, sum, multiplication, degree, radical, trigonometric_functions)
                            
                            stop = False
                            index_division = 1
                            while stop == False:
                                if "(" in function_s[index_f - index_division]:
                                    del function_s[index_f - index_division]
                                    function_s[index_f - index_division] = str(result_f)
                                    stop = True
                                else: 
                                    del function_s[index_f - index_division]
                                    index_division += 1

                    if f"{list_operations[i]}" == "√":
                        if len(part) == 1:
                            index_f = function_s.index(part)
                            list_radical = []
                            column = 0
                            final = False
                            while final == False:
                                if ")" in function_s[index_f + 1]:
                                    list_radical.append(function_s[index_f + 1])
                                    del function_s[index_f + 1]
                                    column -= 1
                                    if column == 0: final = True
                                elif "(" in function_s[index_f + 1]:
                                    list_radical.append(function_s[index_f + 1])
                                    del function_s[index_f + 1]
                                    column += 1
                                else:
                                    list_radical.append(function_s[index_f + 1])
                                    del function_s[index_f + 1]
                            
                            list_radical = [''.join(list_radical)]

                            result_f = radical(list_radical, minus, sum, multiplication, degree, division, trigonometric_functions)
                            del function_s[index_f - 1]
                            function_s.insert(index_f - 1, str(result_f))

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