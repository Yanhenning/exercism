def convert(number):
    factor_three = number % 3 == 0
    factor_five = number % 5 == 0
    factor_seven = number % 7 == 0
    output = ''

    if factor_three:
        output += 'Pling'

    if factor_five:
        output += 'Plang'

    if factor_seven:
        output += 'Plong'

    if bool(output):
        return output

    return str(number)
