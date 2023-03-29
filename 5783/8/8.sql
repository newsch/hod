-- number of collectible products (81)
-- SELECT COUNT(*) FROM products WHERE sku LIKE 'COL%'

-- get customers by largest number of unique collectibles purchased
SELECT COUNT(DISTINCT sku), name, phone, sku FROM customers
JOIN orders USING(customerid)
JOIN orders_items USING(orderid)
WHERE sku LIKE 'COL%'
GROUP BY customerid
ORDER BY COUNT(DISTINCT sku) DESC
LIMIT 10;
