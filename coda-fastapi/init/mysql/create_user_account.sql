CREATE TABLE IF NOT EXISTS `user_account`(
  `id` BIGINT NOT NULL AUTO_INCREMENT ,
  `user_name` VARCHAR(20) NOT NULL ,
  `password` VARCHAR(20) NOT NULL ,
  PRIMARY KEY(`id`),
  UNIQUE KEY `user_name` (`user_name`)
)