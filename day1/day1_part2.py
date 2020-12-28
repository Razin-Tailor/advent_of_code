import sys

"""

find three numbers in your expense report that meet the same criteria.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

x + y + z = 2020
y + z = 2020 - x

2020 - x = P

y + z = P


"""


def get_numbers(data, curr_sum):
    for num in data:
        diff = curr_sum - num
        if diff in data:
            return num, diff
    return 0, 0


def get_three_numbers(data):
    for x in data:
        y_z = 2020 - x
        y, z = get_numbers(data, y_z)
        if y != 0 and z != 0:
            return x, y, z
    return 0, 0, 0


def main(data):
    n1, n2, n3 = get_three_numbers(data)
    return n1 * n2 * n3


if __name__ == "__main__":
    with open("day_1_part1.txt", "r") as f:
        data = f.readlines()
    data = [int(x.strip()) for x in data]
    result = main(data)
    print(result)