CREATE DATABASE OLTP;
CREATE USER 'oltp' IDENTIFIED BY 'oltp';
GRANT ALL ON OLTP.* TO 'oltp';

CREATE TABLE `OLTP`.`departments` (
  `department_id` INT NOT NULL,
  `department` VARCHAR(100) NULL,
  PRIMARY KEY (`department_id`),
  UNIQUE INDEX `department_id_UNIQUE` (`department_id` ASC) VISIBLE);
