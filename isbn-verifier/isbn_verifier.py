def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10 or not isbn:
        return False

    verifiers = range(1, 11)[::-1]
    sum_values = 0
    for index, digit in enumerate(isbn):
        check_digit = index == len(isbn) - 1
        if digit == 'X' and check_digit:
            digit = 10
        try:
            digit = int(digit)
        except ValueError:
            return False
        sum_values += digit * verifiers[index]

    return sum_values % 11 == 0

