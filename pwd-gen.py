#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Generates a fine selection of high-quality, barrel-aged, non-GMO, organic, vegan,
hormone-free, grass-fed, free-range, environmentally sustainable passwords.

Version 0.9.6-Alpha (Do Not Distribute) by Rick Pelletier, 24 June 2019
Last update: 07 April 2023

Selection and acceptanace rules for passwords:
- 16 characters minimum (but more is always better).
- Must use at least one upppercase letter (example character set: "ABCDEFGHIJKLMNOPQRSTUVWXYZ").
- Must not have consecutive uppercase letters (example: "AZ").
- Must use at least one lowercase letter (example character set: "abcdefghijklmnopqrstuvwxyz").
- Must not have consecutive lowercase letters (example: "qr").
- Must use at least one number (example character set: "0123456789").
- Must not have consecutive numbers (example: "15").
- Must use at least one special character (example character set:  "~!@#$%^&*()-_=+[];:,.<>/?\|").
- Must not have consecutive special characters (example" "$*").
- Must not have repeating characters (this is case insensitive, example: "A" and "a" in the same password).

See: http://www.passwordmeter.com/
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
#UPPER_SET = 'ADEFGHJKLMNPRTUW'
#LOWER_SET = 'abdefghijkmnpqrstuwy'
#NUMBER_SET = '234679'
#SPECIAL_SET = '!"#*+-./:=?@^_|'

WORKING_SET = set(UPPER_SET + LOWER_SET + NUMBER_SET + SPECIAL_SET)
MAX_PWD_LENGTH = len(WORKING_SET)


def b64_password(password:str):
    return base64.b64encode(password.encode('utf-8')).decode('utf-8')


def hash_password(password:str):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def generate_character(working_set:list):
    return random.choice(list(working_set))


def acceptance_check(password:str):
    uppercase_set = set(UPPER_SET)
    lowercase_set = set(LOWER_SET)
    number_set = set(NUMBER_SET)
    special_set = set(SPECIAL_SET)

    if len(password) < 16:
        return False

    if not uppercase_set.intersection(password):
        return False

    if not lowercase_set.intersection(password):
        return False

    if not number_set.intersection(password):
        return False

    if not special_set.intersection(password):
        return False

    return True


def generate_password(pwd_len:int):
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
    args = parser.parse_args()

    output_counter = 0
    random.seed()

    if args.length > MAX_PWD_LENGTH:
        args.length = MAX_PWD_LENGTH

    while output_counter < args.count:
        if pwd := generate_password(args.length):
            if acceptance_check(pwd) == True:
                print(f'{pwd}  {b64_password(pwd)}  {hash_password(pwd)}')
                output_counter += 1
            else:
               continue

    sys.exit(0)
else:
    sys.exit(1)

# end of script
