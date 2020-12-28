"""
Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.
"""


def is_valid(low, high, charac, password):
    """
    The charac should appear (low, high) times in the password
    """
    if charac not in password:
        return False
    else:
        count_charac = password.count(charac)
        if low <= count_charac <= high:
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