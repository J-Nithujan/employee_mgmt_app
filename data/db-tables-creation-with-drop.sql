-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_employees
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `db_employees` ;

-- -----------------------------------------------------
-- Schema db_employees
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_employees` DEFAULT CHARACTER SET utf8 ;
USE `db_employees` ;

-- -----------------------------------------------------
-- Table `db_employees`.`addresses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `db_employees`.`addresses` ;

CREATE TABLE IF NOT EXISTS `db_employees`.`addresses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ZIP` VARCHAR(25) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `address_unique` (`ZIP` ASC, `city` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_employees`.`jobs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `db_employees`.`jobs` ;

CREATE TABLE IF NOT EXISTS `db_employees`.`jobs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_employees`.`departments`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `db_employees`.`departments` ;

CREATE TABLE IF NOT EXISTS `db_employees`.`departments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_employees`.`employees`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `db_employees`.`employees` ;

CREATE TABLE IF NOT EXISTS `db_employees`.`employees` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(100) NOT NULL,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `birthdate` DATE NOT NULL,
  `phone_number` VARCHAR(45) NULL DEFAULT NULL,
  `road` VARCHAR(75) NOT NULL,
  `hiring_date` DATE NOT NULL,
  `percentage` DECIMAL(5,2) NOT NULL,
  `salary` DECIMAL(7,2) NOT NULL,
  `holiday_balance` DECIMAL(4,2) NOT NULL DEFAULT 0,
  `under_contract` TINYINT NOT NULL DEFAULT 1,
  `work_time` DECIMAL NOT NULL DEFAULT 0,
  `password` VARCHAR(64) NOT NULL,
  `employee_id` INT NULL DEFAULT NULL,
  `address_id` INT NOT NULL,
  `job_id` INT NOT NULL,
  `department_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  INDEX `fk_employees_employees_idx` (`employee_id` ASC) VISIBLE,
  INDEX `fk_employees_addresses1_idx` (`address_id` ASC) VISIBLE,
  INDEX `fk_employees_job1_idx` (`job_id` ASC) VISIBLE,
  INDEX `fk_employees_departments1_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `fk_employees_employees`
    FOREIGN KEY (`employee_id`)
    REFERENCES `db_employees`.`employees` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employees_addresses1`
    FOREIGN KEY (`address_id`)
    REFERENCES `db_employees`.`addresses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employees_job1`
    FOREIGN KEY (`job_id`)
    REFERENCES `db_employees`.`jobs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employees_departments1`
    FOREIGN KEY (`department_id`)
    REFERENCES `db_employees`.`departments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_employees`.`payslips`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `db_employees`.`payslips` ;

CREATE TABLE IF NOT EXISTS `db_employees`.`payslips` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `file_path` VARCHAR(100) NOT NULL,
  `date` DATE NOT NULL,
  `employee_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `file_path_UNIQUE` (`file_path` ASC) VISIBLE,
  INDEX `fk_payslips_employees1_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `fk_payslips_employees1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `db_employees`.`employees` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_employees`.`tasks`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `db_employees`.`tasks` ;

CREATE TABLE IF NOT EXISTS `db_employees`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `project` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `description` TINYTEXT NULL DEFAULT NULL,
  `validation` TINYINT(1) NULL DEFAULT 0,
  `since` DATETIME NOT NULL,
  `until` DATETIME NOT NULL,
  `duration` TIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `unique_tasks` (`project` ASC, `title` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_employees`.`employee_has_task`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `db_employees`.`employee_has_task` ;

CREATE TABLE IF NOT EXISTS `db_employees`.`employee_has_task` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NOT NULL,
  `task_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_employees_has_tasks_tasks1_idx` (`task_id` ASC) VISIBLE,
  INDEX `fk_employees_has_tasks_employees1_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `fk_employee_has_task_employees1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `db_employees`.`employees` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employee_has_task_tasks1`
    FOREIGN KEY (`task_id`)
    REFERENCES `db_employees`.`tasks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
