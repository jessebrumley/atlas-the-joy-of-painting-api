CREATE TABLE `paintings` (
  `painting_id` INT AUTO_INCREMENT PRIMARY KEY,
  `season` INT NOT NULL,
  `episode` INT NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `date` DATE NOT NULL,
  `num_colors` INT,
  `youtube_src` VARCHAR(255)
);

CREATE TABLE `colors` (
  `color_id` INT AUTO_INCREMENT PRIMARY KEY,
  `painting_id` INT NOT NULL,
  `color_name` VARCHAR(50) NOT NULL,
  `color_hex` CHAR(7) NOT NULL,
  FOREIGN KEY (`painting_id`) REFERENCES `paintings` (`painting_id`)
);

CREATE TABLE `subject_matter` (
  `subject_id` INT AUTO_INCREMENT PRIMARY KEY,
  `painting_id` INT NOT NULL,
  `subject_name` VARCHAR(255) NOT NULL,
  FOREIGN KEY (`painting_id`) REFERENCES `paintings` (`painting_id`)
);
