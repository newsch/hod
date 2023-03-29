#! /usr/bin/env python3
from csv import DictReader, excel_tab
from datetime import datetime, date
from functools import lru_cache
import itertools
import sys


FILE = 'dog-years.tsv'


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


@lru_cache
def aries(y):
    if not isinstance(y, int):
        y = y.year
    return date(y, 3, 20), date(y, 4, 20)


def in_aries(d):
    a_beg, a_end = aries(d)
    return d >= a_beg and d <= a_end


def aries_ranges(start, end):
    """
    >>> list(aries_ranges(date(1, 1, 1), date(1, 12, 31)))
    [(datetime.date(1, 3, 20), datetime.date(1, 4, 20))]
    >>> list(aries_ranges(date(1, 4, 20), date(2, 4, 21)))
    [(datetime.date(1, 4, 20), datetime.date(1, 4, 20)), (datetime.date(2, 3, 20), datetime.date(2, 4, 20))]
    >>> list(aries_ranges(date(1, 4, 21), date(2, 3, 19)))
    []
    """
    def dates():
        yield start
        years = (date(y, 1, 1) for y in range(start.year + 1, end.year + 1))
        yield from years
        if end.month != 1 and end.day != 1:
            yield end

    for r in pairwise(dates()):
        min_r = min_range(aries(r[0].year), r)
        if min_r is None:
            return
        yield min_r


def get_dog_years(f):
    def parse(s):
        d = datetime.strptime(s, '%d %B %Y')
        return d.date()

    reader = DictReader(f, dialect=excel_tab)
    for row in reader:
        start = parse(row['Start date'])
        end = parse(row['End date'])
        yield start, end


def min_range(r1, r2):
    """Intersection, if any, of date ranges"""
    b1, e1 = r1
    b2, e2 = r2
    if e1 < b2 or e2 < b1:
        return None
    new_beg = max(b1, b2)
    new_end = min(e1, e2)
    return new_beg, new_end


def main():
    with open(FILE) as f:
        ranges = list(itertools.chain.from_iterable(aries_ranges(s, e) for s, e in get_dog_years(f)))

    # for start, end in ranges:
    #     print(start, end)

    if len(sys.argv) > 1:
        file = open(sys.argv[1])
    else:
        file = sys.stdin
    reader = DictReader(file)
    for row in reader:
        name = row['name']
        birthdate = date.fromisoformat(row['birthdate'])
        phone_number = row['phone']
        if row['citystatezip'] != 'South Ozone Park, NY 11420':  # yesterday's person's address
            continue
        for start, end in ranges:
            if birthdate >= start and birthdate <= end:
                print(name, phone_number, birthdate)


if __name__ == '__main__':
    main()
