def is_strobogram_number(num: str) -> bool:
    res: str = ''
    strob_digit = '0689'
    for i in range(len(num) - 1, -1, -1):
        if num[i] in strob_digit:
            if num[i] == '6':
                res += '9'
            elif num[i] == '9':
                res += '6'
            else:
                res += num[i]
        else:
            return False
    return res == num


print(is_strobogram_number("100"))
