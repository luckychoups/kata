def count_vowels(s = ''):
    if not type(s) is str:
        return None
    s = s.lower()
    vowels = 'aeuio'
    c = 0
    for v in s:
        if vowels.find(v) > -1:
            c = c+1
    return c

