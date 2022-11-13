# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        depth_map = {}
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                if i in depth_map:
                    height += depth_map[i]
                    break
                else:
                    height += 1
                    i = self.parent[i]
            depth_map[vertex] = height
            maxHeight = max(maxHeight, height)
        return maxHeight


def main():
    tree = TreeHeight()
    tree.read()
    height = tree.compute_height()
    print(height)
    return height


threading.Thread(target=main).start()
