def spot_to_forward(spot,date,date0=date[0]):
    '''
    date: series of datetime, starting from T1 to T2
    spot: series of spot rate, r(t,T)
    date0: time t
    '''
    numerator=(date-date0).apply(lambda x:x.days)*spot-(date.shift(1)-date0).apply(lambda x:x.days)*spot.shift(1)
    denumerator=(date-date.shift(1)).apply(lambda x: x.days)
    forward=(numerator/denumerator).shift(-1)
    return forward
