def order(sentence):
    list1 = []
    for i in range(len(sentence)):
        for j in sentence.split():
            if str(i+1) in j:
                list1.append(j)
    return ' '.join(list1)