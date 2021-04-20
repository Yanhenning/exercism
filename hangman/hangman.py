# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = list(word)
        self.masked_word = ['_' for _ in range(len(word))]

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError('Game ended')

        if self.remaining_guesses <= 0:
            self.status = STATUS_LOSE

        if char not in self.word:
            self.remaining_guesses -= 1
            return

        while char in self.word:
            index_char = self.word.index(char)
            self.masked_word[index_char] = self.word[index_char]
            self.word[index_char] = '_'

        if '_' not in self.masked_word:
            self.status = STATUS_WIN

    def get_masked_word(self):
        return ''.join(self.masked_word)

    def get_status(self):
        return self.status
