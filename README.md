# adv-pwd-gen

adv-pwd-gen (advanced password generator)

## Description

My personal password generation tool. The passwords created this way are not merely random, but are also "anti-pattern" and designed to be as difficult as possible to "break" using existing password recovery tools.

## Prerequisites

Requires Python 3.x (preferrably 3.7+) and uses the following (entirely standard) libraries:
* sys
* random
* string
* base64
* hashlib

## Overview of this Program

This program generates passwords that are intended to be highly resistant to various attacks. While random character selection is at the core, there are rules to be followed:
- 16 characters minimum length (but more is always better).
- Must use at least one upppercase letter (example character set: "ABCDEFGHIJKLMNOPQRSTUVWXYZ").
- Must use at least one lowercase letter (example character set: "abcdefghijklmnopqrstuvwxyz").
- Must use at least one number (example character set: "0123456789").
- Must use at least one special character (example character set:  "~!@#$%^&*()-_=+[];:,.<>/?\|").

Password acceptance criteria:
- Must meet length requirement.
- Must use at least one character from all of the defined character sets , above.
- Must not have consecutive uppercase letters (example: "AZ").
- Must not have consecutive lowercase letters (example: "qr").
- Must not have consecutive numbers (example: "15").
- Must not have consecutive special characters (example" "$*").
- Must not have repeating characters (this is case insensitive, example: "A" and "a" in the same password).

This allows for a functional maximum password length of 89 characters (the sum of the sets of characters).

Below is an alternate selection of character sets, intended to help reduce manual transcription errors, although this will reduce the overall premutation pool a bit. The functional maximum password length is 56 when using this character set.

```
UPPER_SET = 'ADEFGHJKLMNPRTUW'
LOWER_SET = 'abdefghijkmnpqrstuwy'
NUMBER_SET = '234679'
SPECIAL_SET = '!"#*+-./:=?@^_|'
```

Attempting to push beyond these maximum length values results in permutational dead-ends that cannot be resolved. This program has been structured to prevent these situations by enforcing length limits.

You can define your own character sets, if you like.

## How to Use

Clone this repo and run this one script contained within. There is no setup, installation or interconnect to anything else-- it's a self-contained program. A simple command line interface is present:

```
usage: pwd-gen.py [-h] [-c COUNT] [-l LENGTH] [-s]

options:
  -h, --help                    show this help message and exit
  -c COUNT, --count COUNT       number of passwords to generate
  -l LENGTH, --length LENGTH    length of passwords to generate
  -s, --hash                    lnclude password hash (sha256)
```

You can test passwords (in a more general sense) using this link: http://www.passwordmeter.com/ (there are others, of course).

## Built With

* [Python](https://www.python.org) designed by Guido van Rossum

## Author

**Rick Pelletier** - [Gannett Co., Inc. (USA Today Network)](https://www.usatoday.com/)
