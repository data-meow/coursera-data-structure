#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__stack_max = []

    def Push(self, a):
        self.__stack.append(a)
        if not self.__stack_max:
            self.__stack_max.append(a)
        else:
            self.__stack_max.append(max(a, self.__stack_max[-1]))

    def Pop(self):
        assert(len(self.__stack) > 0)
        p_val = self.__stack.pop()
        if p_val == self.__stack_max[-1]:
            self.__stack_max.pop()

    def Max(self):
        assert(len(self.__stack) > 0)
        return self.__stack_max[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
