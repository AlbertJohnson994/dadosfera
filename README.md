SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month_year, 
    SUM(total_sales) AS total_sales
FROM 
    sales
GROUP BY 
    month_year
ORDER BY 
    order_date
LIMIT 10;
