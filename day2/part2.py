"""
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

"""


def is_valid(low, high, charac, password):
    """
    The charac should appear (low, high) times in the password
    """
    char_at_low = password[low - 1]
    char_at_high = password[high - 1]

    if (char_at_low == charac and char_at_high != charac) or (
        char_at_high == charac and char_at_low != charac
    ):
        return True
    else:
        return False


def parse(data_string):
    condition, password = data_string.split(": ")
    limit, character = condition.split(" ")
    low, high = limit.split("-")
    return int(low), int(high), character, password


def main(data):
    count = 0
    for d in data:
        low, high, charac, password = parse(d)
        if is_valid(low, high, charac, password):
            count += 1
        else:
            pass
    return count


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = f.readlines()
    count = main(data)
    print(count)