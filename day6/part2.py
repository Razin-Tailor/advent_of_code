import functools


def main(data: str) -> int:
    parsed = data.split("\n\n")
    print(parsed)
    sum = 0
    for group in parsed:
        splitted = group.split("\n")
        if len(splitted) == 1:
            sum = sum + len(splitted[0])
        else:
            setted = [set(x) for x in splitted]
            print(f"{setted=}")
            reduced = functools.reduce(lambda x, y: x.intersection(y), setted)
            # for item in splitted:
            print(f"{reduced=}")
            sum = sum + len(reduced)
        # set_splitted = set(list(splitted))
        # print(f"{set_splitted=}")
        # sum = sum + len(set_splitted)
    return sum


if __name__ == "__main__":

    with open("data.txt", "r") as f:
        data = f.read()

    sum_yes = main(data)
    print(sum_yes)
