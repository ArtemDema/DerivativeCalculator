r"""
Плюс
"""

import math

def sum(first_path: list, second_path: str):
    if "x" in first_path or "x" in second_path:
        return
    
    first_path = ''.join(first_path)
    first_path = round(float(first_path), 1)
    second_path = round(float(second_path), 1)
    
    result = first_path + second_path
    result = round(float(result), 1)
    return result