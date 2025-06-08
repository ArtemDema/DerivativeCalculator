r"""
Умножение
"""

def multiplication(first_path, second_path):
    if "x" in first_path or "x" in second_path:
        return
    
    return int(int(first_path) * int(second_path))