r"""
Корень c X
"""


def radical_calculating(index, list):
    list_radical = []
    column = 0
    final = False
    while final == False:
        if ")" in list[index + 1]:
            list_radical.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: final = True
        elif "(" in list[index + 1]:
            list_radical.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_radical.append(list[index + 1])
            del list[index + 1]
    
    list_radical = [''.join(list_radical)]

    result_f = radical_x(list_radical)
    del list[index - 1]
    list.insert(index - 1, str(result_f))

    return list

def radical_x(function):
    list_operations = ["^","/","√","|","*","+","(",")","+","-",]
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
    result = ["(1)", "/", "(2*√x)"]
    return result