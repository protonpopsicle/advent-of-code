#!/usr/bin/env python3

import sys

file_content = None
invalid_id_sum = 0


def consecutive_occurance_count(s, sub_str):
    sub_len = len(sub_str)
    chunks = [s[i : i + sub_len] for i in range(0, len(s), sub_len)]
    if all(chunk == sub_str for chunk in chunks):
        return len(chunks)
    return 0


def valid_id(num_str):
    substrings = []
    for x in range(len(num_str) // 2):
        substrings.append(num_str[: x + 1])

    for sub_str in substrings:
        # firstly, does it divide evenly?
        if len(num_str) % len(sub_str) != 0:
            continue
        count = consecutive_occurance_count(num_str, sub_str)
        if count > 0:
            return False
    return True


if __name__ == "__main__":
    file_content = sys.stdin.read()

    for _range in file_content.split(","):
        first_id, last_id = (int(_id) for _id in _range.split("-"))
        ids_to_check = range(first_id, last_id + 1)

        for _id in ids_to_check:
            num_str = str(_id)
            is_valid = valid_id(num_str)
            if not is_valid:
                invalid_id_sum += _id

    print("sum:", invalid_id_sum)
