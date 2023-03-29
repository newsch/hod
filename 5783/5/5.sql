SELECT DISTINCT customerid, name, phone, citystatezip FROM customers
JOIN orders USING(customerid)
JOIN orders_items USING(orderid)
JOIN products USING(sku)
WHERE
citystatezip = 'Queens Village, NY 11429'
AND
-- desc LIKE '%Jersey%'
-- INTERSECT
-- SELECT DISTINCT customerid, name, phone, citystatezip FROM customers
-- JOIN orders USING(customerid)
-- JOIN orders_items USING(orderid)
-- WHERE
desc LIKE '%senior cat food%'