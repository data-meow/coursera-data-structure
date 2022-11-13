# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    height_map = {} # store height of processed node to avoid duplicate work
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            if current not in height_map:
                height += 1
                current = parents[current]
            else:
                height += height_map[current]
                break
        height_map[vertex] = height
        max_height = max(max_height, height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    height = compute_height(n, parents)
    print(height)
    return height


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
