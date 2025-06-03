r"""
Умножение
"""

def multiplication(first_path: list, second_path: list):
    if "x" in first_path or "x" in second_path:
        return

    return int(int(first_path[0]) * int(second_path[0]))