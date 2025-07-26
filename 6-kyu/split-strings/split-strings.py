def solution(s):
    list1 = [s[2*i:(2*i)+2] for i in range(len(s)//2)]
    return list1 if len(s) % 2 == 0 else list1 + [s[-1]+'_']