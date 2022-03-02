-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.23 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour db_employees
DROP DATABASE IF EXISTS `db_employees`;
CREATE DATABASE IF NOT EXISTS `db_employees` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_employees`;

-- Listage de la structure de la table db_employees. addresses
DROP TABLE IF EXISTS `addresses`;
CREATE TABLE IF NOT EXISTS `addresses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ZIP` varchar(25) NOT NULL,
  `city` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `address_unique` (`ZIP`,`city`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Listage de la structure de la table db_employees. departments
DROP TABLE IF EXISTS `departments`;
CREATE TABLE IF NOT EXISTS `departments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Listage de la structure de la table db_employees. employees
DROP TABLE IF EXISTS `employees`;
CREATE TABLE IF NOT EXISTS `employees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `birthdate` date NOT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `road` varchar(75) NOT NULL,
  `hiring_date` date NOT NULL,
  `percentage` decimal(3,2) NOT NULL,
  `salary` decimal(6,2) NOT NULL,
  `holiday_balance` decimal(2,2) NOT NULL DEFAULT '0.00',
  `under_contract` tinyint NOT NULL,
  `work_time` decimal(10,0) NOT NULL DEFAULT '0',
  `password` varchar(255) NOT NULL,
  `employee_id` int DEFAULT NULL,
  `address_id` int NOT NULL,
  `job_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `fk_employees_employees_idx` (`employee_id`),
  KEY `fk_employees_addresses1_idx` (`address_id`),
  KEY `fk_employees_job1_idx` (`job_id`),
  CONSTRAINT `fk_employees_addresses1` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`),
  CONSTRAINT `fk_employees_employees` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `fk_employees_job1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Listage de la structure de la table db_employees. employees_has_tasks
DROP TABLE IF EXISTS `employees_has_tasks`;
CREATE TABLE IF NOT EXISTS `employees_has_tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `task_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_employees_has_tasks_tasks1_idx` (`task_id`),
  KEY `fk_employees_has_tasks_employees1_idx` (`employee_id`),
  CONSTRAINT `fk_employees_has_tasks_employees1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `fk_employees_has_tasks_tasks1` FOREIGN KEY (`task_id`) REFERENCES `tasks` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Listage de la structure de la table db_employees. jobs
DROP TABLE IF EXISTS `jobs`;
CREATE TABLE IF NOT EXISTS `jobs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `department_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `fk_jobs_departments1_idx` (`department_id`),
  CONSTRAINT `fk_jobs_departments1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Listage de la structure de la table db_employees. payslips
DROP TABLE IF EXISTS `payslips`;
CREATE TABLE IF NOT EXISTS `payslips` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file_path` varchar(100) NOT NULL,
  `employee_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `file_path_UNIQUE` (`file_path`),
  KEY `fk_payslips_employees1_idx` (`employee_id`),
  CONSTRAINT `fk_payslips_employees1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Listage de la structure de la table db_employees. tasks
DROP TABLE IF EXISTS `tasks`;
CREATE TABLE IF NOT EXISTS `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `project` varchar(45) NOT NULL,
  `title` varchar(45) NOT NULL,
  `description` tinytext,
  `validation` tinyint(1) DEFAULT '0',
  `since` datetime NOT NULL,
  `until` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_tasks` (`project`,`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
