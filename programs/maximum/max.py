def taocp_max(nums: list[int]) -> tuple[int, int]:
    """
    TAOCP 1.3.2
    returns the max of the given list and the highest index of that maximal


    performs in O(n)
    """
    # M1 Initialize
    max_index = len(nums) - 1
    next_index = len(nums) - 2
    max = nums[max_index]

    # M2 All tested?
    while next_index >= 0:
        # M3 Compare
        if max < nums[next_index]:
            # M4 Change m
            max_index = next_index
            max = nums[max_index]

        # M5 Decrease next_index
        next_index -= 1

    return max, max_index

def pythonic_max(nums: list[int]) -> tuple[int, int]:
    maximum = max(nums)
    nums.reverse()
    return maximum, len(nums) - 1 - nums.index(maximum)

if __name__ == '__main__':
    import time
    import random
    from numpy import mean

    # unit tests
    nums = [1, 2, 3, 4, 5]
    m, j = taocp_max(nums)
    assert m == 5 and j == 4, f"taocp failed test 1 (m={m}, j={j})"
    m, j = pythonic_max(nums)
    assert m == 5 and j == 4, f"pythonic failed test 1 (m={m}, j={j})"

    nums = [10, 5, 3, 2, 1]
    m, j = taocp_max(nums)
    assert m == 10 and j == 0, f"taocp failed test 2 (m={m}, j={j})"
    m, j = pythonic_max(nums)
    assert m == 10 and j == 0, f"pythonic failed test 2 (m={m}, j={j})"

    nums = [3, 7, 2, 9, 9, 4]
    m, j = taocp_max(nums)
    assert m == 9 and j == 4, f"taocp failed test 3 (m={m}, j={j})"
    m, j = pythonic_max(nums)
    assert m == 9 and j == 4, f"pythonic failed test 3 (m={m}, j={j})"

    nums = [42]
    m, j = taocp_max(nums)
    assert m == 42 and j == 0, f"taocp failed test 4 (m={m}, j={j})"
    m, j = pythonic_max(nums)
    assert m == 42 and j == 0, f"pythonic failed test 4 (m={m}, j={j})"

    nums = [-5, -10, -3, -8]
    m, j = taocp_max(nums)
    assert m == -3 and j == 2, f"taocp failed test 5 (m={m}, j={j})"
    m, j = pythonic_max(nums)
    assert m == -3 and j == 2, f"pythonic failed test 5 (m={m}, j={j})"

    print('All unit tests passed\n')

    times_taocp = []
    times_pythonic = []
    for _ in range(1000):
        nums = [random.randint(0, 1000) for _ in range(10000)]

        now = time.time()
        taocp_max(nums)
        times_taocp.append(time.time() - now)

        now = time.time()
        pythonic_max(nums)
        times_pythonic.append(time.time() - now)

    print(f'TAOCP average time: {mean(times_taocp)} (sec)')
    print(f'Pythonic average time: {mean(times_pythonic)} (sec)')
