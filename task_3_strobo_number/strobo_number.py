def is_strobogram_number(number: str) -> bool:
    res: str = ''
    strob_digit = '0689'
    for i in range(len(number) - 1, -1, -1):
        if number[i] in strob_digit:
            if number[i] == '6':
                res += '9'
            elif number[i] == '9':
                res += '6'
            else:
                res += number[i]
        else:
            return False
    return res == number


print(is_strobogram_number("100"))
