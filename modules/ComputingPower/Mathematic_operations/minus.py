r"""
Минус
"""

import math

def minus(first_path: str, second_path: str):
    if "x" in first_path or "x" in second_path:
        return
    
    first_path = round(float(first_path), 1)
    second_path = round(float(second_path), 1)
    print(first_path, second_path)
    
    return first_path - second_path