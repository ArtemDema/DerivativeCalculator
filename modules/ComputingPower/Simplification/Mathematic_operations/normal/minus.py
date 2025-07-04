r"""
Минус
"""

import math

def minus(first_path: list, second_path: str):
    for part in first_path:
        if "x" in part or "√" in part or "sin" in part or "cos" in part or "tg" in part or "|" in part or "(" in part:
            return
        
    if "x" in second_path or "√" in second_path or "sin" in second_path or "cos" in second_path or "tg" in second_path or "|" in second_path or "(" in second_path:
        return
    
    first_path = ''.join(first_path)
    first_path = round(float(first_path), 1)
    second_path = round(float(second_path), 1)

    result = first_path - second_path
    result = round(float(result), 1)
    return result