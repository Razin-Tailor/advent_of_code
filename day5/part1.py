import math


ROWS = 128
COLUMNS = 8


def get_seat_id(row: int, col: int) -> int:
    return row * 8 + col


def get_row(row_seq: str) -> int:
    """
    Given a seq of FBFBFB return a row in the plane
    F means take lower half
    B means take upper half

    Args:
        row_seq (str): sequence of FBFBF

    Returns:
        int: row of plane
    """
    # print(f"{row_seq=}")
    min_row = 0
    max_row = 127
    for step in row_seq:
        if step == "F":
            max_row = math.floor((min_row + max_row) / 2)
        elif step == "B":
            min_row = math.ceil((min_row + max_row) / 2)
        # print(f"Range is {min_row} : {max_row}")
    # print(f"{min_row=} {max_row=}")
    if min_row == max_row:
        return min_row


def get_col(col_seq: str) -> int:
    """
    Given a seq of LR return a column in the plane
    L means take lower half
    R means take upper half

    Args:
        col_seq (str): sequence of LR

    Returns:
        int: column of plane
    """
    # print(f"{col_seq=}")
    min_col = 0
    max_col = 7
    for step in col_seq:
        if step == "L":
            max_col = math.floor((min_col + max_col) / 2)
        elif step == "R":
            min_col = math.ceil((min_col + max_col) / 2)
        # print(f"Range is {min_col} : {max_col}")
    # print(f"{min_col=} {max_col=}")
    if min_col == max_col:
        return min_col


def main(data: list) -> int:
    seat_id_list = []
    for position in data:
        position = position.strip()
        row_seq = position[:-3]
        col_seq = position[-3:]

        row = get_row(row_seq)
        col = get_col(col_seq)
        seat_id = get_seat_id(row, col)
        # print(f"{seat_id=}")
        seat_id_list.append(seat_id)
    return max(seat_id_list)


if __name__ == "__main__":
    # answer max(567, 119, 820) => 820
    with open("data.txt", "r") as f:
        data = f.readlines()
    # print(data)
    max_seat_id = main(data)
    print(max_seat_id)
