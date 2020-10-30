import operator

def accumulate(iterable, func = operator.add, *, initial=None):
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return 
    yield total
    for element in it:
        total = func(total, element)
        yield total

data = [4,5,7]

#data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
t = accumulate(data, operator.mul)
#print(list(t))
print(next(t))
print(next(t))

def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
result = chain('ABC', 'DEF')      
# print(next(result)) 
# print(next(result)) 
# print(list(result))