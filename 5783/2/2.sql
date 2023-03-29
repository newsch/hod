SELECT DISTINCT name, phone, citystatezip, ordered FROM customers
JOIN orders ON customers.customerid = orders.customerid
JOIN orders_items ON orders.orderid = orders_items.orderid
JOIN products ON orders_items.sku = products.sku
WHERE ordered < date('2017-12-31')
AND customers.name LIKE 'J% D%'
AND products.sku IN ('DLI1464', 'BKY4234', 'BKY5887') -- coffee and bagels
