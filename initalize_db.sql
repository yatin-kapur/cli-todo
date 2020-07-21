CREATE DATABASE todo;

USE todo;

CREATE TABLE `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `task` varchar(150) NOT NULL,
  `finish_by` date NOT NULL,
  `completed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
);
