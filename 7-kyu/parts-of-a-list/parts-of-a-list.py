def partlist(arr):
    a = []
    for i in range(len(arr)-1):
        a.append((' '.join(arr[:i+1]), ' '.join(arr[i+1:])))
    return a
​