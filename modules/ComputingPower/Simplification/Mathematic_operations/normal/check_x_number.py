


def check_x(index, function):
    list_operation = ["*"]
    
    left_pos = index - 1
    while left_pos >= 0 and function[left_pos] not in list_operation:
        left_pos -= 1

    if left_pos >= 0:
        if "x" in function[left_pos - 1]:
            return False
    

    right_pos = index + 1
    while right_pos < len(function) and function[right_pos] not in list_operation:
        right_pos += 1
    print(right_pos)
    if right_pos < len(function):
        if "x" in function[right_pos + 1]:
            return False
    
    return True