r"""
Деление
"""

def division(first_path: str, second_path: str):
    if int(second_path) != 0:
        return int(first_path) / int(second_path)
    return ValueError