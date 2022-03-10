NEEDED_KEYS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
]
OPTIONAL_KEY = "cid"


def make_data(parsed: list) -> list:
    passport_list = []
    for d in parsed:
        passport = []
        split_new_line = d.split("\n")
        for info in split_new_line:
            kv = info.split(" ")
            passport.extend(kv)

        passport_list.append(passport)

    key_list_passport = []
    for passport in passport_list:
        cleaned = [x.split(":")[0] for x in passport]
        key_list_passport.append(cleaned)

    return key_list_passport


def main(data: list) -> int:
    valid_passports = 0
    parsed = data.split("\n\n")
    passports_to_check = make_data(parsed)
    for passport in passports_to_check:
        not_found = [x for x in NEEDED_KEYS if x not in passport]
        if len(not_found) == 0 or (
            len(not_found) == 1 and not_found[0] == OPTIONAL_KEY
        ):
            valid_passports = valid_passports + 1
    return valid_passports


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = f.read()
    count = main(data)
    print(count)
