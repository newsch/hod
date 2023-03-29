#! /usr/bin/env python3
import sqlite3
import os
import sys


def get_colored_orders(cur, customerid):
    query = """
    SELECT orderid, ordered, desc
    FROM customers
    JOIN orders USING(customerid)
    JOIN orders_items USING(orderid)
    JOIN products USING(sku)
    WHERE
    customerid = ?
    --AND ordered = shipped
    AND desc LIKE '% (%)'
    """
    return cur.execute(query, (customerid,))


def strip_color(s):
    return s[:s.find(' (')]


def get_similar_nearby_orders(cur, orderid, ordered, desc):
    MINUTES = 1 / 24 / 60
    difference = 60 * MINUTES

    desc_uncolored = strip_color(desc)

    query = """
    SELECT phone
    FROM customers
    JOIN orders USING(customerid)
    JOIN orders_items USING(orderid)
    JOIN products USING(sku)
    WHERE
    orderid != :orderid -- different orders
    -- close in time
    AND abs(julianday(ordered) - julianday(:orig_ordered)) < :julian_length
    -- same product
    AND SUBSTR(desc, 1, LENGTH(:desc_uncolored)) = :desc_uncolored
    -- different color
    AND desc != :desc
    --AND ordered = shipped -- in-store purchase?
    """
    values = {
        "orderid": orderid,
        "orig_ordered": ordered,
        "julian_length": difference,
        "desc": desc,
        "desc_uncolored": desc_uncolored,
    }

    return cur.execute(query, values)


def main():
    ID = 8342

    db_file = os.getenv('DATABASE')
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    for row in list(get_colored_orders(cur, ID)):
        orderid, date, desc = row
        print(strip_color(desc), file=sys.stderr)
        for phone, in list(get_similar_nearby_orders(cur, *row)):
            print(phone)


if __name__ == '__main__':
    main()
