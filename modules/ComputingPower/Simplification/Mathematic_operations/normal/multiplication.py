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
    
    first_path = cut_function(first_path)
    if "(" in second_path:
        second_path = second_path[1:-1]
    second_path = cut_function(list(second_path))

    for part in first_path:
        if part == "(" or part == ")": 
            index = first_path.index(part)
            del first_path[index]


    if len(second_path) == 1 or second_path[0] == "-":
        if "x" in second_path:
            if "-" in first_path:
                if second_path[0] == "-":
                    result = f"{first_path[1]}{second_path[1]}"
                else:
                    result = f"-{first_path[1]}{second_path[0]}"
            elif "-" in second_path:
                if len(second_path) == 3:
                    result = f"-{int(first_path[0]) * int(second_path[1])}{second_path[2]}"
                else:
                    result = f"-{first_path[0]}{second_path[1]}"
            else:
                result = f"{first_path[0]}{second_path[0]}"
            return result
    else:
        if first_path[0] == "-":
            result = f"-{int(first_path[0]) * int(second_path[1])}{second_path[2]}"
        else:
            result = f"{int(first_path[0]) * int(second_path[0])}{second_path[1]}"
        return result

    if len(first_path) == 1 or first_path[0] == "-":
        if "x" in first_path:
            if "-" in second_path:
                if first_path[0] == "-":
                    result = f"{second_path[1]}{first_path[1]}"
                else:
                    result = f"-{second_path[1]}{first_path[0]}"
            elif "-" in first_path:
                result = f"-{second_path[0]}{first_path[1]}"
            else:
                result = f"{second_path[0]}{first_path[0]}"
            return result
    else:
        if second_path[0] == "-":
            result = f"-{second_path[0] * first_path[1]}{first_path[2]}"
        else:
            result = f"{second_path[0] * first_path[0]}{first_path[1]}"
        return result



    first_path = ''.join(first_path)
    first_path = round(float(first_path), 1)
    second_path = ''.join(second_path)
    second_path = round(float(second_path), 1)
    
    result = first_path * second_path
    result = round(float(result), 1)
    return result