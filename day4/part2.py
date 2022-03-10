import re

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
ALLOWED_ECL = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_byr(val: str) -> bool:
    if len(val) == 4 and (1920 <= int(val) <= 2002):
        return True
    else:
        return False


def is_valid_iyr(val: str) -> bool:
    if len(val) == 4 and (2010 <= int(val) <= 2020):
        return True
    else:
        return False


def is_valid_eyr(val: str) -> bool:
    if len(val) == 4 and (2020 <= int(val) <= 2030):
        return True
    else:
        return False


def is_valid_hgt(val: str) -> bool:
    if "cm" in val and 150 <= int(val[:-2]) <= 193:
        return True
    elif "in" in val and 59 <= int(val[:-2]) <= 76:
        return True
    else:
        return False


def is_valid_hcl(val: str) -> bool:
    exp = r"#(?:[a-f\d]{3}){1,2}\b"
    matched = re.match(exp, val)
    return bool(matched)


def is_valid_ecl(val: str) -> bool:
    return True if val in ALLOWED_ECL else False


def is_valid_pid(val: str) -> bool:
    exp = r"^0*\d{9}$"
    matched = re.match(exp, val)
    print("PID REGEX", bool(matched))
    return bool(matched)


def is_valid_cid(val: str) -> bool:
    return True


IS_KEY_VALID = {
    "byr": is_valid_byr,
    "iyr": is_valid_iyr,
    "eyr": is_valid_eyr,
    "hgt": is_valid_hgt,
    "hcl": is_valid_hcl,
    "ecl": is_valid_ecl,
    "pid": is_valid_pid,
    "cid": is_valid_cid,
}


def make_data(parsed: list) -> list:
    passport_list = []
    for d in parsed:
        passport = []
        split_new_line = d.split("\n")
        for info in split_new_line:
            kv = info.split(" ")
            passport.extend(kv)

        passport_list.append(passport)
    print(f"{passport_list=}")
    to_return = []
    for passport in passport_list:
        passport_dict = {}
        for data in passport:
            splitted = data.split(":")
            passport_dict[splitted[0]] = splitted[1]
        to_return.append(passport_dict)
    print(f"{to_return=}")
    return to_return


def is_valid(passport: dict) -> bool:
    not_found = [x for x in NEEDED_KEYS if x not in passport.keys()]
    if len(not_found) == 0 or (
        len(not_found) == 1 and not_found[0] == OPTIONAL_KEY
    ):
        for key, value in passport.items():
            print(f"{key=}\t{value=}\n")
            if not IS_KEY_VALID[key](value):
                return False
        return True
    else:
        return False


def main(data: list) -> int:
    valid_passports = 0
    parsed = data.split("\n\n")
    passports_to_check = make_data(parsed)
    for passport in passports_to_check:
        print("passport to check")
        print(passport)
        if is_valid(passport):
            valid_passports = valid_passports + 1
    return valid_passports


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        data = f.read()
    count = main(data)
    print(count)
