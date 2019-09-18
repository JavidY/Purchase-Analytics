CREATE TABLE `OLTP`.`departments` (
  `department_id` VARCHAR(100) NOT NULL,
  `department` VARCHAR(100) NULL,
  PRIMARY KEY (`department_id`),
  UNIQUE INDEX `department_id_UNIQUE` (`department_id` ASC) VISIBLE);
