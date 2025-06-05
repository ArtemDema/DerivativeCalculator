r"""
Деление
"""

def division(first_path: list, second_path: list, minus, sum, multiplication): 
    for i in range(len(first_path)):
        first_path[i] = first_path[i].replace("(", "").replace(")", "")
    
    for i in range(len(second_path)):
        second_path[i] = second_path[i].replace("(", "").replace(")", "")

    for part in first_path:
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
    for part in second_path:
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