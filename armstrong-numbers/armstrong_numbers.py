def is_armstrong_number(number):
    str_number = str(number)
    numbers = [int(n) for n in str_number]
    power_sum = sum(n ** len(str_number) for n in numbers)
    return power_sum == number
