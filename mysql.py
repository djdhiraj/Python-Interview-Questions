Creating a new table from the select statement 

The following SQL code is an example of creating a table from a SELECT query:

CREATE TABLE TempCustomer AS

SELECT first_name, last_name

FROM ExternalCustomer AS c

WHERE c.create_date >= ‘8/1/2015'


Take a look at the following query:


CREATE TABLE TempCustomer AS

SELECT c.first_name, c.last_name, a.address

FROM ExternalCustomer AS c

INNER JOIN ExternalAddress AS a

ON c.customer_id = a.customer_id

WHERE c.create_date >= ‘8/1/2015';




INSERT INTO Customer (first_name, last_name, address)

SELECT first_name, last_name, address FROM TempCustomer;

UPDATE Customer AS c

LEFT JOIN TempCustomer AS tc ON c.customer_id = tc.customer_id

SET c.first_name = tc.first_name, c.last_name = tc.last_name, c.address = tc.address

WHERE c.customer_id > 5;


UPDATE Customer

SET first_name = (SELECT first_name FROM TempCustomer where TempCustomer.customer_id = Customer.customer_id);

