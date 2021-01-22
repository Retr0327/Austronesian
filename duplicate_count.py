def num_count(sentence, target):
    start=-1
    contain=[]
    while True:
        try:
            loc=sentence.index(target, start+1)
        except ValueError:
            break
        contain.append(loc)
        start=loc
    return contain