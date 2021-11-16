from itertools import islice

def gen_prime(n):
    primes = [2]
    next_prime = 3
    while next_prime < n:
        isPrime = True

        i = 0

        squareRoot = int(next_prime ** 0.5)

        while primes[i] <= squareRoot:
             if next_prime % primes[i] == 0:
                 isPrime = False

             i += 1
        if isPrime:
            primes.append(next_prime)
        next_prime += 1
    print(primes)

if __name__ == "__main__":
    gen_prime(200)