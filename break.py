def break1(n, r, iterable):
    pool = tuple(iterable)
    indices = list(range(n))
    return tuple(pool[i] for i in indices[:r])
print(break1(4,2, 'ABCD'))    

def break2(n, r, iterable):
    pool = tuple(iterable)
    indices = list(range(n))
    yield tuple(pool[i] for i in indices[:r])
t = break2(4, 2, 'abcd')    
print('next is ', next(t))
print(list(t))