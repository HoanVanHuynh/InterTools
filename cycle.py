# itertools.cycle(iterable)
# Make an iterator returning elements from the iterable and saving a copy of each.
# When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely.
# Roughly equivalent to: 
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    print(saved)
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        print(saved)
        for element in saved:
            yield element
result = cycle('ABCD')            
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))