import prime_sqrt


def test_fibo_primes():
    assert [2, 3, 5, 13, 89, 233, 1597] == prime_sqrt.fibo_primes(7)