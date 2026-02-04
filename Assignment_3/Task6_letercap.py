def word_upper(s: str):
    snew = ""
    for word in s.split():
        snew += word[0].upper()
    return snew

s = input()
print(word_upper(s))