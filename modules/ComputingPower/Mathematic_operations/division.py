r"""
Деление
"""

def division(first_path: list, second_path: list, minus, sum, multiplication, degree, radical): 
    list_operations = ["^","/","√","*","+","-","log","lg","(",")"]
    final = False
    while final == False:
        number = 0
        for i in range(len(list_operations)):
            for part in first_path:
                if f"{list_operations[i]}" in part:
                    if len(part) > 1:
                        number += 1
                        index_f = first_path.index(part)
                        del first_path[index_f]
                        split_f= part.split(f"{list_operations[i]}", 1)
                        split_f.insert(1, f"{list_operations[i]}")
                        if split_f[0] == "": 
                            del split_f[0]
                        if len(split_f) == 3:
                            if split_f[2] == "": 
                                del split_f[2]
                        for i in range(len(split_f)):
                            first_path.insert(index_f + i, split_f[i])
        if number == 0: final = True

    del (first_path[0])
    del (first_path[-1])

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

    for i in range(2):
        for part in first_path:
            if "^" in part:
                index_f = first_path.index(part)
                list_degree = []
                column = 0
                final = False 
                while final == False:
                    if ")" in first_path[index_f + 1]:
                        list_degree.append(first_path[index_f + 1])
                        del first_path[index_f + 1]
                        column -= 1
                        if column == 0: final = True
                    elif "(" in first_path[index_f + 1]:
                        list_degree.append(first_path[index_f + 1])
                        del first_path[index_f + 1]
                        column += 1
                    else:
                        list_degree.append(first_path[index_f + 1])
                        del first_path[index_f + 1]
                
                list_degree = [''.join(list_degree)]

                result_f = degree(first_path[index_f - 1], list_degree, minus, sum, multiplication, division, radical)

                del first_path[index_f - 1]
                first_path[index_f - 1] =  str(result_f)
            
            if "√" in part:
                index_f = first_path.index(part)
                list_radical = []
                column = 0
                final = False
                while final == False:
                    if ")" in first_path[index_f + 1]:
                        list_radical.append(first_path[index_f + 1])
                        del first_path[index_f + 1]
                        column -= 1
                        if column == 0: final = True
                    elif "(" in first_path[index_f + 1]:
                        list_radical.append(first_path[index_f + 1])
                        del first_path[index_f + 1]
                        column += 1
                    else:
                        list_radical.append(first_path[index_f + 1])
                        del first_path[index_f + 1]
                
                list_radical = [''.join(list_radical)]

                result_f = radical(list_radical, minus, sum, multiplication, degree, division)
                del first_path[index_f - 1]
                first_path.insert(index_f - 1, str(result_f))

            if "*" in part:
                index_f = first_path.index(part)
                result_f = multiplication(first_path[index_f - 1], first_path[index_f + 1])
                del first_path[index_f - 1]
                del first_path[index_f - 1]
                del first_path[index_f - 1]
                first_path.insert(index_f - 1, result_f)

            if "+" in part:
                index_f = first_path.index(part)
                result_f = sum(first_path[index_f - 1], first_path[index_f + 1])
                del first_path[index_f - 1]
                del first_path[index_f - 1]
                del first_path[index_f - 1]
                first_path.insert(index_f - 1, result_f)
        
            if "-" in part:
                index_f = first_path.index(part)
                result_f = minus(first_path[index_f - 1], first_path[index_f + 1])
                del first_path[index_f - 1]
                del first_path[index_f - 1]
                del first_path[index_f - 1]
                first_path.insert(index_f - 1, result_f)

    #---------------------------------------------------------------
    for i in range(2):
        for part in second_path:
            if "^" in part:
                index_f = second_path.index(part)
                list_degree = []
                column = 0
                final = False
                while final == False:
                    if ")" in second_path[index_f + 1]:
                        list_degree.append(second_path[index_f + 1])
                        del second_path[index_f + 1]
                        column -= 1
                        if column == 0: final = True
                    elif "(" in second_path[index_f + 1]:
                        list_degree.append(second_path[index_f + 1])
                        del second_path[index_f + 1]
                        column += 1
                    else:
                        list_degree.append(second_path[index_f + 1])
                        del second_path[index_f + 1]

                list_degree = [''.join(list_degree)]

                result_f = degree(second_path[index_f - 1], list_degree, minus, sum, multiplication, division)

                del second_path[index_f - 1]
                second_path[index_f - 1] = str(result_f)

            if "*" in part:
                index_f = second_path.index(part)
                result_f = multiplication(second_path[index_f - 1], second_path[index_f + 1])
                del second_path[index_f - 1]
                del second_path[index_f - 1]
                del second_path[index_f - 1]
                second_path.insert(index_f - 1, result_f)
                
            if "+" in part:
                index_f = second_path.index(part)
                result_f = sum(second_path[index_f - 1], second_path[index_f + 1])
                del second_path[index_f - 1]
                del second_path[index_f - 1]
                del second_path[index_f - 1]
                second_path.insert(index_f - 1, result_f)
        
            if "-" in part:
                index_f = second_path.index(part)
                result_f = minus(second_path[index_f - 1], second_path[index_f + 1])
                del second_path[index_f - 1]
                del second_path[index_f - 1]
                del second_path[index_f - 1]
                second_path.insert(index_f - 1, result_f)

    return int(first_path[0]) // int(second_path[0])