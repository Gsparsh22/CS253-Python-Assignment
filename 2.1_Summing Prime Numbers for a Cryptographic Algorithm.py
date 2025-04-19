import math

def sum_of_primes(n):
    if n < 6:
        upper_bound = 16  # ensure enough primes for small n
    else:
        upper_bound = int(n * (math.log(n) + math.log(math.log(n)))) # upper bound used as mentioned by the TA for efficient complexity
    a = [True] * (upper_bound + 1)
    if upper_bound >= 0:
        a[0] = False
    if upper_bound >= 1:
        a[1] = False
    for i in range(2, int(math.sqrt(upper_bound)) + 1): # no need to check beyond the square root of the upper bound
        if a[i]:
            for j in range(i * i, upper_bound + 1, i):
                a[j] = False
    primes = []
    for i, is_prime in enumerate(a):
        if is_prime:
            primes.append(i)
            if len(primes) == n:
                break
    return sum(primes)

if __name__ == "__main__":
    n = int(input("Enter the number of primes to sum: "))
    if n ==1:
        print("The first prime is 2") # no sense of sum of 1 number, so just display the first prime
    else:
        print(f"Sum of first {n} primes:", sum_of_primes(n))