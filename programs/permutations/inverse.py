def inverse_i(perm: list[int]) -> None:
    """
    TAOCP 1.3.3 finds the inverse permutation, in place.
    The input perm, is the integers from 1 to len(perm) (notice indexing by 1)
    """
    current = len(perm)
    prev = -1
    while current > 0:
        next = perm[current - 1]
        # already adjusted
        if next < 0:
            perm[current - 1] *= -1
            current -= 1
            continue
        perm[current - 1] = prev
        prev = -current
        current = next
        next = perm[current - 1]
        if next < 0:
            next = prev
            perm[current - 1] = -next
            current -= 1
            continue


if __name__ == '__main__':
    # unit tests
    perm = [6, 2, 1, 5, 4, 3]
    inverse_i(perm)
    assert perm == [3, 2, 6, 5, 4, 1], f'inverse_i failed test 1: {perm}'

    perm = [1]
    inverse_i(perm)
    assert perm == [1], f'inverse_i failed test 2: {perm}'

    perm = [2, 1]
    inverse_i(perm)
    assert perm == [2, 1], f'inverse_i failed test 3: {perm}'

    perm = [2, 3, 4, 1]
    inverse_i(perm)
    assert perm == [4, 1, 2, 3], f'inverse_i failed test 4: {perm}'

    perm = [5, 4, 3, 2, 1]
    inverse_i(perm)
    assert perm == [5, 4, 3, 2, 1], f'inverse_i failed test 5: {perm}'

    perm = [1, 2, 3, 4, 5]
    inverse_i(perm)
    assert perm == [1, 2, 3, 4, 5], f'inverse_i failed test 6: {perm}'

    print('all tests passed')

    # speed analysis
    import random
    import time

    sizes = [10, 100, 1000, 10000]
    trials = 1000

    print('\nSpeed Analysis:')
    for size in sizes:
        total_time = 0
        for _ in range(trials):
            perm = list(range(1, size + 1))
            random.shuffle(perm)
            start = time.perf_counter()
            inverse_i(perm)
            end = time.perf_counter()
            total_time += (end - start)
        avg_time = total_time / trials
        print(f'Size {size:5d}: avg time = {avg_time*1e6:8.3f} microseconds ({trials} trials)')

# speed analysis of inverse_i
# Size    10: avg time =    1.554 microseconds (1000 trials)
# Size   100: avg time =   13.749 microseconds (1000 trials)
# Size  1000: avg time =  195.322 microseconds (1000 trials)
# Size 10000: avg time = 2141.008 microseconds (1000 trials)
