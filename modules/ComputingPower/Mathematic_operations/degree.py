r"""
Степень
"""

def degree_calculating(index, list, type, minus, sum, 
           multiplication, division, division_calculating, 
           radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating):
    list_degree = []
    column = 0
    final = False 
    while final == False:
        if ")" in list[index + 1]:
            list_degree.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: final = True
        elif "(" in list[index + 1]:
            list_degree.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_degree.append(list[index + 1])
            del list[index + 1]
    
    list_degree = [''.join(list_degree)]

    result_f = degree(list[index - 1], list_degree, minus, sum, 
           multiplication, division, division_calculating, 
           radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)

    del list[index]
    list.insert(index, str(result_f))

def degree(first_path: str, second_path: list, minus, sum, 
           multiplication, division, division_calculating, 
           radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating):
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
                
                if f"{list_operations[i]}" == "sin" or f"{list_operations[i]}" == "cos" or f"{list_operations[i]}" == "tg":
                    if list_operations[i] == "sin" or list_operations[i] == "cos": len_t = 3
                    else: len_t = 2
                    if len(part) == len_t:
                        index_f = second_path.index(part)
                        second_path = trigonimetric_functions_calculating(index_f, second_path, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, logarithm, log_calculating, ln_calculating)

                if f"{list_operations[i]}" == "/":
                    if len(part) == 1:
                        index_f = second_path.index(part)
                        second_path = division_calculating(index_f, second_path, type, minus, sum,multiplication, degree, degree_calculating, radical, radical_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)
                
                if f"{list_operations[i]}" == "log":
                    if len(part) == 3:
                        index_f = second_path.index(part)
                        second_path = log_calculating(index_f, second_path, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating)

                if f"{list_operations[i]}" == "ln":
                    if len(part) == 2:
                        index_f = second_path.index(part)
                        second_path = ln_calculating(index_f, second_path, f"{list_operations[i]}", minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating)

                if f"{list_operations[i]}" == "√":
                    if len(part) == 1:
                        index_f = second_path.index(part)
                        function_f = radical_calculating(index_f, function_f, f"{list_operations[i]}", minus, sum, multiplication, degree, degree_calculating, division, division_calculating, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating)

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

    result = float(first_path[0]) ** float(second_path[0])
    result = round(float(result), 1)
    return result