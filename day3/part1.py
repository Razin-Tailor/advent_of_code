"""
start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1
Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
"""


def main(data: list) -> int:
    data = [x.strip() for x in data]
    # starting at (0,0)
    row, col = 0, 0
    count = 0
    while row + 1 < len(data):
        row += 1
        col += 3
        place = data[row][col % len(data[row])]
        if place == "#":
            count += 1
    return count


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = f.readlines()
    count = main(data)
    print(count)
