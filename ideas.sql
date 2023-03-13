-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema ideas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ideas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ideas` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `ideas` ;

-- -----------------------------------------------------
-- Table `ideas`.`type_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ideas`.`type_user` (
  `idtipo` INT NOT NULL,
  `description` VARCHAR(45) NULL,
  PRIMARY KEY (`idtipo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ideas`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ideas`.`users` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL DEFAULT NULL,
  `last_name` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(500) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `type` VARCHAR(10) NULL,
  `type_user` INT NOT NULL,
  PRIMARY KEY (`iduser`),
  INDEX `fk_users_type_user_idx` (`type_user` ASC) VISIBLE,
  CONSTRAINT `fk_users_type_user`
    FOREIGN KEY (`type_user`)
    REFERENCES `ideas`.`type_user` (`idtipo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ideas`.`strategies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ideas`.`strategies` (
  `idstrategy` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`idstrategy`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ideas`.`campaigns`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ideas`.`campaigns` (
  `idcampaign` INT NOT NULL AUTO_INCREMENT,
  `name_campaing` VARCHAR(150) NULL,
  `description` TEXT NULL,
  `id_strategy` INT NOT NULL,
  PRIMARY KEY (`idcampaign`),
  INDEX `fk_campaigns_strategies1_idx` (`id_strategy` ASC) VISIBLE,
  CONSTRAINT `fk_campaigns_strategies1`
    FOREIGN KEY (`id_strategy`)
    REFERENCES `ideas`.`strategies` (`idstrategy`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ideas`.`cluster`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ideas`.`cluster` (
  `idcluster` INT NOT NULL AUTO_INCREMENT,
  `name_cluster` VARCHAR(150) NULL,
  `id_campaign` INT NOT NULL,
  PRIMARY KEY (`idcluster`),
  INDEX `fk_cluster_campaigns1_idx` (`id_campaign` ASC) VISIBLE,
  CONSTRAINT `fk_cluster_campaigns1`
    FOREIGN KEY (`id_campaign`)
    REFERENCES `ideas`.`campaigns` (`idcampaign`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ideas`.`ideas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ideas`.`ideas` (
  `idideas` INT NOT NULL AUTO_INCREMENT,
  `content` TEXT NULL,
  `user_id` INT NOT NULL,
  `id_cluster` INT NOT NULL,
  PRIMARY KEY (`idideas`),
  INDEX `fk_ideas_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_ideas_cluster1_idx` (`id_cluster` ASC) VISIBLE,
  CONSTRAINT `fk_ideas_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `ideas`.`users` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ideas_cluster1`
    FOREIGN KEY (`id_cluster`)
    REFERENCES `ideas`.`cluster` (`idcluster`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ideas`.`ratings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ideas`.`ratings` (
  `idratings` INT NOT NULL AUTO_INCREMENT,
  `score` VARCHAR(150) NULL,
  `id_user` INT NOT NULL,
  PRIMARY KEY (`idratings`),
  INDEX `fk_ratings_users1_idx` (`id_user` ASC) VISIBLE,
  CONSTRAINT `fk_ratings_users1`
    FOREIGN KEY (`id_user`)
    REFERENCES `ideas`.`users` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ideas`.`initiative`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ideas`.`initiative` (
  `idinitiative` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NULL,
  `id_cluster` INT NOT NULL,
  PRIMARY KEY (`idinitiative`),
  INDEX `fk_initiative_cluster1_idx` (`id_cluster` ASC) VISIBLE,
  CONSTRAINT `fk_initiative_cluster1`
    FOREIGN KEY (`id_cluster`)
    REFERENCES `ideas`.`cluster` (`idcluster`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ideas`.`hypothesis`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ideas`.`hypothesis` (
  `idhypothesis` INT NOT NULL AUTO_INCREMENT,
  `hypothesis` VARCHAR(255) NULL,
  `experiment` VARCHAR(255) NULL,
  `learning` VARCHAR(255) NULL,
  `id_initiative` INT NOT NULL,
  PRIMARY KEY (`idhypothesis`),
  INDEX `fk_hypothesis_initiative1_idx` (`id_initiative` ASC) VISIBLE,
  CONSTRAINT `fk_hypothesis_initiative1`
    FOREIGN KEY (`id_initiative`)
    REFERENCES `ideas`.`initiative` (`idinitiative`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
