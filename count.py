def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) --> 2.5 3.0 3.5...
    n = start
    while True:
        yield n
        n += step

#result = count(10)
#print(list(result))
result = count(10,2)
print(next(result))
print(next(result))