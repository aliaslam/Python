# Implementation of the Sieve of Eratosthenes:  Algorithm for finding all prime numbers up to n

def primes_sieve(n):
    nn = n + 1
    potential_primes = [True] * nn
    primes = []

    for i in range(2, nn):
        if potential_primes[i] == False:
            continue

        for j in range(i*2, nn, i):
            potential_primes[j] = False

        primes.append(i)
    
    return primes

print(primes_sieve(10000))

