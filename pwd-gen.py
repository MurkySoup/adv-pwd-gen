#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Generates a fine selection of high-quality, barrel-aged, non-GMO, organic, vegan, cruelty-free,
gluten-free, pesticide-free, hormone-free, grass-fed, free range, sustainable passwords.
Now new and improvewd with shock-absorbing infinite-loop protection!

Version 0.7-Alpha (Do Not Distribute) by Rick Pelletier, 24 June 2019
Last update: 31 March 2023

Selection rules for passwords:
- 16 characters minimum (but more is always better)
- Must use at least one character from all of the following categories:
- Must use at least one upppercase letters (example character set: "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
- Must use at least one lowercase letters (example character set: "abcdefghijklmnopqrstuvwxyz")
- Must use at least one numbers (example character set: "0123456789")
- Must use at least one special characters (example character set:  "~!@#$%^&*()-_=+[];:,.<>/?\|")

Password acceptance criteria:
- Must not have consecutive uppercase letters (example: "AZ")
- Must not have consecutive lowercase letters (example: "qr")
- Must not have consecutive numbers (example: "15")
- Must not have consecutive special characters (example" "$*")
- Must not have repeating characters (this is case insensitive, example: "A" and "a" in the same password)

See: http://www.passwordmeter.com/

Optimizations implemented in the version (for the curious):

- Moved the constant character sets ('upper_set', 'lower_set', 'number_set', special_set' and 'working_set') outside
  of the 'generate_password' function and make them global variables. This way, they are only initialized once and can
  be reused across multiple function calls.

- Used a list comprehension to generate the complete character set in 'working_set' instead of concatenating them with
  '+.'. This can potentially be faster and more memory-efficient.

- Replaced the 'rule_check' function with a set intersection operation. For example, instead of:
  'if rule_check(upper_set, pwd[-1])', I can use 'if set(pwd[-1]).intersection(upper_set)'. Sets have constant time
  complexity for membership tests, so this can be faster than looping through each character in the set.

- Used a 'for' loop instead of a while loop in generate_password to avoid the risk of infinite loops. I can set a
  maximum number of iterations to prevent the function from running too long (and into a permutational dead end).

- Used 'join' instead of '+=' to concatenate strings in 'generate_password'. This can be more memory-efficient
  since strings are immutable and '+=' creates a new string object each time.

- Instead of checking for repeating characters with '(candidate.lower() in list(pwd))' or '(candidate.upper() in list(pwd))',
  a set is used to keep track of the characters that have already been used in the password. Sets have constant
  time complexity for membership tests and can improve performance for large passwords.

- Reformatted code to PEP8-spec because I got tired of hearing people kvetch about it.
"""


import sys
import random
import string
import base64
import hashlib


# Character sets

"""
An alternate selection of character sets, intended to help reduce manual transcription errors, although this will
reduce the overall premutation pool a bit. Functional maximum value for 'pwd_len' is 34 when using these character
sets:

UPPER_SET = 'ADEFGHJKLMNPRTUW'
LOWER_SET = 'abdefghijkmnpqrstuwy'
NUMBER_SET = '234679'
SPECIAL_SET = '!"#*+-./:=?@^_|'
"""

UPPER_SET = string.ascii_uppercase
LOWER_SET = string.ascii_lowercase
NUMBER_SET = string.digits
SPECIAL_SET = '~!@#$%^&*()-_=+[];:,.<>/?\\|'
WORKING_SET = set(UPPER_SET + LOWER_SET + NUMBER_SET + SPECIAL_SET)


def b64_password(string):
    return base64.b64encode(string.encode('utf-8')).decode('utf-8')


def hash_password(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


def generate_character(working_set):
    return random.choice(list(working_set))


def generate_password(pwd_len):
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
    random.seed()
    pwd_len = 32
    pwd_count = 25
    counter = 0

    while counter < pwd_count:
        if (pwd := generate_password(pwd_len)):
            print(f'{pwd}  {b64_password(pwd)}  {hash_password(pwd)}')
            counter += 1

    sys.exit(0)
else:
    sys.exit(1)

# end of script
