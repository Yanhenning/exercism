import random

a = 97
z = a + 25


class Robot:
    seed = 1

    def __init__(self):
        self.name = self.create_name()

    @staticmethod
    def create_name():
        first_letter = chr(random.randint(a, z)).upper()
        second_letter = chr(random.randint(a, z)).upper()
        number = random.randint(0, 999)
        return f'{first_letter}{second_letter}{number}'

    def reset(self):
        self.seed += random.randint(1, 5)
        random.seed(self.seed)
        self.name = self.create_name()
