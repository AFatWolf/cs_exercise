def factorize(n):
    isPrime = [1] * (n+1)
    PrimeFactor = []
    for i in range(2, n+1):
        if (isPrime[i]):
            for j in range(i*i, n+1, i):
                isPrime[j] = False
            j = i
            while (n % j == 0):
                PrimeFactor.append(i)
                j*=i
    return PrimeFactor
print(factorize(48))
print(factorize(21))
print(factorize(22))
print(factorize(23))


