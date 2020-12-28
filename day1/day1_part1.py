import sys

"""

Specifically, they need you to find the two entries that sum to 2020 
and then multiply those two numbers together

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. 
Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
"""


def get_numbers(data):
    for num in data:
        diff = 2020 - num
        if diff in data:
            return num, diff
    return 0, 0


def main(data):
    n1, n2 = get_numbers(data)
    return n1 * n2


if __name__ == "__main__":
    with open("day_1_part1.txt", "r") as f:
        data = f.readlines()
    data = [int(x.strip()) for x in data]
    result = main(data)
    print(result)