def xo(s):
    count1 = 0
    count2 = 0
    for i in s:
        if i in 'xX':
            count1 += 1
        elif i in 'oO':
            count2 += 1
    return count1 == count2