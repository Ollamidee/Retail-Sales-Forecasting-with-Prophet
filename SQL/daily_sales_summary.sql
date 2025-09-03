USE sales_project;

SELECT 
	DATE(inv.invoice_date) AS sales_date, 
    SUM(prod.unit_price * inv_it.quantity) AS total_sales
FROM customers cus
JOIN invoices inv
	USING (customer_id)
JOIN invoice_item inv_it
	USING (invoice_no )
JOIN products prod
	USING(product_id)
WHERE quantity > 0
GROUP BY sales_date
ORDER BY sales_date;





