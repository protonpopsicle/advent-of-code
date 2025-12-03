#!/usr/bin/env python3

import sys


file_content = None
invalid_id_sum = 0

def valid_id(num_str):
    if len(num_str) % 2 == 0:  # even num of digits
        half_len = len(num_str) // 2
        first_half = num_str[:half_len]
        second_half = num_str[half_len:]
        return first_half != second_half
    return True

if __name__ == "__main__":
    file_content = sys.stdin.read()

    for _range in file_content.split(','):
        first_id, last_id = (int(_id) for _id in _range.split('-'))
        ids_to_check = range(first_id, last_id + 1)
    
        for _id in ids_to_check:
            num_str = str(_id)
            is_valid = valid_id(num_str)
            if not is_valid:
                invalid_id_sum += _id

    print('sum:', invalid_id_sum)
