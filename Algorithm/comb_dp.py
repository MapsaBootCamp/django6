def comb(n, k, cache={}):
    if n < k:
        raise Exception("shab bekheir!")

    elif k == 0 or n == k:
        return 1

    if (n, k) in cache:
        return cache[(n, k)]

    else:
        temp = comb(n-1, k-1) + comb(n-1, k)
        print(cache)
        cache[(n, k)] = temp
        return temp


print(comb(5, 2))
print(comb(2, 0))