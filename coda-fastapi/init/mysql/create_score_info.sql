CREATE TABLE IF NOT EXISTS `score_info`(
  `id` BIGINT NOT NULL AUTO_INCREMENT ,
  `score_name` VARCHAR(30) NOT NULL ,
  `user_id` BIGINT NOT NULL ,
  `score_url` VARCHAR(30) NOT NULL ,
  `thumbnail_url` VARCHAR(30) NOT NULL ,
  `created_at` DATETIME ,
  `updated_at` DATETIME ,
  `deleted_at` DATETIME ,
  `delete_flg` BOOLEAN ,
  PRIMARY KEY(`id`)
)