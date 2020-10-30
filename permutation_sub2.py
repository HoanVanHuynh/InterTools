def permutation_sub2(str):
    str = list(str)
    ret = []
    for index, c in enumerate(str):
        str[0], str[index] = str[index], str[0]
        for index, e in enumerate(str[1:]):
            ret.append(c + e)
        str[0], str[index] = str[index], str[0]
    return ret
print(permutation_sub2('ABCD'))
print(permutation_sub2('ABCDE'))
print(len(permutation_sub2('ABCDE')))

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
r = permutations('ABCD', 3)
#print(list(r))
print(len(list(r)))