CREATE TABLE `action_monitor` (
  `am_id` int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `am_name` varchar(30) NOT NULL
);

CREATE TABLE `monitor_sales_details` (
  `msd_id` int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `sale_detail_id` int(10) NOT NULL DEFAULT 0,
  `am_id` int(10) NOT NULL DEFAULT 1,
  `msd_date` date DEFAULT null
);

CREATE TABLE `clients` (
  `client_id` int(10) PRIMARY KEY NOT NULL,
  `client_name` varchar(30) NOT NULL,
  `client_lastname` varchar(30) NOT NULL,
  `client_address` text NOT NULL
);

CREATE TABLE `products` (
  `product_id` int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `product_name` varchar(30) NOT NULL,
  `product_description` text NOT NULL,
  `product_date` date NOT NULL,
  `product_value` decimal(10,2) NOT NULL
);

CREATE TABLE `sales` (
  `sale_id` int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `sale_date` date NOT NULL,
  `client_id` int(10) NOT NULL DEFAULT 0,
  `employee_id` int(10) NOT NULL DEFAULT 1
);

CREATE TABLE `currencys` (
  `currency_id` int(3) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `currency_name` varchar(30) NOT NULL,
  `currency_relation` decimal(10,2)
);

CREATE TABLE `methods` (
  `method_id` int(3) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `method_name` varchar(30) NOT NULL,
  `method_description` text NOT NULL
);

CREATE TABLE `sales_details` (
  `sale_detail_id` int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `sale_id` int(10) NOT NULL DEFAULT 0,
  `product_id` int(10) NOT NULL DEFAULT 1,
  `currency_id` int(3) NOT NULL DEFAULT 2,
  `method_id` int(3) NOT NULL DEFAULT 3,
  `sale_detail_quantity` int(5) NOT NULL
);

CREATE TABLE `employees` (
  `employee_id` int(10) PRIMARY KEY NOT NULL,
  `employee_name` varchar(30) NOT NULL,
  `employee_last_name` varchar(30) NOT NULL,
  `employee_address` text NOT NULL,
  `employee_password` varchar(64),
  `employee_salt` varchar(16),
  `rol_id` int(2) NOT NULL DEFAULT 0
);

CREATE TABLE `rols` (
  `rol_id` int(2) PRIMARY KEY NOT NULL,
  `rol_name` varchar(30) NOT NULL,
  `rol_permissions` bool NOT NULL
);

CREATE INDEX `FK__sales_details` ON `monitor_sales_details` (`sale_detail_id`);

CREATE INDEX `FK__action_monitor` ON `monitor_sales_details` (`am_id`);

CREATE INDEX `FK__clients` ON `sales` (`client_id`);

CREATE INDEX `FK_sellers` ON `sales` (`employee_id`);

CREATE INDEX `FK__sales` ON `sales_details` (`sale_id`);

CREATE INDEX `FK_products` ON `sales_details` (`product_id`);

CREATE INDEX `FK_currencys` ON `sales_details` (`currency_id`);

CREATE INDEX `FK_methods` ON `sales_details` (`method_id`);

CREATE INDEX `FK_rols` ON `employees` (`rol_id`);

ALTER TABLE `monitor_sales_details` ADD FOREIGN KEY (`sale_detail_id`) REFERENCES `sales_details` (`sale_detail_id`);

ALTER TABLE `monitor_sales_details` ADD CONSTRAINT `FK__action_monitor` FOREIGN KEY (`am_id`) REFERENCES `action_monitor` (`am_id`);

ALTER TABLE `sales` ADD CONSTRAINT `FK__clients` FOREIGN KEY (`client_id`) REFERENCES `clients` (`client_id`);

ALTER TABLE `sales_details` ADD CONSTRAINT `FK__sales` FOREIGN KEY (`sale_id`) REFERENCES `sales` (`sale_id`);

ALTER TABLE `sales_details` ADD FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`);

ALTER TABLE `sales_details` ADD CONSTRAINT `FK__currencys` FOREIGN KEY (`currency_id`) REFERENCES `currencys` (`currency_id`);

ALTER TABLE `sales_details` ADD CONSTRAINT `FK__methods` FOREIGN KEY (`method_id`) REFERENCES `methods` (`method_id`);

ALTER TABLE `sales` ADD CONSTRAINT `FK_sellers` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`);

ALTER TABLE `employees` ADD FOREIGN KEY (`rol_id`) REFERENCES `rols` (`rol_id`);
