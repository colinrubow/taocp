import numpy as np


def get_min(array: np.ndarray) -> tuple[int, int]:
    """
    returns the min value and indice
    """
    min = array[0]
    min_i = 0
    for i, a in enumerate(array):
        if a < min:
            min = a
            min_i = i
    return min, min_i

def get_saddle_point(m: np.ndarray) -> tuple[int, int]:
    """
    returns the saddle point indices of the matrix. Min row, max column
    """
    row = 0
    another = False
    column = 0
    while row < len(m):
        if not another:
            row_min, column = get_min(m[row])
        column_max = max(m[:,column])
        if m[row][column] == column_max:
            return row, column
        else:
            # see if there's another min in the row
            i = column + 1
            another = False
            while i < len(m[row]):
                if m[row][i] == row_min:
                    column = i
                    another = True
                    break
                i += 1
            if another:
                continue
            else:
                row += 1
    return -1, -1

def get_saddle_point_exhaustive(m: np.ndarray) -> tuple[int, int]:
    """
    see previous
    """
    for i, row in enumerate(m):
        for j, entry in enumerate(row):
            if entry == min(row) and entry == max(m[:,j]):
                return i, j
    return -1, -1

if __name__ == '__main__':
    m = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    r, c = get_saddle_point(m)
    assert r == 2 and c == 0, f"get_saddle_point failed test 1: r = {r}, c = {c}"
    r, c = get_saddle_point_exhaustive(m)
    assert r == 2 and c == 0, f"get_saddle_point_exhaustive failed test 1: r = {r}, c = {c}"

    m = np.array([
        [1, 2, 3],
        [4, 3, 5],
        [6, 2, 8]
    ])
    r, c = get_saddle_point(m)
    assert r == 1 and c == 1, f"failed test 2: r = {r}, c = {c}"
    r, c = get_saddle_point_exhaustive(m)
    assert r == 1 and c == 1, f"get_saddle_point_exhaustive failed test 2: r = {r}, c = {c}"

    m = np.array([
        [1, 2, 3, 4]
    ])
    r, c = get_saddle_point(m)
    assert r == 0 and c == 0, f"failed test 3: r = {r}, c = {c}"
    r, c = get_saddle_point_exhaustive(m)
    assert r == 0 and c == 0, f"get_saddle_point_exhaustive failed test 3: r = {r}, c = {c}"

    m = np.array([
        [1],
        [2],
        [3],
        [4]
    ])
    r, c = get_saddle_point(m)
    assert r == 3 and c == 0, f"failed test 4: r = {r}, c = {c}"
    r, c = get_saddle_point_exhaustive(m)
    assert r == 3 and c == 0, f"get_saddle_point_exhaustive failed test 4: r = {r}, c = {c}"

    m = np.array([
        [1, 2, 3],
        [6, 5, 6],
        [3, 8, 9]
    ])
    r, c = get_saddle_point(m)
    assert r == -1 and c == -1, f"failed test 5: r = {r}, c = {c}"
    r, c = get_saddle_point_exhaustive(m)
    assert r == -1 and c == -1, f"get_saddle_point_exhaustive failed test 5: r = {r}, c = {c}"

    m = np.array([
        [5]
    ])
    r, c = get_saddle_point(m)
    assert r == 0 and c == 0, f"failed test 6: r = {r}, c = {c}"
    r, c = get_saddle_point_exhaustive(m)
    assert r == 0 and c == 0, f"get_saddle_point_exhaustive failed test 6: r = {r}, c = {c}"

    m = -np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    r, c = get_saddle_point(m)
    assert r == 0 and c == 3, f"failed test 7: r = {r}, c = {c}"
    r, c = get_saddle_point_exhaustive(m)
    assert r == 0 and c == 3, f"get_saddle_point_exhaustive failed test 7: r = {r}, c = {c}"

    m = np.array([
        [69, 50, 14],
        [18, 88, 18],
        [93, 13, 47]
    ])
    r, c = get_saddle_point(m)
    assert r == -1 and c == -1, f"failed test 8: r = {r}, c = {c}"
    r, c = get_saddle_point_exhaustive(m)
    assert r == -1 and c == -1, f"get_saddle_point_exhaustive failed test 8: r = {r}, c = {c}"

    print('Passed all tests')

    # time analysis
    import time

    print("\n" + "="*60)
    print("TIME ANALYSIS - get_saddle_point function")
    print("="*60)

    test_cases = [
        (3, 3),
        (5, 5),
        (10, 10),
        (100, 100),
        (1000, 1000)
    ]

    iterations = 1000

    for rows, cols in test_cases:
        total_time = 0

        for _ in range(iterations):
            # Generate random matrix
            matrix = np.random.randint(0, 100, size=(rows, cols))

            # Time the function
            start = time.perf_counter()
            get_saddle_point_exhaustive(matrix)
            end = time.perf_counter()

            total_time += (end - start)

        avg_time = total_time / iterations
        print(f"\n{rows}x{cols} matrix:")
        print(f"  Average time: {avg_time*1000:.6f} ms")
        print(f"  Total time for {iterations} iterations: {total_time:.6f} s")

# Time analysis for get_saddle_point
#
# 3x3 matrix:
#   Average time: 0.008155 ms
#   Total time for 1000 iterations: 0.008155 s
#
# 5x5 matrix:
#   Average time: 0.017154 ms
#   Total time for 1000 iterations: 0.017154 s
#
# 10x10 matrix:
#   Average time: 0.046064 ms
#   Total time for 1000 iterations: 0.046064 s
#
# 100x100 matrix:
#   Average time: 2.858636 ms
#   Total time for 1000 iterations: 2.858636 s
#
# 1000x1000 matrix:
#   Average time: 889.043355 ms
#   Total time for 1000 iterations: 889.043355 s

# Time analysis for get_saddle_point_exhaustive
# 3x3 matrix:
#   Average time: 0.010151 ms
#   Total time for 1000 iterations: 0.010151 s
#
# 5x5 matrix:
#   Average time: 0.027633 ms
#   Total time for 1000 iterations: 0.027633 s
#
# 10x10 matrix:
#   Average time: 0.109199 ms
#   Total time for 1000 iterations: 0.109199 s
#
# 100x100 matrix:
#   Average time: 33.982236 ms
#   Total time for 1000 iterations: 33.982236 s
