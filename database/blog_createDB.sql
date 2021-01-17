DROP DATABASE IF EXISTS `blog_sql`;
CREATE DATABASE `blog_sql`; 
USE `blog_sql`;

SET NAMES UTF8MB4 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE `tbl_entry` (
  `entry_id` int NOT NULL AUTO_INCREMENT,
  `entry_title` varchar(50) NOT NULL,
  `entry_date` date NOT NULL,
  `entry_content` varchar(500) NOT NULL,
  PRIMARY KEY (`entry_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `tbl_entry` VALUES (1,'Test Post', '2020-01-01', 'This is a Test Post and the text here is fake content!');