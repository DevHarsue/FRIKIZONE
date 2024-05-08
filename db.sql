-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         11.3.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para frikizone
CREATE DATABASE IF NOT EXISTS `frikizone` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `frikizone`;

-- Volcando estructura para tabla frikizone.action_monitor
CREATE TABLE IF NOT EXISTS `action_monitor` (
  `am_id` int(10) NOT NULL AUTO_INCREMENT,
  `am_name` varchar(30) NOT NULL,
  PRIMARY KEY (`am_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.clients
CREATE TABLE IF NOT EXISTS `clients` (
  `client_id` int(10) NOT NULL,
  `client_name` varchar(30) NOT NULL,
  `client_lastname` varchar(30) NOT NULL,
  `client_address` text NOT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.currencys
CREATE TABLE IF NOT EXISTS `currencys` (
  `currency_id` int(3) NOT NULL AUTO_INCREMENT,
  `currency_name` varchar(30) NOT NULL,
  `currency_relation` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`currency_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.employees
CREATE TABLE IF NOT EXISTS `employees` (
  `employee_id` int(10) NOT NULL,
  `employee_name` varchar(30) NOT NULL,
  `employee_last_name` varchar(30) NOT NULL,
  `employee_address` text NOT NULL,
  `employee_password` varchar(64) DEFAULT NULL,
  `employee_salt` varchar(16) DEFAULT NULL,
  `rol_id` int(2) NOT NULL DEFAULT 0,
  PRIMARY KEY (`employee_id`),
  KEY `FK_rols` (`rol_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rols` (`rol_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.methods
CREATE TABLE IF NOT EXISTS `methods` (
  `method_id` int(3) NOT NULL AUTO_INCREMENT,
  `method_name` varchar(30) NOT NULL,
  `method_description` text NOT NULL,
  PRIMARY KEY (`method_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.monitor_sales_details
CREATE TABLE IF NOT EXISTS `monitor_sales_details` (
  `msd_id` int(10) NOT NULL AUTO_INCREMENT,
  `sale_detail_id` int(10) NOT NULL DEFAULT 0,
  `am_id` int(10) NOT NULL DEFAULT 1,
  `msd_date` date DEFAULT NULL,
  PRIMARY KEY (`msd_id`),
  KEY `FK__sales_details` (`sale_detail_id`),
  KEY `FK__action_monitor` (`am_id`),
  CONSTRAINT `FK__action_monitor` FOREIGN KEY (`am_id`) REFERENCES `action_monitor` (`am_id`),
  CONSTRAINT `monitor_sales_details_ibfk_1` FOREIGN KEY (`sale_detail_id`) REFERENCES `sales_details` (`sale_detail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.products
CREATE TABLE IF NOT EXISTS `products` (
  `product_id` int(10) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(30) NOT NULL,
  `product_description` text NOT NULL,
  `product_date` date NOT NULL,
  `product_value` decimal(10,2) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.rols
CREATE TABLE IF NOT EXISTS `rols` (
  `rol_id` int(2) NOT NULL AUTO_INCREMENT,
  `rol_name` varchar(30) NOT NULL,
  `rol_permissions` text NOT NULL,
  PRIMARY KEY (`rol_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.sales
CREATE TABLE IF NOT EXISTS `sales` (
  `sale_id` int(10) NOT NULL AUTO_INCREMENT,
  `sale_date` date NOT NULL,
  `client_id` int(10) NOT NULL DEFAULT 0,
  `employee_id` int(10) NOT NULL DEFAULT 1,
  PRIMARY KEY (`sale_id`),
  KEY `FK__clients` (`client_id`),
  KEY `FK_sellers` (`employee_id`),
  CONSTRAINT `FK__clients` FOREIGN KEY (`client_id`) REFERENCES `clients` (`client_id`),
  CONSTRAINT `FK_sellers` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.sales_details
CREATE TABLE IF NOT EXISTS `sales_details` (
  `sale_detail_id` int(10) NOT NULL AUTO_INCREMENT,
  `sale_id` int(10) NOT NULL DEFAULT 0,
  `product_id` int(10) NOT NULL DEFAULT 1,
  `currency_id` int(3) NOT NULL DEFAULT 2,
  `method_id` int(3) NOT NULL DEFAULT 3,
  `sale_detail_quantity` int(5) NOT NULL,
  PRIMARY KEY (`sale_detail_id`),
  KEY `FK__sales` (`sale_id`),
  KEY `FK_products` (`product_id`),
  KEY `FK_currencys` (`currency_id`),
  KEY `FK_methods` (`method_id`),
  CONSTRAINT `FK__currencys` FOREIGN KEY (`currency_id`) REFERENCES `currencys` (`currency_id`),
  CONSTRAINT `FK__methods` FOREIGN KEY (`method_id`) REFERENCES `methods` (`method_id`),
  CONSTRAINT `FK__sales` FOREIGN KEY (`sale_id`) REFERENCES `sales` (`sale_id`),
  CONSTRAINT `sales_details_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
