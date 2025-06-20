r"""
Степень c X
"""


def degree_calculating_x(index, list):
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

    result_f = degree_x(list[index - 1], list_degree)

    del list[index]
    del list[index - 1]
    list.insert(index - 1, str(result_f))

    return list

def degree_x(function_f, function_s):
    list_operations = ["^","/","√","|","*","+","(",")","+","-",]
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
    result = [f"{function_s[0]}", "*", f"{function_f}", "^", f"({float(function_s[0]) - 1.0})"]
    return result