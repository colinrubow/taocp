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

def inverse_j(perm: list[int]) -> None:
    """
    TAOCP 1.3.3 find the inverse permuation in place
    The input perm is the integers from 1 to len(perm) (notice indexing by 1)
    """
    for i, element in enumerate(perm):
        perm[i] = -element
    for m in range(len(perm), 0, -1):
        j = m
        i = perm[j - 1]
        while i > 0:
            j = i
            i = perm[j - 1]
        perm[j - 1] = perm[-i - 1]
        perm[-i - 1] = m
        m -= 1

def inverse_copy(perm: list[int]) -> list[int]:
    """
    finds the inverse permutation and returns a copy
    The input perm is the integers from 1 to len(perm) (notice indexing by 1)
    """
    inv_perm = [0]*len(perm)
    for i, val in enumerate(perm):
        inv_perm[val - 1] = i + 1
    return inv_perm

if __name__ == '__main__':
    # unit tests
    perm = [6, 2, 1, 5, 4, 3]
    perm_copy = inverse_copy(perm)
    perm_j = perm.copy()
    inverse_i(perm)
    inverse_j(perm_j)
    assert perm_copy == [3, 2, 6, 5, 4, 1], f'inverse_copy failed test 1: {perm_copy}'
    assert perm == [3, 2, 6, 5, 4, 1], f'inverse_i failed test 1: {perm}'
    assert perm_j == [3, 2, 6, 5, 4, 1], f'inverse_j failed test 1: {perm_j}'

    perm = [1]
    perm_copy = inverse_copy(perm)
    perm_j = perm.copy()
    inverse_i(perm)
    inverse_j(perm_j)
    assert perm_copy == [1], f'inverse_copy failed test 2: {perm_copy}'
    assert perm == [1], f'inverse_i failed test 2: {perm}'
    assert perm_j == [1], f'inverse_j failed test 2: {perm_j}'

    perm = [2, 1]
    perm_copy = inverse_copy(perm)
    perm_j = perm.copy()
    inverse_i(perm)
    inverse_j(perm_j)
    assert perm_copy == [2, 1], f'inverse_copy failed test 3: {perm_copy}'
    assert perm == [2, 1], f'inverse_i failed test 3: {perm}'
    assert perm_j == [2, 1], f'inverse_j failed test 3: {perm_j}'

    perm = [2, 3, 4, 1]
    perm_copy = inverse_copy(perm)
    perm_j = perm.copy()
    inverse_i(perm)
    inverse_j(perm_j)
    assert perm_copy == [4, 1, 2, 3], f'inverse_copy failed test 4: {perm_copy}'
    assert perm == [4, 1, 2, 3], f'inverse_i failed test 4: {perm}'
    assert perm_j == [4, 1, 2, 3], f'inverse_j failed test 4: {perm_j}'

    perm = [5, 4, 3, 2, 1]
    perm_copy = inverse_copy(perm)
    perm_j = perm.copy()
    inverse_i(perm)
    inverse_j(perm_j)
    assert perm_copy == [5, 4, 3, 2, 1], f'inverse_copy failed test 5: {perm_copy}'
    assert perm == [5, 4, 3, 2, 1], f'inverse_i failed test 5: {perm}'
    assert perm_j == [5, 4, 3, 2, 1], f'inverse_j failed test 5: {perm_j}'

    perm = [1, 2, 3, 4, 5]
    perm_copy = inverse_copy(perm)
    perm_j = perm.copy()
    inverse_i(perm)
    inverse_j(perm_j)
    assert perm_copy == [1, 2, 3, 4, 5], f'inverse_copy failed test 6: {perm_copy}'
    assert perm == [1, 2, 3, 4, 5], f'inverse_i failed test 6: {perm}'
    assert perm_j == [1, 2, 3, 4, 5], f'inverse_j failed test 6: {perm_j}'

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
            inverse_copy(perm)
            end = time.perf_counter()
            total_time += (end - start)
        avg_time = total_time / trials
        print(f'Size {size:5d}: avg time = {avg_time*1e6:8.3f} microseconds ({trials} trials)')

# speed analysis of inverse_i
# Size    10: avg time =    1.554 microseconds (1000 trials)
# Size   100: avg time =   13.749 microseconds (1000 trials)
# Size  1000: avg time =  195.322 microseconds (1000 trials)
# Size 10000: avg time = 2141.008 microseconds (1000 trials)

# speed anaysis of inverse_j
# Size    10: avg time =    1.771 microseconds (1000 trials)
# Size   100: avg time =   18.601 microseconds (1000 trials)
# Size  1000: avg time =  360.661 microseconds (1000 trials)
# Size 10000: avg time = 4658.025 microseconds (1000 trials)

# speed analysis of inverse_copy
# Size    10: avg time =    0.669 microseconds (1000 trials)
# Size   100: avg time =    3.408 microseconds (1000 trials)
# Size  1000: avg time =   57.802 microseconds (1000 trials)
# Size 10000: avg time =  580.852 microseconds (1000 trials)
