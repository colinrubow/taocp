def product_a(perm_prod: list[int]) -> list[int]:
    """
    TAOCP 1.3.3 performs a permutation product with multiple passes

    a permutation is represented as in this example: ['(', 'a', 'c', 'd', ')', '(', 'd', 'c', 'e', ')']
    but not that all elements should be their ascii code, rather than a str
    """
    # constants of str to ascii ints
    LPREN = ord('(')
    RPREN = ord(')')

    tag_array = [0]*len(perm_prod)

    # First pass
    char_temp = 0
    for i, char in enumerate(perm_prod):
        if char == LPREN:
            tag_array[i] = 1
            char_temp = perm_prod[i+1]
        elif char == RPREN:
            perm_prod[i] = char_temp
            tag_array[i] = 1

    output = []
    index = 0

    while 0 in tag_array:
        index = tag_array.index(0)
        start = perm_prod[index]
        output.append(LPREN)
        output.append(start)
        tag_array[index] = 1

        index += 1
        current = perm_prod[index]
        while current != start:
            # follow the permutations till we hit start again
            index += 1
            while index < len(perm_prod) - 1:
                # follow the permutation
                if perm_prod[index] == current:
                    tag_array[index] = 1
                    index += 1
                    current = perm_prod[index]
                index += 1
            # at end of expression
            if current != start:
                output.append(current)
                index = 0
        output.append(RPREN)

    return output

def product_b(perm_prod: list[int]) -> list[int]:
    """
    TAOCP 1.3.3 performs a permutation product with a single pass

    see notes for product_a
    """
    # constants of str to ascii ints
    LPREN = ord('(')
    RPREN = ord(')')

    aux_table = []

    perm_prod.reverse()

    z = 0
    j = 0
    for element in perm_prod:
        if element == RPREN:
            z = 0
        elif element == LPREN:
            aux_table[j] = z
        else:
            if element not in aux_table:
                aux_table.append(element)
            element_index = aux_table.index(element)
            z, aux_table[element_index] = aux_table[element_index], z
            if aux_table[element_index] == 0:
                j = element_index



if __name__ == '__main__':
    # unit tests
    permutation = ['(', 'a', 'b', 'c', ')', '(', 'b', 'c', 'a', ')', '(', 'c', 'a', 'b', ')']
    permutation = [ord(char) for char in permutation]
    prod = product_a(permutation)
    prod = [chr(char) for char in prod]
    assert prod == ['(', 'a', ')', '(', 'b', ')', '(', 'c', ')'], f'test 0 failed: {prod}'

    permutation = ['(', 'a', 'c', 'f', 'g', ')', '(', 'b', 'c', 'd', ')', '(', 'a', 'e', 'd', ')', '(', 'f', 'a', 'd', 'e', ')', '(', 'b', 'g', 'f', 'a', 'e', ')']
    permutation = [ord(char) for char in permutation]
    prod = product_a(permutation)
    prod = [chr(char) for char in prod]
    assert prod == ['(', 'a', 'd', 'g', ')', '(', 'c', 'e', 'b', ')', '(', 'f', ')'], f'test 1 failed: {prod}'

    permutation = ['(', 'a', 'b', ')', '(', 'b', 'c', ')', '(', 'c', 'a', ')']
    permutation = [ord(char) for char in permutation]
    prod = product_a(permutation)
    prod = [chr(char) for char in prod]
    assert prod == ['(', 'a', ')', '(', 'b', 'c', ')'], f'test 2 failed: {prod}'

    permutation = ['(', 'x', 'y', ')', '(', 'a', 'b', 'c', ')', '(', 'y', 'z', ')', '(', 'b', 'x', ')']
    permutation = [ord(char) for char in permutation]
    prod = product_a(permutation)
    prod = [chr(char) for char in prod]
    assert prod == ['(', 'x', 'z', 'y', 'b', 'c', 'a', ')'], f'test 3 failed: {prod}'

    print('all tests passed\n')

    # Performance analysis
    import time
    import random

    def generate_random_permutation_product(n):
        """Generate a random permutation product with n elements"""
        # Create a list of n unique elements (using ASCII codes starting from 'a')
        elements = list(range(ord('a'), ord('a') + n))
        result = [LPREN]

        # Create random cycles
        remaining = elements.copy()
        while remaining:
            # Random cycle length (at least 1, at most remaining elements)
            cycle_len = random.randint(1, min(5, len(remaining)))
            cycle = random.sample(remaining, cycle_len)

            if len(result) > 1:
                result.append(LPREN)

            result.extend(cycle)
            result.append(RPREN)

            for elem in cycle:
                remaining.remove(elem)

        return result

    LPREN = ord('(')
    RPREN = ord(')')

    for size in [10, 100, 1000]:
        times = []
        num_trials = 100

        for _ in range(num_trials):
            perm_prod = generate_random_permutation_product(size)

            start_time = time.perf_counter()
            product_a(perm_prod)
            end_time = time.perf_counter()

            times.append(end_time - start_time)

        avg_time = sum(times) / len(times)
        print(f"Size {size}: Average time = {avg_time*1000:.4f} ms ({num_trials} trials)")

    # Size 10: Average time = 0.0117 ms (100 trials)
    # Size 100: Average time = 0.9217 ms (100 trials)
    # Size 1000: Average time = 124.1438 ms (100 trials)
