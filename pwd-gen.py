#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
A fine selection of high-quality, barrel-aged, non-gmo, organic,
vegan, cruelty-free, gluten-free passwords-- just like mom used to make!
now with shock-absorbing infinite-loop potection!

Version 0.6-alpha (do not distribute) by Rick Pelletier, 24 June 2019
Last update: 11 March 2021

Selection rules for "perfect" passwords:
- 16 characters minimum (more is always better)
- Must use at least one character from all of the following categories:
  - Upppercase letters ( "ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
  - Lowercase letters ( "abcdefghijklmnopqrstuvwxyz" )
  - Numbers ( "0123456789" )
  - Special characters ( "~!@#$%^&*()-_=+[];:,.<>/?\|" )

Password acceptance criteria:
- Must not have consecutive uppercase letters (like "AZ")
- Must not have consecutive lowercase letters (like "qr")
- Must not have consecutive numbers (like "15")
- Must not have consecutive special characters (like "$*")
- Must not have repeating characters (case insensitive, like "A" and "a" in the same password)



upper_set = 'ADEFGHJKLMNPRTUW'
lower_set = 'abdefghijkmnpqrstuwy'
number_set = '234679'
special_set = ' !"#*+-./:=?@^_|'
"""


import sys
import random
import string
import base64
import hashlib


def b64_password(string):
  return base64.b64encode(bytes(string, 'utf-8')).decode('utf-8')


def hash_password(string):
  return hashlib.sha256(bytes(string, 'utf-8')).hexdigest()


def generate_character(working_set):
  return system_random.choice(list(working_set))


def rule_check(character_set, character):
  if any((c in character_set) for c in character):
    return True
  else:
    return False


def generate_password(pwd_len):
  pwd = generate_character(working_set)
  candidate = ''
  counter = 0

  while(len(pwd) < pwd_len):
    if counter > (pwd_len * 100): # force break-out if we appear to hit a permutational dead-end
      return False

    if rule_check(upper_set, pwd[-1]):
      candidate = generate_character(lower_set + number_set + special_set)

    if rule_check(lower_set, pwd[-1]):
      candidate = generate_character(upper_set + number_set + special_set)

    if rule_check(number_set, pwd[-1]):
      candidate = generate_character(upper_set + lower_set + special_set)

    if rule_check(special_set, pwd[-1]):
      candidate = generate_character(upper_set + lower_set + number_set)

    if (candidate.lower() in list(pwd)) or (candidate.upper() in list(pwd)):
      counter += 1
      continue

    pwd += candidate

  return pwd


if __name__ == '__main__':
  system_random = random.SystemRandom() # no need for seed()

  # functional max value for 'pwd_len' is 48 when using this character set
  upper_set = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  lower_set = list('abcdefghijklmnopqrstuvwxyz')
  number_set = list('0123456789')
  special_set = list('~!@#$%^&*()-_=+[];:,.<>/?\|')

  """
  # An alternate selection of character sets, intended to help reduce manual transcription
  # errors, although this will reduce the overall premutation pool a bit.
  # functional max value for 'pwd_len' is 34 when using this character set

  upper_set = 'ADEFGHJKLMNPRTUW'
  lower_set = 'abdefghijkmnpqrstuwy'
  number_set = '234679'
  special_set = ' !"#*+-./:=?@^_|'
  """

  working_set = upper_set + lower_set + number_set + special_set

  pwd_len = 32;
  pwd_count = 16;
  counter = 0

  while(counter < pwd_count):
    pwd = generate_password(pwd_len)

    if pwd:
      print(f'{pwd}  {b64_password(pwd)}  {hash_password(pwd)}')
      counter += 1

  sys.exit(0)
else:
  sys.exit(1)

# end of script
