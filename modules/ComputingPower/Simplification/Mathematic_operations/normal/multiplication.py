r"""
Умножение
"""

from ...cut_function import cut_function

def multiplication(first_path: list, second_path: str):
    for part in first_path:
        if "√" in part or "sin" in part or "cos" in part or "tg" in part or "|" in part:
            return
    if "√" in second_path or "sin" in second_path or "cos" in second_path or "tg" in second_path or "|" in second_path:
        return
    
    first_path = cut_function(list(first_path))
    if "(" in second_path:
        second_path = second_path[1:-1]
    second_path = cut_function(list(second_path))

    for part in first_path:
        if part == "(" or part == ")": 
            index = first_path.index(part)
            del first_path[index]

    first_path = ''.join(first_path)
    first_path = round(float(first_path), 1)
    second_path = ''.join(second_path)
    second_path = round(float(second_path), 1)
    
    result = first_path * second_path
    result = round(float(result), 1)
    return result