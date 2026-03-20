def list_primes(num_primes: int) -> list[int]:
    """
    TAOCP 1.3.2 returns a list of first num_primes primes
    """
    if num_primes == 1:
        return [2]

    # initialize
    primes = [2, 3]
    num = 3
    num_found = 2

    while num_found < num_primes:
        num += 2
        prime_index = 1

        while True:
            div = num/primes[prime_index]
            # num is multiple of found prime
            if div%1 == 0:
                num += 2
                prime_index = 1
                continue

            # found a prime
            if div//1 <= primes[prime_index]:
                break

            prime_index += 1

        # found a prime
        primes.append(num)
        num_found += 1

    return primes


if __name__ == "__main__":
    # unit tests
    assert list_primes(1) == [2], "First prime should be 2"
    assert list_primes(5) == [2, 3, 5, 7, 11], "First 5 primes should be [2, 3, 5, 7, 11]"
    print("all tests pass\n")

    # print 500 primes, 10 columns of 50 numbers each
    primes = list_primes(500)
    print('FIRST FIVE HUNDRED PRIMES')
    for i in range(50):
        buffer = [primes[i + m*50] for m in range(10)]
        print(' '.join(f"{num:5d}" for num in buffer))

    # time it
    print()
    import time

    for exp in range(7):
        now = time.time()
        list_primes(10**exp)
        click = time.time() - now
        print(f'first 10^{exp} primes: {click} (sec)')

    # first 10^0 primes: 0.0 (sec)
    # first 10^1 primes: 0.0 (sec)
    # first 10^2 primes: 0.0 (sec)
    # first 10^3 primes: 0.0 (sec)
    # first 10^4 primes: 0.07808589935302734 (sec)
    # first 10^5 primes: 2.276947021484375 (sec)
    # first 10^6 primes: 63.577624797821045 (sec)
