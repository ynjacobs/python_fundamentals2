def accepts_string(word):
    letters = len(word)
    if len(word) < 8:
        return False
    else:
        return True
word = 'hiiiiiii'
print(accepts_string(word))
word = 'yay'
print(accepts_string(word))
