slope_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def main(data: list) -> int:
    data = [x.strip() for x in data]
    # starting at (0,0)
    mult = 1
    for slope in slope_list:
        row, col = 0, 0
        count = 0
        while row + 1 < len(data):
            row += slope[1]
            col += slope[0]
            place = data[row][col % len(data[row])]
            if place == "#":
                count += 1
        mult *= count
    return mult


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = f.readlines()
    count = main(data)
    print(count)
