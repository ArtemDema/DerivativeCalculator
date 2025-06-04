r"""
Степень
"""


def degree(first_path: str, second_path: list, minus, sum, multiplication):
    result = 1
    if "x" in first_path or "x" in second_path:
        return
    
    for i in range(len(second_path)):
        second_path[i] = second_path[i].replace("(", "").replace(")", "")

    if len(second_path) == 1:
        for i in range(int(second_path[0])):
            result = result * int(first_path)
        return result

    for part in second_path:
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
        
        if "*" in part:
            index_f = second_path.index(part)
            result_f = multiplication(second_path[index_f - 1], second_path[index_f + 1])
            del second_path[index_f - 1]
            del second_path[index_f - 1]
            del second_path[index_f - 1]
            second_path.insert(index_f - 1, result_f)

    for i in range(int(second_path[0])):
        result = result * int(first_path)
    return result