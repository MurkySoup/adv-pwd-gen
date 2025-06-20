#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Password Risk Analyzer, Version 0.2-Beta (Do Not Distribute)
By Rick Pelletier, 20 June 2025
Last Update: 20 June 2025

Arbitrary scoring system for paswsord string, based on the 'passwordmeter.com' methodology.
See: https://passwordmeter.com/ . Output is a JSON object.
"""


import sys
import re
import argparse
import json


def analyze_password(password:str) -> int:
    score = 0
    length = len(password)

    # Basic point scoring
    score += length * 4  # Number of Characters
    upper_case = re.findall(r'[A-Z]', password)
    lower_case = re.findall(r'[a-z]', password)
    numbers = re.findall(r'[0-9]', password)
    symbols = re.findall(r'[~!@#$%^&*()\-_=+\[\];:,.<>/?|]', password)

    if upper_case:
        score += (length - len(upper_case)) * 2  # Uppercase Letters Present
    if lower_case:
        score += (length - len(lower_case)) * 2  # Lowercase Letters Present
    if numbers:
        score += len(numbers) * 4  # Numbers present
    if symbols:
        score += len(symbols) * 6  # Symbols present

    middle_numbers_symbols = re.findall(r'(?<=.)([0-9~!@#$%^&*()\-_=+\[\];:,.<>/?|])(?=.)', password)
    score += len(middle_numbers_symbols) * 2  # Middle Numbers or Symbols

    if length >= 16:
        score += 2  # Length Requirement met (16 characters)

    # Point deductions
    if password.isalpha():
        score -= length  # Password is Letters Only
    if password.isdigit():
        score -= length  # Password is Numbers Only

    repeat_chars = len(password) - len(set(password.lower()))
    score -= repeat_chars  # Repeat Characters present (Case Insensitive)

    consecutive_upper = re.findall(r'([A-Z])\1', password)
    score -= len(consecutive_upper) * 2  # Consecutive Uppercase Letters Present

    consecutive_lower = re.findall(r'([a-z])\1', password)
    score -= len(consecutive_lower) * 2  # Consecutive Lowercase Letters Present

    consecutive_numbers = re.findall(r'([0-9])\1', password)
    score -= len(consecutive_numbers) * 2  # Consecutive Numbers Present

    sequential_letters = re.findall(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower())
    score -= len(sequential_letters) * 3  # Sequential Letters Present (3+)

    sequential_numbers = re.findall(r'(012|123|234|345|456|567|678|789)', password)
    score -= len(sequential_numbers) * 3  # Sequential Numbers Present (3+)

    sequential_symbols = re.findall(r'(~!@|!@#|@#$|#$%|$%^|%^&|^&*|&*\(\)|\(\)_|\)_\+|\+=\{|=\{\[|\[;|;:|:,.|,.<|.<>)', password)
    score -= len(sequential_symbols) * 3  # Sequential Symbols Present (3+)

    return score


def scoring_label(score:int) -> str:
    risk_label = 'No Risk Label'
    risk_class = 0

    if score <= 74:
        risk_label = "Very High Risk"
        risk_class = 1
    elif 75 <= score <= 124:
        risk_label = "High Risk"
        risk_class = 2
    elif 125 <= score <= 199:
        risk_label = "Moderate Risk"
        risk_class = 3
    elif 200 <= score <= 274:
        risk_label = "Low Risk"
        risk_class = 4
    else: # 275+
        risk_label = "Very Low Risk"
        risk_class = 5

    return risk_label, risk_class


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", type=str, help='password string to analayze', required=True)
    args = parser.parse_args()

    risk_score  = analyze_password(args.string)
    risk_label, risk_class = scoring_label(risk_score)

    data_obj = {
        'password':args.string,
        'risk_score':risk_score,
        'risk_label':risk_label,
        'risk_class':risk_class
    }

    print(json.dumps(data_obj, indent=2, sort_keys=True))

    sys.exit(0)
else:
    sys.exit(1)

# end of script
