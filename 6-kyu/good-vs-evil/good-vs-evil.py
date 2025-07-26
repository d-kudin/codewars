def good_vs_evil(good, evil):
    countgood = sum(map(lambda x,y: int(x)*y, good.split(" "), [1,2,3,3,4,10]))
    countevil = sum(map(lambda x,y: int(x)*y, evil.split(" "), [1,2,2,2,3,5,10]))
    if countgood > countevil:
        return "Battle Result: Good triumphs over Evil"
    elif countgood < countevil:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"