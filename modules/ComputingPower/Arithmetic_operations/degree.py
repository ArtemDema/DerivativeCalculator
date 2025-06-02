r"""
Степень
"""
from .multiplication import multiplication
from .minus import minus
from .plus import sum

def degree(first_path: str, second_path: list):
    result = 1
    if "x" in first_path or "x" in second_path:
        return
    
    for i in range(len(second_path)):
        second_path[i] = second_path[i].replace("(", "").replace(")", "")

    if len(second_path) == 1:
        for i in range(int(second_path[0])):
            result_f = result_f * int(first_path)
        return result_f

    for part in second_path:
        if "+" in part:
            index_f = second_path.index(part)
            result_f = sum(second_path[index_f - 1], second_path[index_f + 1])
            second_path = result_f
    
        if "-" in part:
            index_f = second_path.index(part)
            result_f = minus(second_path[index_f - 1], second_path[index_f + 1])
            second_path = result_f
        
        if "*" in part:
            index_f = second_path.index(part)
            result_f = multiplication(second_path[index_f - 1], second_path[index_f + 1])
            second_path = result_f

    if second_path < 0:
        for i in range(second_path * (-1)):
            result = result * int(first_path)
        return f"1/({result})"

    for i in range(second_path):
        result = result * int(first_path)
    return result