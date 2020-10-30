
# Make an iterator that filters elements from iterable returing only those for which
# the predicate is False. If predicate is None, return the items that are false.
# Roughly equivalent to:

def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x

t = lambda x: x%2
print(t(2))            
print(t(3))
print(t(5))
result = filterfalse(t, range(10))
print(result)
print(next(result))
print(next(result))
if not 0:
    print('this is')

print(bool(0))    
