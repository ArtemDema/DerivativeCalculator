r"""
Синус, косинус, тангeнс и котангенс c X
"""


def trigonimetric_functions_calculating_x(index, list, type):
    list_trigonometric = []
    column = 0
    final = False 
    while final == False:
        if ")" in list[index + 1]:
            list_trigonometric.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: final = True
        elif "(" in list[index + 1]:
            list_trigonometric.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_trigonometric.append(list[index + 1])
            del list[index + 1]
    
    list_trigonometric = [''.join(list_trigonometric)]

    result_f = trigonometric_functions_x(list_trigonometric, type)

    del list[index]
    for i in range(len(result_f)):
        list.insert(index + i, result_f[i])
    
    return list

def trigonometric_functions_x(list_trigonometric, type):
    list_operations = ["^","/","√","|","*","+","(",")","+","-",]
    final = False
    while final == False:
        number = 0
        for i in range(len(list_operations)):
            for part in list_trigonometric:
                if f"{list_operations[i]}" in part:
                    if len(part) > 1:
                        number += 1
                        index_f = list_trigonometric.index(part)
                        del list_trigonometric[index_f]
                        split_f= part.split(f"{list_operations[i]}", 1)
                        split_f.insert(1, f"{list_operations[i]}")
                        if split_f[0] == "": 
                            del split_f[0]
                        if len(split_f) == 3:
                            if split_f[2] == "": 
                                del split_f[2]
                        for i in range(len(split_f)):
                            list_trigonometric.insert(index_f + i, split_f[i])
        if number == 0: final = True

    del (list_trigonometric[0])
    del (list_trigonometric[-1])

    if type == "sin":
        result = ["-","cos", f"(x)"]
        return result
    if type == "cos":
        result = ["sin", f"(x)"]
        return result
    if type == "tg":
        result = ["-", "ln", "(|cos(x)|)"]
        return result