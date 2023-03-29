SELECT orderid, ordered, desc,
SUBSTR(desc, 0, INSTR(desc, ' (')) AS desc_uncolored
FROM customers
JOIN orders USING(customerid)
JOIN orders_items USING(orderid)
JOIN products USING(sku)
WHERE
customerid = 8342
AND desc LIKE '% (%)'