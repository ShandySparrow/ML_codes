SELECT * FROM sales LIMIT 5;

SELECT "Boxes" FROM sales WHERE "Boxes" = 0;

-- To estimate amount per box and deal with division by zero error
SELECT "SaleDate", "Customers", "Amount", ROUND(COALESCE("Amount" / NULLIF("Boxes",0),0),2)k AS "AmountPerBox" 
FROM sales;

SELECT * FROM sales WHERE "Amount" > 10000 AND "SaleDate" >= '2021-10-21' ORDER BY "Customers" DESC;

SELECT * FROM sales WHERE "Boxes" BETWEEN 0 AND 50;

SELECT "SaleDate", "Amount", DATE_PART('week',"SaleDate") FROM sales WHERE DATE_PART('week',"SaleDate") = 4; 

SELECT * FROM people WHERE "Team" = 'Yummies' OR "Team" = 'Delish';
SELECT * FROM people WHERE "Team" IN ('Yummies' , 'Delish');

SELECT * FROM people WHERE "Salesperson" LIKE 'B%';

SELECT "SaleDate", "Amount", 
				CASE 	WHEN "Amount" < 1000 THEN 'under 1k'
						WHEN "Amount" < 5000 THEN 'under 5k'
						WHEN "Amount" < 8000 THEN 'under 8k'
						ELSE 'under 10k or more'
				END AS "Amount Category" 
FROM sales;

-- INNER JOIN
SELECT s."SaleDate", s."Amount", p."Salesperson"
FROM sales s JOIN people p
ON s."SPID" = p."SPID";
				
-- MULTIPLE JOIN

SELECT s."SaleDate", p."Salesperson", p."Team", pr."Product", pr."Category"
FROM sales s JOIN people p
ON s."SPID" = p."SPID" JOIN products pr
ON pr."PID" = s."PID";

-- GROUP BY

SELECT "Region", COUNT("Region") 
FROM geo GROUP BY "Region";

SELECT "Region", COUNT("Region") 
FROM geo GROUP BY "Region" HAVING COUNT("Region") > 1;

SELECT "GeoID", SUM("Amount"), AVG("Amount"), SUM("Customers") 
FROM sales GROUP BY "GeoIDk"; 

SELECT g."Geo", SUM("Amount"), AVG("Amount"), SUM("Customers") 
FROM sales s JOIN geo g ON s."GeoID" = g."GeoID"
GROUP BY g."Geo"; 

-- Practice Problems

-- 1) Print details of shipments (sales) where amounts are > 2,000 and boxes are <100?
SELECT * FROM sales WHERE "Amount" > 2000 AND "Boxes" < 100;

-- 2) How many shipments (sales) each of the sales persons had in the month of January 2022?
SELECT p."Salesperson", COUNT(*) FROM sales s
JOIN people p ON s."SPID" = p."SPID"
WHERE s."SaleDate" BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY p."Salesperson";

-- 3) Which product sells more boxes? Milk Bars or Eclairs?
SELECT p."Product", SUM(s."Boxes") FROM sales s
JOIN products p ON s."PID" = p."PID"
WHERE p."Product" IN ('Milk Bars', 'Eclairs')
GROUP BY p."Product" ORDER BY SUM(s."Boxes") DESC LIMIT 1;

-- 4) Which product sold more boxes in the first 7 days of February 2022? Milk Bars or Eclairs?
SELECT p."Product", SUM(s."Boxes") FROM sales s
JOIN products p ON s."PID" = p."PID"
WHERE p."Product" IN ('Milk Bars', 'Eclairs') AND s."SaleDate" BETWEEN '2022-2-1' AND '2022-2-7'
GROUP BY p."Product";

-- 5) Which shipments had under 100 customers & under 100 boxes? Did any of them occur on Wednesday?
SELECT * FROM sales 
WHERE "Customers" < 100 AND "Boxes" < 100 AND DATE_PART('week',"SaleDate") = 3;

-- 6) What are the names of salespersons who had at least one shipment (sale) in the first 7 days of January 2022?
SELECT p."Salesperson", COUNT(*) FROM sales s
JOIN people p ON s."SPID" = p."SPID"
WHERE s."SaleDate" BETWEEN '2022-1-1' AND '2022-1-7'
GROUP BY p."Salesperson";

-- 7) Which salespersons did not make any shipments in the first 7 days of January 2022?
SELECT p."Salesperson" FROM people p
WHERE p."SPID" NOT IN
(SELECT s."SPID" FROM sales s
WHERE s."SaleDate" BETWEEN '2022-1-1' AND '2022-1-7');

-- 8) How many times we shipped more than 1,000 boxes in each month?
SELECT TO_CHAR("SaleDate",'MONTH'), COUNT("Boxes") FROM sales
WHERE "Boxes" > 1000
GROUP BY TO_CHAR("SaleDate",'MONTH')
ORDER BY COUNT("Boxes") DESC;

-- 9) Did we ship at least one box of ‘After Nines’ to ‘New Zealand’ on all the months?
SELECT TO_CHAR("SaleDate",'MONTH'), CASE WHEN SUM("Boxes") > 1 THEN 'YES'
										 ELSE 'NO' 		
									END AS "Status"								
FROM sales s JOIN products pr ON s."PID" = pr."PID"
JOIN geo g ON s."GeoID" = g."GeoID"
WHERE pr."Product" = 'After Nines' AND g."Geo" = 'New Zealand'
GROUP BY TO_CHAR("SaleDate",'MONTH');

-- 10) India or Australia? Who buys more chocolate boxes on a monthly basis?
SELECT TO_CHAR("SaleDate",'MONTH'),
	   SUM(CASE WHEN g."Geo" = 'India' THEN s."Boxes"
	   			ELSE 0
	   		END) AS "India Boxes",
	   SUM(CASE WHEN g."Geo" = 'Australia' THEN s."Boxes"
	   			ELSE 0
	   		END) AS "Australia Boxes"
FROM sales s JOIN geo g ON s."GeoID" = g."GeoID"
GROUP BY TO_CHAR("SaleDate",'MONTH');

