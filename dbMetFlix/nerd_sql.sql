-- MySQL Script generated by MySQL Workbench
-- Sex 05 Jul 2019 16:07:16 -05
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema nerd_flix
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema nerd_flix
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `nerd_flix` DEFAULT CHARACTER SET utf8 ;
USE `nerd_flix` ;

-- -----------------------------------------------------
-- Table `nerd_flix`.`clients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nerd_flix`.`clients` (
  `CLI_ID` INT(10) NOT NULL AUTO_INCREMENT,
  `CLI_NAME` VARCHAR(75) NOT NULL,
  `CLI_RG` VARCHAR(7) NOT NULL,
  `CLI_CPF` VARCHAR(14) NOT NULL,
  `CLI_EMAIL` VARCHAR(50) NOT NULL,
  `CLI_RG_UF` VARCHAR(2) NULL,
  `CLI_RG_ORG` VARCHAR(45) NULL,
  PRIMARY KEY (`CLI_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nerd_flix`.`payments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nerd_flix`.`payments` (
  `PAY_ID` INT(10) NOT NULL AUTO_INCREMENT,
  `PAY_DATE` DATE NULL,
  `PAY_DAY` DATE NOT NULL,
  `PAY_PRICE` FLOAT NOT NULL,
  PRIMARY KEY (`PAY_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nerd_flix`.`plans`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nerd_flix`.`plans` (
  `PLA_ID` INT(10) NOT NULL AUTO_INCREMENT,
  `PLA_NAME` VARCHAR(100) NOT NULL,
  `PLA_QTN_SCREEN` INT(3) NOT NULL,
  `PLA_RESOLUTION` VARCHAR(10) NOT NULL,
  `PLA_PRICE` FLOAT NOT NULL,
  PRIMARY KEY (`PLA_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nerd_flix`.`contracts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nerd_flix`.`contracts` (
  `CON_ID` INT(10) NOT NULL AUTO_INCREMENT,
  `CON_DATE_INITIAL` DATE NOT NULL,
  `CON_DATE_FINAL` DATE NOT NULL,
  `CON_PAY_ID` INT(10) NOT NULL,
  `CON_PLA_ID` INT(10) NOT NULL,
  PRIMARY KEY (`CON_ID`),
  INDEX `fk_contracts_payments1_idx` (`CON_PAY_ID` ASC),
  INDEX `fk_contracts_plans1_idx` (`CON_PLA_ID` ASC),
  CONSTRAINT `fk_contracts_payments1`
    FOREIGN KEY (`CON_PAY_ID`)
    REFERENCES `nerd_flix`.`payments` (`PAY_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_contracts_plans1`
    FOREIGN KEY (`CON_PLA_ID`)
    REFERENCES `nerd_flix`.`plans` (`PLA_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nerd_flix`.`type_collection`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nerd_flix`.`type_collection` (
  `TYP_COL_ID` INT(10) NOT NULL AUTO_INCREMENT,
  `TYP_COL_NAME` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`TYP_COL_ID`))
ENGINE = InnoDB;


-- DATA TYPE COLLETION

INSERT INTO type_collection (TYP_COL_NAME) VALUES ('Documentário');
INSERT INTO type_collection (TYP_COL_NAME) VALUES ('Filme');
INSERT INTO type_collection (TYP_COL_NAME) VALUES ('Stand-UP');
INSERT INTO type_collection (TYP_COL_NAME) VALUES ('Serie');
INSERT INTO type_collection (TYP_COL_NAME) VALUES ('Curta-Metragem');
INSERT INTO type_collection (TYP_COL_NAME) VALUES ('Novela');
INSERT INTO type_collection (TYP_COL_NAME) VALUES ('Programa de TV');


-- -----------------------------------------------------
-- Table `nerd_flix`.`genre`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nerd_flix`.`genre` (
  `GEN_ID` INT(5) NOT NULL AUTO_INCREMENT,
  `GEN_NAME` VARCHAR(75) NOT NULL,
  PRIMARY KEY (`GEN_ID`))
ENGINE = InnoDB;

-- DATA GENRE

INSERT INTO genre (GEN_NAME) VALUES ('Ação');
INSERT INTO genre (GEN_NAME) VALUES ('Animação');
INSERT INTO genre (GEN_NAME) VALUES ('Cinema de arte');
INSERT INTO genre (GEN_NAME) VALUES ('Chanchada');
INSERT INTO genre (GEN_NAME) VALUES ('Cinema catástrofe');
INSERT INTO genre (GEN_NAME) VALUES ('Comédia');
INSERT INTO genre (GEN_NAME) VALUES ('Comédia romântica');
INSERT INTO genre (GEN_NAME) VALUES ('Comédia dramática');
INSERT INTO genre (GEN_NAME) VALUES ('Comédia de ação');
INSERT INTO genre (GEN_NAME) VALUES ('Dança');
INSERT INTO genre (GEN_NAME) VALUES ('Documentário');
INSERT INTO genre (GEN_NAME) VALUES ('Docuficção');
INSERT INTO genre (GEN_NAME) VALUES ('Drama');
INSERT INTO genre (GEN_NAME) VALUES ('Espionagem');
INSERT INTO genre (GEN_NAME) VALUES ('Faroeste');
INSERT INTO genre (GEN_NAME) VALUES ('Fantasia científica');
INSERT INTO genre (GEN_NAME) VALUES ('Ficção científica');
INSERT INTO genre (GEN_NAME) VALUES ('Guerra');
INSERT INTO genre (GEN_NAME) VALUES ('Musical');
INSERT INTO genre (GEN_NAME) VALUES ('Policial');
INSERT INTO genre (GEN_NAME) VALUES ('Romance');
INSERT INTO genre (GEN_NAME) VALUES ('Seriado');
INSERT INTO genre (GEN_NAME) VALUES ('Suspense');
INSERT INTO genre (GEN_NAME) VALUES ('Terror');


-- -----------------------------------------------------
-- Table `nerd_flix`.`collections`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nerd_flix`.`collections` (
  `COL_ID` INT(10) NOT NULL AUTO_INCREMENT,
  `COL_TITLE` VARCHAR(155) NULL,
  `COL_YEAR` INT(4) NULL,
  `COL_TYP_COL_ID` INT(4) NOT NULL,
  `COL_GEN_ID` INT(5) NOT NULL,
  `COL_PRODUCER_YEAR` INT(4) NULL,
  `COL_PRODUCER_NAME` VARCHAR(155) NULL,
  PRIMARY KEY (`COL_ID`),
  INDEX `fk_collections_type_collection_idx` (`COL_TYP_COL_ID` ASC),
  INDEX `fk_collections_genre1_idx` (`COL_GEN_ID` ASC),
  CONSTRAINT `fk_collections_type_collection`
    FOREIGN KEY (`COL_TYP_COL_ID`)
    REFERENCES `nerd_flix`.`type_collection` (`TYP_COL_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_collections_genre1`
    FOREIGN KEY (`COL_GEN_ID`)
    REFERENCES `nerd_flix`.`genre` (`GEN_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nerd_flix`.`rating`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nerd_flix`.`rating` (
  `RAT_ID` INT(10) NOT NULL AUTO_INCREMENT,
  `RAT_COL_ID` INT(10) NOT NULL,
  `RAT_CLI_ID` INT(10) NOT NULL,
  `RAT_VALUE` INT(1) NOT NULL,
  PRIMARY KEY (`RAT_ID`),
  INDEX `fk_rating_collections1_idx` (`RAT_COL_ID` ASC),
  INDEX `fk_rating_clients1_idx` (`RAT_CLI_ID` ASC),
  CONSTRAINT `fk_rating_collections1`
    FOREIGN KEY (`RAT_COL_ID`)
    REFERENCES `nerd_flix`.`collections` (`COL_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_rating_clients1`
    FOREIGN KEY (`RAT_CLI_ID`)
    REFERENCES `nerd_flix`.`clients` (`CLI_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nerd_flix`.`access_control`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nerd_flix`.`access_control` (
  `ACC_ID` INT(10) NOT NULL AUTO_INCREMENT,
  `ACC_CLI_ID` INT(10) NOT NULL,
  `ACC_COL_ID` INT(10) NOT NULL,
  `ACC_CON_ID` INT(10) NOT NULL,
  `ACC_DATE_VIEW` DATETIME NOT NULL,
  PRIMARY KEY (`ACC_ID`),
  INDEX `fk_access_control_clients1_idx` (`ACC_CLI_ID` ASC),
  INDEX `fk_access_control_collections1_idx` (`ACC_COL_ID` ASC),
  INDEX `fk_access_control_contracts1_idx` (`ACC_CON_ID` ASC),
  CONSTRAINT `fk_access_control_clients1`
    FOREIGN KEY (`ACC_CLI_ID`)
    REFERENCES `nerd_flix`.`clients` (`CLI_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_access_control_collections1`
    FOREIGN KEY (`ACC_COL_ID`)
    REFERENCES `nerd_flix`.`collections` (`COL_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_access_control_contracts1`
    FOREIGN KEY (`ACC_CON_ID`)
    REFERENCES `nerd_flix`.`contracts` (`CON_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
