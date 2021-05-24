def is_isogram(string):
    cleaned_string = string.lower().replace(',', '').replace('-', '').replace(' ', '')
    return len(cleaned_string) == len(set(cleaned_string))
