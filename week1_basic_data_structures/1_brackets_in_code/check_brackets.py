# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_brackets_index = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            opening_brackets_index.append(i+1)

        if next in ")]}":
            # Process closing bracket, write your code here
            # When opening_brackets_stack is empty, report error directly
            if not opening_brackets_stack:
                return i+1
            # When opening_brackets_stack is not empty but doesn't match with last opening left bracket,
            # report error as well
            last_open_left = opening_brackets_stack.pop()
            opening_brackets_index.pop()
            if not are_matching(last_open_left, next):
                return i+1
    # After loop through the text, check if any remaining open bracket before report success
    if len(opening_brackets_stack) > 0:
        return opening_brackets_index.pop()
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)
    return mismatch


if __name__ == "__main__":
    main()