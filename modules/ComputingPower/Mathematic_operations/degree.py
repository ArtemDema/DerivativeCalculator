r"""
Степень
"""


def degree(first_path: str, second_path: list, minus, sum, multiplication, division, radical, logarithm):
    result = 1
    if "x" in first_path or "x" in second_path:
        return
    
    list_operations = ["^","/","√","*","+","-","(",")"]
    final = False
    while final == False:
        number = 0
        for i in range(len(list_operations)):
            for part in second_path:
                if f"{list_operations[i]}" in part:
                    if len(part) > 1:
                        number += 1
                        index_f = second_path.index(part)
                        del second_path[index_f]
                        split_f= part.split(f"{list_operations[i]}", 1)
                        split_f.insert(1, f"{list_operations[i]}")
                        if split_f[0] == "": 
                            del split_f[0]
                        if len(split_f) == 3:
                            if split_f[2] == "": 
                                del split_f[2]
                        for i in range(len(split_f)):
                            second_path.insert(index_f + i, split_f[i])
        if number == 0: final = True

    del (second_path[0])
    del (second_path[-1])
    list_operations = ["^","sin","cos","tg","ctg","√","log","ln","/","*","+","-"]
    for i in range(len(list_operations)):
        for part in second_path:
            if f"{list_operations[i]}" in part:
                if f"{list_operations[i]}" == "/":
                    if len(part) == 1:
                        index_f = second_path.index(part)
                        list_division_f = []
                        list_division_s = []
                        index_division = 1
                        stop = False
                        while stop == False:
                            if "(" in second_path[index_f - index_division]:
                                stop = True
                            else:
                                index_division += 1

                        for i in range(index_division):
                            list_division_f.append(second_path[index_f - index_division])
                            index_division -= 1

                        column = 0
                        final = False 
                        while final == False:
                            if ")" in second_path[index_f + 1]:
                                list_division_s.append(second_path[index_f + 1])
                                del second_path[index_f + 1]
                                column -= 1
                                if column == 0: final = True
                            elif "(" in second_path[index_f + 1]:
                                list_division_s.append(second_path[index_f + 1])
                                del second_path[index_f + 1]
                                column += 1
                            else:
                                list_division_s.append(second_path[index_f + 1])
                                del second_path[index_f + 1]

                        list_division_f = [''.join(list_division_f)]
                        list_division_s = [''.join(list_division_s)]

                        result_f = division(list_division_f, list_division_s, minus, sum, multiplication, degree, radical, logarithm)
                        
                        stop = False
                        index_division = 1
                        while stop == False:
                            if "(" in second_path[index_f - index_division]:
                                del second_path[index_f - index_division]
                                second_path[index_f - index_division] = str(result_f)
                                stop = True
                            else: 
                                del second_path[index_f - index_division]
                                index_division += 1
                
                if f"{list_operations[i]}" == "log":
                        if len(part) == 3:
                            index_f = second_path.index(part)
                            list_logarithm_f = []
                            list_logarithm_s = []
                            stop = False
                            column = 0
                            while stop == False:
                                if ")" in second_path[index_f + 1]:
                                    list_logarithm_f.append(second_path[index_f + 1])
                                    del second_path[index_f + 1]
                                    column -= 1
                                    if column == 0: stop = True
                                elif "(" in second_path[index_f + 1]:
                                    list_logarithm_f.append(second_path[index_f + 1])
                                    del second_path[index_f + 1]
                                    column += 1
                                else:
                                    list_logarithm_f.append(second_path[index_f + 1])
                                    del second_path[index_f + 1]
                            
                            stop = False
                            column = 0
                            while stop == False:
                                if ")" in second_path[index_f + 1]:
                                    list_logarithm_s.append(second_path[index_f + 1])
                                    del second_path[index_f + 1]
                                    column -= 1
                                    if column == 0: stop = True
                                elif "(" in second_path[index_f + 1]:
                                    list_logarithm_s.append(second_path[index_f + 1])
                                    del second_path[index_f + 1]
                                    column += 1
                                else:
                                    list_logarithm_s.append(second_path[index_f + 1])
                                    del second_path[index_f + 1]

                            result_f = logarithm(list_logarithm_f, list_logarithm_s, "log", minus, sum, multiplication, division, radical, degree)
                            del second_path[index_f]
                            second_path.insert(index_f, str(result_f))

                if f"{list_operations[i]}" == "ln":
                    if len(part) == 2:
                            index_f = second_path.index(part)
                            list_logarithm_f = []
                            column = 0
                            final = False 
                            while final == False:
                                if ")" in second_path[index_f + 1]:
                                    list_logarithm_f.append(second_path[index_f + 1])
                                    del second_path[index_f + 1]
                                    column -= 1
                                    if column == 0: final = True
                                elif "(" in second_path[index_f + 1]:
                                    list_logarithm_f.append(second_path[index_f + 1])
                                    del second_path[index_f + 1]
                                    column += 1
                                else:
                                    list_logarithm_f.append(second_path[index_f + 1])
                                    del second_path[index_f + 1]
                            
                            list_logarithm_f = [''.join(list_logarithm_f)]

                            result_f = logarithm(list_logarithm_f, None, "ln", minus, sum, multiplication, division, radical, degree)

                            del second_path[index_f]
                            second_path.insert(index_f, str(result_f))

                if f"{list_operations[i]}" == "√":
                    if len(part) == 1:
                        index_f = second_path.index(part)
                        list_radical = []
                        column = 0
                        final = False
                        while final == False:
                            if ")" in second_path[index_f + 1]:
                                list_radical.append(second_path[index_f + 1])
                                del second_path[index_f + 1]
                                column -= 1
                                if column == 0: final = True
                            elif "(" in second_path[index_f + 1]:
                                list_radical.append(second_path[index_f + 1])
                                del second_path[index_f + 1]
                                column += 1
                            else:
                                list_radical.append(second_path[index_f + 1])
                                del second_path[index_f + 1]
                        
                        list_radical = [''.join(list_radical)]

                        result_f = radical(list_radical, minus, sum, multiplication, degree, division, logarithm)
                        del second_path[index_f - 1]
                        second_path.insert(index_f - 1, str(result_f))

                if f"{list_operations[i]}" == "*":
                    if len(part) == 1:
                        index_f = second_path.index(part)
                        result_f = multiplication(second_path[index_f - 1], second_path[index_f + 1])
                        del second_path[index_f - 1]
                        del second_path[index_f - 1]
                        del second_path[index_f - 1]
                        second_path.insert(index_f - 1, str(result_f))

                if f"{list_operations[i]}" == "+":
                    if len(part) == 1:
                        index_f = second_path.index(part)
                        result_f = sum(second_path[index_f - 1], second_path[index_f + 1])
                        del second_path[index_f - 1]
                        del second_path[index_f - 1]
                        del second_path[index_f - 1]
                        second_path.insert(index_f - 1, str(result_f))
            
                if f"{list_operations[i]}" == "-":
                    if len(part) == 1:
                        index_f = second_path.index(part)
                        result_f = minus(second_path[index_f - 1], second_path[index_f + 1])
                        del second_path[index_f - 1]
                        del second_path[index_f - 1]
                        del second_path[index_f - 1]
                        second_path.insert(index_f - 1, str(result_f))

    for i in range(int(second_path[0])):
        result = result * int(first_path)
    return result