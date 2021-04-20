alphabet = "abcdefghijklmnopqrstuvwxyz"


def is_pangram(sentence):
    return not bool(set(alphabet) - set(sentence.lower()))
