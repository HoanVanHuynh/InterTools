import itertools
def is_even(x):
    return x % 2 == 0
lst = [0,2,4,12,18,12,14,22,23,44]
result6 = list(itertools.dropwhile(is_even, lst))
print(result6)
# itertools.dropwhile enables you to take items from a sequence 
# after a condition first becomes False
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1, 4, 6, 4, 1])
    iterable = iter(iterable)
    for x in iterable:

        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x 
result = dropwhile(lambda x: x<5, [100,99,6,4,1])
print(next(result))
print(next(result))

print(list(result))
result1 = dropwhile(lambda x: x<5, [1,2,3,4,1000, 2000,1])
print(next(result1))
print(next(result1))

f = lambda x: x<5
print(f(2))
print(f(3))
