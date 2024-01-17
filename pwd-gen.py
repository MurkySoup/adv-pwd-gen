#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Generates a fine selection of high-quality, barrel-aged, non-GMO, organic, vegan,
hormone-free, grass-fed, free-range, environmentally sustainable passwords.

Version 0.9.8-Alpha (Do Not Distribute) by Rick Pelletier, 24 June 2019
Last update: 16 January 2024
"""

import sys
import random
import string
import base64
import hashlib
import argparse


# Standard character sets
UPPER_SET = string.ascii_uppercase
LOWER_SET = string.ascii_lowercase
NUMBER_SET = string.digits
SPECIAL_SET = '~!@#$%^&*()-_=+[];:,.<>/?\\|'

# Reduced character sets
"""
UPPER_SET = 'ADEFGHJKLMNPRTUW'
LOWER_SET = 'abdefghijkmnpqrstuwy'
NUMBER_SET = '234679'
SPECIAL_SET = '!"#*+-./:=?@^_|'
"""
WORKING_SET = set(UPPER_SET + LOWER_SET + NUMBER_SET + SPECIAL_SET)
MAX_PWD_LENGTH = len(WORKING_SET) - 1


def hash_password(password:str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def generate_character(working_set:list) -> str:
    return random.choice(list(working_set))


def generate_password(pwd_len:int) -> str:
    pwd = generate_character(WORKING_SET)
    used_chars = set(pwd)
    max_iter = pwd_len * 100

    for i in range(max_iter):
        if len(pwd) == pwd_len:
            return pwd

        last_char = pwd[-1]
        candidate_set = None

        if last_char in UPPER_SET:
            candidate_set = set(LOWER_SET + NUMBER_SET + SPECIAL_SET)
        elif last_char in LOWER_SET:
            candidate_set = set(UPPER_SET + NUMBER_SET + SPECIAL_SET)
        elif last_char in NUMBER_SET:
            candidate_set = set(UPPER_SET + LOWER_SET + SPECIAL_SET)
        elif last_char in SPECIAL_SET:
            candidate_set = set(UPPER_SET + LOWER_SET + NUMBER_SET)
        if candidate_set is not None:
            candidates = candidate_set - used_chars

            if candidates:
                candidate = random.choice(list(candidates))
                pwd += candidate
                used_chars.add(candidate)

    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", type=int, help='number of passwords to generate', default=1, required=False)
    parser.add_argument("-l", "--length", type=int, help='length of passwords to generate', default=24, required=False)
    parser.add_argument("-s", "--hash", action='store_true', help='lnclude password hash (sha256)', required=False)

    args = parser.parse_args()

    random.seed()

    if args.length > MAX_PWD_LENGTH:
        args.length = MAX_PWD_LENGTH

    while(args.count > 0):
        if (pwd := generate_password(args.length)):
            print(f'{pwd}', end='')

            if args.hash:
                print(f'  {hash_password(pwd)}', end='')

            print()

            args.count -= 1
        else:
            continue


    sys.exit(0)
else:
    sys.exit(1)

# end of script
