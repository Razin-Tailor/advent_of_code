def main(data: str) -> int:
    parsed = data.split("\n\n")
    print(parsed)
    sum = 0
    for group in parsed:
        splitted = "".join(group.split("\n"))
        set_splitted = set(list(splitted))
        print(f"{set_splitted=}")
        sum = sum + len(set_splitted)
    return sum


if __name__ == "__main__":

    with open("data.txt", "r") as f:
        data = f.read()

    sum_yes = main(data)
    print(sum_yes)
