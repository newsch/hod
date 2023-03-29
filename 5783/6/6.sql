-- customers ranked by number of orders that were a loss to Noah's
SELECT COUNT(*), name, phone, SUM(total) - SUM(cost) AS lost FROM (
	-- orders where wholesale_cost > unit_price
	SELECT customerid, name, phone, ordered, shipped, SUM(unit_price * qty) AS total, SUM(wholesale_cost * qty) AS cost
	FROM customers
	JOIN orders USING(customerid)
	JOIN orders_items USING(orderid)
	JOIN products USING(sku)
	GROUP BY orderid
	HAVING SUM(unit_price * qty) < SUM(wholesale_cost * qty)
)
GROUP BY customerid
ORDER BY COUNT(*) DESC