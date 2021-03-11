# adv-pwd-gen
adv-pwd-gen (advanced password generator)

## Description

My personal password generation tool.

## Prerequisites

Requires Python 3.x (preferrably 3.6+) and uses the following (entirely standard) libraries:
* sys
* random
* string
* base64
* hashlib

## Overview of this Program

This program generates passwords that are intended to be highly resistant to various attacks. While random generation is at the core, there are rules to be followed:

- 16 character minimum (more is always better)
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

This allows for a functional maximum password length of 48 characters.

An alternate selection of character sets, intended to help reduce manual transcription errors, although this will reduce the overall premutation pool a bit. The functional maximum password length is 34 when using this character set.

- upper_set = 'ADEFGHJKLMNPRTUW'
- lower_set = 'abdefghijkmnpqrstuwy'
- number_set = '234679'
- special_set = ' !"#*+-./:=?@^_|'

You can push a bit beyond these suggested maximum values, but the farther you go, the more often this programm will run into permutational dead-ends. Code has been added to allow this program to break out of these situations and attempt to proceed normally.

## How to Use

Clone this repo and run this one script contained within. There is no setup, installation or interconnect to anything else-- it's a self-contained program. At present, there is no command-line interface, and adjusting this programs behavior means making changes to the source code directly.

## Built With

* [Python](https://www.python.org) designed by Guido van Rossum

## Author

**Rick Pelletier** - [Gannett Co., Inc. (USA Today Network)](https://www.usatoday.com/)
