CREATE TABLE `todolistdb`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(85) NOT NULL,
  `is_finished` TINYINT NULL,
  PRIMARY KEY (`id`));