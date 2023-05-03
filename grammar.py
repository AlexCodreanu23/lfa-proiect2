def verify(word, symbol):
    if symbol not in grammar:
        return False
    elif not word and 'l' in grammar[symbol]:
        return True
    else:
        for i in grammar[symbol]:
            if isinstance(i, tuple):
                if word.startswith(i[0]) and i[0].islower():
                    if verify(word[1:], i[1]):
                        return True
                elif word.startswith(i[0]) and i[0].isupper():
                    if verify(i[1] + word, i[0]):
                        return True
            elif i == ('l',):
                if verify(word, symbol):
                    return True
    return False




grammar = {
    'S': [('a', 'A'), ('d', 'E')],
    'A': [('a', 'B'), ('a', 'S')],
    'B': [('b', 'C')],
    'C': [('b', 'D'), ('b', 'B')],
    'D': [('c', 'D'), 'l'],
    'E': ['l']
}

word=input("word= ")
symbol='S'

print(verify(word,symbol))
