def break3(n, r, iterable):
    pool = tuple(iterable)
    indices = list(range(n))
    #return [pool[i] for i in indices[:r]]
    yield [pool[i] for i in indices[:r]]
    yield tuple(pool[i] for i in indices[:r+1])
    #yield tuple(pool[i] for i in indices[:r])

t = break3(10, 3, 'abcdefghkl')
print(next(t))    
print(next(t))
print(next(t))