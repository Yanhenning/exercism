import re

pattern = r'(\.|\+|\-|\(|\))|\s+'
invalid_pattern = r'[A-z]|\@|\,|\+'

# (NXX)-NXX-XXXX


class PhoneNumber:
    def __init__(self, number):
        cleaned_number = re.sub(pattern, '', number)
        has_international_code = len(cleaned_number) == 11
        self.international_code = int(cleaned_number[0]) if has_international_code else None
        self.number = cleaned_number[1:] if has_international_code else cleaned_number
        self.validate_number()
        self.area_code = self.number[:3]

    def pretty(self):
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[-4:]}'

    def validate_international_code(self):
        if self.international_code and self.international_code != 1:
            raise ValueError('Invalid international code')

    def validate_exchange_code(self):
        if int(self.number[0]) < 2 or int(self.number[3]) < 2:
            raise ValueError('The exchange code must be greater than 2')

    def validate_number(self):
        if len(self.number) > 11:
            raise ValueError('Max length for number is 11')
        self.validate_pattern()
        self.validate_international_code()
        self.validate_exchange_code()

    def validate_pattern(self):
        if re.match(invalid_pattern, self.number):
            raise ValueError('Invalid digits')
