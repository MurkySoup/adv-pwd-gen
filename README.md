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

This allows for a functional maximum password length of roughly 88 characters.

Below is an alternate selection of character sets, intended to help reduce manual transcription errors, although this will reduce the overall premutation pool a bit. The functional maximum password length is roughly 56 when using this character set.

```
UPPER_SET = 'ADEFGHJKLMNPRTUW'
LOWER_SET = 'abdefghijkmnpqrstuwy'
NUMBER_SET = '234679'
SPECIAL_SET = '!"#*+-./:=?@^_|'
```

You can push a bit beyond these suggested maximum values, but the farther you go, the more often this program will run into permutational dead-ends. This program has been structured to prevent these situations.

## How to Use

Clone this repo and run this one script contained within. There is no setup, installation or interconnect to anything else-- it's a self-contained program. At present, there is no command-line interface, and adjusting this program's behavior means making changes to the source code directly.

You can test passwords (in a more general sense) using this link: http://www.passwordmeter.com/

## Built With

* [Python](https://www.python.org) designed by Guido van Rossum

## Author

**Rick Pelletier** - [Gannett Co., Inc. (USA Today Network)](https://www.usatoday.com/)
