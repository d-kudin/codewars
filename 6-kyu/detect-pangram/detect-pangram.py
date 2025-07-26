def is_pangram(s):
    flag = True
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if s.lower().count(i) == 0:
            flag = False
            break
    if flag:
        return True
    else:
        return False