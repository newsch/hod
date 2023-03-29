SELECT name, phone, citystatezip, ordered, shipped FROM customers
JOIN orders USING(customerid)
JOIN orders_items USING(orderid)
-- JOIN products USING(sku)
WHERE date(ordered) >= '2017-04-01'
-- AND date(ordered) < '2019-01-01'
AND time(shipped) < '06:00:00'
AND time(shipped) > '03:00:00'
AND ordered = shipped
AND orders_items.sku LIKE 'BKY%'
GROUP BY orderid
HAVING SUM(qty) > 1
ORDER BY shipped
