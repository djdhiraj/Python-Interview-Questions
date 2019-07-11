-- 
-- Table structure for table `animal_types` 
-- 
  
CREATE TABLE `animal_types` ( 
  `animal_type_id` int(11) NOT NULL AUTO_INCREMENT, 
  `animal_type_description` varchar(255) NOT NULL, 
  PRIMARY KEY (`animal_type_id`) 
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ; 
  
-- 
-- Dumping data for table `animal_types` 
-- 
  
INSERT INTO `animal_types` VALUES(1, 'duck'); 
INSERT INTO `animal_types` VALUES(2, 'cow'); 
INSERT INTO `animal_types` VALUES(3, 'goose'); 
INSERT INTO `animal_types` VALUES(4, 'cat'); 
INSERT INTO `animal_types` VALUES(5, 'sheep'); 
INSERT INTO `animal_types` VALUES(6, 'horse'); 
  
-- 
-- Table structure for table `farm` 
-- 
  
CREATE TABLE `farm` ( 
  `animal_id` int(11) NOT NULL AUTO_INCREMENT, 
  `animal_type` int(11) NOT NULL, 
  `animal_description` varchar(255) NOT NULL, 
  `animal_name` varchar(255) NOT NULL, 
  PRIMARY KEY (`animal_id`) 
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ; 
  
-- 
-- Dumping data for table `farm` 
-- 
  
INSERT INTO `farm` VALUES(1, 2, 'spotted', 'Mal'); 
INSERT INTO `farm` VALUES(2, 4, 'spotted', 'Zoe'); 
INSERT INTO `farm` VALUES(3, 1, 'solid color', 'Wash'); 
INSERT INTO `farm` VALUES(4, 2, 'solid color', 'Inara'); 
  
-- 
-- Table structure for table `wild` 
-- 
  
CREATE TABLE `wild` ( 
  `animal_id` int(11) NOT NULL AUTO_INCREMENT, 
  `animal_type` int(11) NOT NULL, 
  `animal_description` varchar(255) NOT NULL, 
  `animal_name` varchar(255) NOT NULL, 
  PRIMARY KEY (`animal_id`) 
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ; 
  
-- 
-- Dumping data for table `wild` 
-- 
  
INSERT INTO `wild` (`animal_id`, `animal_type`, `animal_description`, `animal_name`) VALUES(1, 2, 'spotted', 'Jayne'); 
INSERT INTO `wild` (`animal_id`, `animal_type`, `animal_description`, `animal_name`) VALUES(2, 6, 'solid color', 'Kaylee'); 
INSERT INTO `wild` (`animal_id`, `animal_type`, `animal_description`, `animal_name`) VALUES(3, 1, 'spotted', 'Simon'); 
INSERT INTO `wild` (`animal_id`, `animal_type`, `animal_description`, `animal_name`) VALUES(4, 3, 'solid color', 'River'); 
INSERT INTO `wild` (`animal_id`, `animal_type`, `animal_description`, `animal_name`) VALUES(5, 5, 'solid color', 'Sheppard');



SELECT att.animal_type_id AS animal_type_id, 
       att.animal_type_description AS animal_type_description 
FROM animal_types att


SELECT att.animal_type_id AS animal_type_id, 
       att.animal_type_description AS animal_type_description 
FROM tutorial.animal_types att


SELECT f.animal_id AS animal_id, 
       f.animal_type AS animal_type, 
       f.animal_description AS animal_description, 
       f.animal_name AS animal_name 
FROM tutorial.farm f 
WHERE f.animal_type IN (SELECT att.animal_type_id FROM tutorial.animal_types att where att.animal_type_id = 2)


SELECT f.animal_id AS animal_id, 
       f.animal_type AS animal_type, 
       f.animal_description AS animal_description, 
       f.animal_name AS animal_name 
FROM tutorial.farm f 
WHERE f.animal_type IN (SELECT att.animal_type_id FROM tutorial.animal_types att where att.animal_type_id = 2 OR att.animal_type_id = 1)


SELECT f.animal_id AS animal_id, 
       f.animal_type AS animal_type, 
       f.animal_description AS animal_description, 
       f.animal_name AS animal_name 
FROM tutorial.farm f 
WHERE f.animal_type IN (1, 2)

INNER JOINS

SELECT f.animal_id AS farm_animal_id, 
       f.animal_type AS farm_animal_type, 
       f.animal_description AS farm_animal_description, 
       f.animal_name AS farm_animal_name, 
       att.animal_type_description AS description 
  
FROM tutorial.farm f 
INNER JOIN tutorial.animal_types att 
ON f.animal_type = att.animal_type_id;


SELECT f.animal_id AS farm_animal_id, 
       f.animal_type AS farm_animal_type, 
       f.animal_description AS farm_animal_description, 
       f.animal_name AS farm_animal_name, 
       att.animal_type_description AS description 
  
FROM tutorial.farm f 
  
INNER JOIN tutorial.animal_types att 
ON f.animal_type = att.animal_type_id;


SELECT w.animal_id AS wild_animal_id, 
       w.animal_type AS wild_animal_type, 
       w.animal_description AS wild_animal_description, 
       w.animal_name AS wild_animal_name, 
       att.animal_type_description AS description 
  
FROM tutorial.wild w 
INNER JOIN tutorial.animal_types att 
ON w.animal_type = att.animal_type_id




OUTER JOINS:
SELECT f.animal_id AS farm_animal_id, 
       f.animal_type AS farm_animal_type, 
       f.animal_description AS farm_animal_description, 
       f.animal_name AS farm_animal_name, 
       att.animal_type_description AS description 
  
FROM tutorial.farm f 
LEFT OUTER JOIN tutorial.animal_types att 
ON f.animal_type = att.animal_type_id


SELECT f.animal_id AS farm_animal_id, 
       f.animal_type AS farm_animal_type, 
       f.animal_description AS farm_animal_description, 
       f.animal_name AS farm_animal_name, 
       att.animal_type_description AS description 
  
FROM tutorial.farm f 
RIGHT OUTER JOIN tutorial.animal_types att 
ON f.animal_type = att.animal_type_id


-- 
-- Table structure for table `animal_descriptions` 
-- 
  
CREATE TABLE `animal_descriptions` ( 
  `animal_description_id` int(11) NOT NULL AUTO_INCREMENT, 
  `animal_description` varchar(255) NOT NULL, 
  PRIMARY KEY (`animal_description_id`) 
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ; 
  
-- 
-- Dumping data for table `animal_descriptions` 
-- 
  
INSERT INTO `animal_descriptions` VALUES(1, 'Spotted'); 
INSERT INTO `animal_descriptions` VALUES(2, 'Striped'); 
INSERT INTO `animal_descriptions` VALUES(3, 'Solid Color');


SELECT f.animal_id AS farm_animal_id, 
       f.animal_type AS farm_animal_type, 
       d.animal_description AS farm_animal_description, 
       f.animal_name AS farm_animal_name, 
       att.animal_type_description AS description 
  
FROM tutorial.farm f 
  
LEFT OUTER JOIN tutorial.animal_types att 
ON f.animal_type = att.animal_type_id 
LEFT OUTER JOIN tutorial.animal_descriptions d 
on f.animal_description = d.animal_description_id

Combining JOINS

SELECT w.animal_id AS wild_animal_id, 
       w.animal_type AS wild_animal_type, 
       d.animal_description AS farm_animal_description, 
       w.animal_name AS wild_animal_name, 
       att.animal_type_description AS description 
  
FROM tutorial.wild w 
  
LEFT OUTER JOIN tutorial.animal_types att 
ON w.animal_type = att.animal_type_id 
LEFT OUTER JOIN tutorial.animal_descriptions d 
on w.animal_description = d.animal_description_id


SELECT w.animal_id AS wild_animal_id, 
       w.animal_type AS wild_animal_type, 
       d.animal_description AS farm_animal_description, 
       w.animal_name AS wild_animal_name, 
       att.animal_type_description AS description 
  
FROM tutorial.wild w 
  
LEFT OUTER JOIN tutorial.animal_types att 
ON w.animal_type = att.animal_type_id 
INNER JOIN tutorial.animal_descriptions d 
on w.animal_description = d.animal_description_id


SELECT w.animal_id AS wild_animal_id, 
       w.animal_type AS wild_animal_type, 
       d.animal_description AS farm_animal_description, 
       same.animal_name AS wild_animal_name_from_same_table, 
       att.animal_type_description AS description 
  
FROM tutorial.wild w 
  
LEFT OUTER JOIN tutorial.animal_types att 
ON w.animal_type = att.animal_type_id 
  
INNER JOIN tutorial.animal_descriptions d 
on w.animal_description = d.animal_description_id 

SELECT f.animal_id AS animal_id, 
       f.animal_type AS animal_type, 
       d.animal_description AS animal_description, 
       f.animal_name AS animal_name, 
       'Farm' AS domain, 
       att.animal_type_description AS description 
  
FROM tutorial.farm f 
  
LEFT OUTER JOIN tutorial.animal_types att 
ON f.animal_type = att.animal_type_id 
  
LEFT OUTER JOIN tutorial.animal_descriptions d 
ON f.animal_description = d.animal_description_id 
  
UNION ALL 
  
SELECT w.animal_id AS animal_id, 
       w.animal_type AS animal_type, 
       d.animal_description AS animal_description, 
       w.animal_name AS animal_name, 
       'Wild' AS domain, 
       att.animal_type_description AS description 
  
FROM tutorial.wild w 
  
LEFT OUTER JOIN tutorial.animal_types att 
ON w.animal_type = att.animal_type_id 
  
LEFT OUTER JOIN tutorial.animal_descriptions d 
ON w.animal_description = d.animal_description_id

SELECT f.animal_id AS animal_id, 
       f.animal_type AS animal_type, 
       d.animal_description AS animal_description, 
       f.animal_name AS animal_name, 
       'Farm' AS domain, 
       att.animal_type_description AS description 
  
FROM tutorial.farm f 
  
LEFT OUTER JOIN tutorial.animal_types att 
ON f.animal_type = att.animal_type_id 
  
LEFT OUTER JOIN tutorial.animal_descriptions d 
ON f.animal_description = d.animal_description_id 
  
UNION ALL 
  
SELECT w.animal_id AS animal_id, 
       w.animal_type AS animal_type, 
       d.animal_description AS animal_description, 
       w.animal_name AS animal_name, 
       'Wild' AS domain, 
       att.animal_type_description AS description 
  
FROM tutorial.wild w 
  
LEFT OUTER JOIN tutorial.animal_types att 
ON w.animal_type = att.animal_type_id 
  
LEFT OUTER JOIN tutorial.animal_descriptions d 
ON w.animal_description = d.animal_description_id 
  
WHERE w.animal_id IN (SELECT animal_id FROM wild WHERE animal_id <= 3)


Simulating a FULL OUTER JOIN:


SELECT f.animal_id AS farm_animal_id, 
       f.animal_type AS farm_animal_type, 
       d.animal_description AS farm_animal_description, 
       f.animal_name AS farm_animal_name, 
       att.animal_type_description AS description 
  
FROM tutorial.farm f 
  
LEFT OUTER JOIN tutorial.animal_types att 
ON f.animal_type = att.animal_type_id 
LEFT OUTER JOIN tutorial.animal_descriptions d 
on f.animal_description = d.animal_description_id 
  
UNION 
  
SELECT f.animal_id AS farm_animal_id, 
       f.animal_type AS farm_animal_type, 
       d.animal_description AS farm_animal_description, 
       f.animal_name AS farm_animal_name, 
       att.animal_type_description AS description 
  
FROM tutorial.farm f 
  
RIGHT OUTER JOIN tutorial.animal_types att 
ON f.animal_type = att.animal_type_id 
RIGHT OUTER JOIN tutorial.animal_descriptions d 
on f.animal_description = d.animal_description_id

  
LEFT OUTER JOIN tutorial.wild same 


Unions:


ON w.animal_id = same.animal_id




set @startdate = cast('2018-01-17' as datetime);
set @enddate = cast('2019-01-17' as datetime);
set @word = 'ZENGA MEDIA';
SELECT 
		cinvoice.id, cinvoice.cp_user_id, cinvoice.duty_ids, cinvoice.payment_status, cinvoice.baseamount, cinvoice.totalamount, cinvoice.paidamount, cinvoice.dueamount, cinvoice.invoice, cinvoice.invoice_status, 
        cinvoice.igst, cinvoice.cgst, cinvoice.sgst, Date(cinvoice.created_date) as created_date,
        cu.cp_company_name,cu.cp_contact_person_name,cu.cp_contact_person_mobile,
        istatus.invoice_status_name,cinvoice.no_of_duties,cinvoice.comment
	FROM 
		rastey.corporate_invoice cinvoice
        left join rastey.corporate_users cu on cu.cp_user_id = cinvoice.cp_user_id
		left join rastey.invoice_status istatus on istatus.invoice_status_id = cinvoice.invoice_status
    where 
    ((cinvoice.created_date) between @startdate and DATE_ADD(@enddate, INTERVAL 1 DAY))
    and (
		cinvoice.id like CONCAT('%',@word,'%') 
        or cinvoice.cp_user_id like CONCAT('%',@word,'%')
        or cinvoice.payment_status like CONCAT('%',@word,'%')
        or istatus.invoice_status_name like CONCAT('%',@word,'%')
        or cinvoice.invoice_status like CONCAT('%',@word,'%')
        or cinvoice.duty_ids like CONCAT('%',@word,'%')
        or cu.cp_company_name like CONCAT('%',@word,'%')
        or cinvoice.booking_ids like CONCAT('%',@word,'%'))
	ORDER BY  cinvoice.created_date desc;
