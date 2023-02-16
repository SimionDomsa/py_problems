# def fibonacci_sum_recursive(n):  # todo v2
#     cache = {0: 0, 1: 1}  # sterge dictionarul asta, foloseste-te de un caz de baza in schimb
#     if n in cache:
#         return cache[n]
#     cache[n] = fibonacci_sum_recursive(n - 1) + fibonacci_sum_recursive(
#         n - 2)  # aici nu ai nevoie de un dictionar, poti returna direct rezultatul
#     return cache[n]
import math
# am sters dictionarul si la final am returnat rezultatul fara sa ma folosesc de cache
# def fibonacci_of(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_of(n - 1) + fibonacci_of(n - 2)


# number = fibonacci_of(20)
# print(number)


# def eratosthenes(n):
#     primes = list()
#     sieve = [True] * (n+1)
#     for p in range(2, n+1):
#         if sieve[p]:
#             primes.append(p)
#             for i in range(p, n+1, p):
#                 sieve[i] = False
#     return primes


# todo: testare
# daca un nr apartine sirului lui F. (0 nu apartine) (1 1 2 3 5 8 ...)

# iei continuu nr din sirul lui F
# din astea le folosesti doar pe primele N (100) care sunt prime
# apoi calculezi suma radicalului numerelor fara sqrt (cauti pe google alg)

# testezi ca sirul lui F iti da ce trebuie (cauti pe net val la o poz, si verifici ca alg iti da la fel)
# testezi alg de nr prime, ca sa iti returneze corect daca un nr e prim sau nu
# testezi pas interm. in care iei primele N nr din sirul lui F. si verifici ca nr de elemente prime este cel la care te astepti
# testezi func de calcul a radicalului (cu 2-3 edge case-uri)
# testezi integration toate functiile din alg


# functia de mai jos nu e precisa, am testat-o
#
# def find_sqrt(x):
#     if x < 2:
#         return x

#     y = x
#     z = (y + (x / y)) / 2

#     while abs(y - z) >= 0.0000000000000001:
#         y = z
#         z = (y + (x / y)) / 2

#     return z


from math import log2


def fibo_primes(user_input):
    lista_fibonacci_prime = [2, 3]
    a, b = 2, 3
    if user_input == 0:
        return []
    elif user_input == 1:
        return [2]
    elif user_input == 2:
        return [2, 3]
    else:
        while len(lista_fibonacci_prime) < user_input:
            if is_prime(a + b):
                lista_fibonacci_prime.append(a + b)
            a, b = b, a + b
    return lista_fibonacci_prime


def is_prime(n) -> bool:
    if type(n) != int:
        raise TypeError('n is of invalid type')
    if n < 0:
        raise ValueError('n must be a non-negative integer?')
    k = 0
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False


def fibonacci_list(n):
    f = [1, 1]
    if n < 0:
        raise ValueError('please insert a positive integer')
    elif n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        for i in range(2, n + 1):
            f.append(f[i - 1] + f[i - 2])
    return f[:-1]


# aici am incercat cu logaritm

def log_sqrt(n):
    x = pow(2, 0.5*log2(n))
    return x


def sum_of_primes_sqrt():
    suma = 0
    for number in fibo_primes(user_input):
        suma = + log_sqrt(number)
    return suma


# user_input = int(input("How many prime numbers from the Fibonacci sequence do you want to add the sum of their square roots? "))


# first 10 prime numbers from the fibonacci sequence: 2 3 5 13 89 233 1597 28657 514229 433494437


# print(fibonacci_list(100))

# print('The numbers are: ')
# for prime in fibo_primes(user_input):
#     print(prime, end=' ')
# print('\nThe sum of their sqare roots is: ')
# print(sum_of_primes_sqrt())
