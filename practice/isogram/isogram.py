#complete this function to check if the input string is an isogram or not
def is_isogram(string):
    scrubbed = string.replace('-', '').replace(' ', '').lower()
    return len(scrubbed) == len(set(scrubbed))
    pass
