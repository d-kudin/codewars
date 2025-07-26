def disemvowel(string_):
    list = []
    for i in string_:
        if i.isalpha() and i in 'aeiouAEIOU':
            continue
        else:
            list.append(i)
    return ''.join(list)