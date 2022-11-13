# python3
# import sys
# sys.path.insert(1, '../4_stack_with_max')
# import stack_with_max_naive


def max_sliding_window_naive(sequence, m):
    maximums = []
    memory = []
    for i, val in enumerate(sequence):
        while (len(memory) > 0) and (val > memory[-1]):
            memory.pop()
        memory.append(val)
        if i >= (m - 1):
            maximums.append(memory[0])
            if sequence[i-m+1] == memory[0]:
                memory.pop(0)
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

