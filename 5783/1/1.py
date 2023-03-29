#! /usr/bin/env python3
import csv
import sys
from itertools import chain, repeat

LETTER_TO_NUMBER = dict(chain.from_iterable((
    zip(letters, repeat(num)) for num, letters in
        enumerate([
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz',
        ], 2))))


SUFFIXES = {'I', 'II', 'III', 'IV', 'V', 'VI', 'Jr.', 'Sr.'}


def process_number(number):
    return ''.join(c for c in number if c != '-')


def process_name(name):
    return [part for part in name.split(' ') if part not in SUFFIXES][-1]


def name_to_number(name):
    last_name = process_name(name)
    return ''.join(str(LETTER_TO_NUMBER[c.lower()]) for c in last_name)


def main():
    if len(sys.argv) > 1:
        file = open(sys.argv[1])
    else:
        file = sys.stdin
    reader = csv.DictReader(file)
    for row in reader:
        name_number = name_to_number(row['name'])
        phone_number = process_number(row['phone'])
        if phone_number.endswith(name_number):
            print(row['phone'])


if __name__ == '__main__':
    main()
