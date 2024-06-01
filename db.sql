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
  `currency_relation` decimal(10,2) NOT NULL,
  PRIMARY KEY (`currency_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.methods
CREATE TABLE IF NOT EXISTS `methods` (
  `method_id` int(3) NOT NULL AUTO_INCREMENT,
  `method_name` varchar(30) NOT NULL,
  `method_description` text NOT NULL,
  PRIMARY KEY (`method_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.monitor_delete_sales_details
CREATE TABLE IF NOT EXISTS `monitor_delete_sales_details` (
  `mdsd_id` int(10) NOT NULL AUTO_INCREMENT,
  `mdsd_date` datetime NOT NULL,
  `sale_detail_id` int(10) NOT NULL,
  `sale_id` int(10) DEFAULT NULL,
  `product_id` int(10) DEFAULT NULL,
  `currency_id` int(3) DEFAULT NULL,
  `method_id` int(3) DEFAULT NULL,
  `sale_detail_quantity` int(5) DEFAULT NULL,
  `user_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`mdsd_id`) USING BTREE,
  KEY `FK__sales_details` (`sale_detail_id`) USING BTREE,
  KEY `FK__users` (`user_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.monitor_update_sales_details
CREATE TABLE IF NOT EXISTS `monitor_update_sales_details` (
  `musd_id` int(10) NOT NULL AUTO_INCREMENT,
  `sale_detail_id` int(10) NOT NULL,
  `musd_date` datetime NOT NULL,
  `musd_atr` varchar(30) DEFAULT NULL,
  `musd_old_value` int(11) DEFAULT NULL,
  `musd_new_value` int(11) DEFAULT NULL,
  `user_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`musd_id`) USING BTREE,
  KEY `FK__sales_details` (`sale_detail_id`),
  KEY `FK__users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.products
CREATE TABLE IF NOT EXISTS `products` (
  `product_id` int(10) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(30) NOT NULL,
  `product_description` text NOT NULL,
  `product_date` datetime NOT NULL,
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
  `sale_date` datetime NOT NULL,
  `client_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  PRIMARY KEY (`sale_id`),
  KEY `FK__clients` (`client_id`),
  KEY `FK__users` (`user_id`),
  CONSTRAINT `FK__clients` FOREIGN KEY (`client_id`) REFERENCES `clients` (`client_id`) ON UPDATE CASCADE,
  CONSTRAINT `FK__users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.sales_details
CREATE TABLE IF NOT EXISTS `sales_details` (
  `sale_detail_id` int(10) NOT NULL AUTO_INCREMENT,
  `sale_id` int(10) NOT NULL,
  `product_id` int(10) NOT NULL,
  `currency_id` int(3) NOT NULL,
  `method_id` int(3) NOT NULL,
  `sale_detail_quantity` int(5) NOT NULL,
  PRIMARY KEY (`sale_detail_id`),
  KEY `FK__sales` (`sale_id`),
  KEY `FK__products` (`product_id`) USING BTREE,
  KEY `FK__currencys` (`currency_id`) USING BTREE,
  KEY `FK__methods` (`method_id`) USING BTREE,
  CONSTRAINT `FK__currencys` FOREIGN KEY (`currency_id`) REFERENCES `currencys` (`currency_id`),
  CONSTRAINT `FK__methods` FOREIGN KEY (`method_id`) REFERENCES `methods` (`method_id`),
  CONSTRAINT `FK__products` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON UPDATE CASCADE,
  CONSTRAINT `FK__sales` FOREIGN KEY (`sale_id`) REFERENCES `sales` (`sale_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla frikizone.users
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(10) NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `user_last_name` varchar(30) NOT NULL,
  `user_address` text NOT NULL,
  `user_password` varchar(64) NOT NULL,
  `user_salt` varchar(16) NOT NULL,
  `rol_id` int(2) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `FK_rols` (`rol_id`),
  CONSTRAINT `FK__rols` FOREIGN KEY (`rol_id`) REFERENCES `rols` (`rol_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para procedimiento frikizone.insert_into_musd
DELIMITER //
CREATE PROCEDURE `insert_into_musd`(
	IN `sale_detail_id` INT,
	IN `atr` TEXT,
	IN `old_v` INT,
	IN `new_v` INT
)
BEGIN
	INSERT INTO monitor_update_sales_details(sale_detail_id,musd_date,musd_atr,musd_old_value,musd_new_value)
	VALUES (sale_detail_id,NOW(),atr,old_v,new_v);
END//
DELIMITER ;

-- Volcando estructura para procedimiento frikizone.old_new_equal
DELIMITER //
CREATE PROCEDURE `old_new_equal`(
	IN `old_value` TEXT,
	IN `new_value` TEXT,
	OUT `result` BIT
)
BEGIN 
	 IF old_value = new_value THEN
        SET result = TRUE;
    ELSE
        SET result = FALSE;
    END IF;
END//
DELIMITER ;

-- Volcando estructura para procedimiento frikizone.procedure_musd
DELIMITER //
CREATE PROCEDURE `procedure_musd`(
	IN `sale_detail_id` INT,
	IN `atr` TEXT,
	IN `old_v` INT,
	IN `new_v` INT
)
BEGIN

CALL old_new_equal(new_v,old_v,@result);
IF @result = FALSE THEN 
CALL insert_into_musd(sale_detail_id,atr,old_v,new_v);
END IF;

END//
DELIMITER ;

-- Volcando estructura para disparador frikizone.sales_details_after_delete
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `sales_details_after_delete` AFTER DELETE ON `sales_details` FOR EACH ROW BEGIN
	INSERT INTO monitor_delete_sales_details
	(mdsd_date,sale_detail_id,sale_id,product_id,currency_id,method_id,sale_detail_quantity)
	VALUES (NOW(),OLD.sale_detail_id,OLD.sale_id,OLD.product_id,OLD.currency_id,OLD.method_id,OLD.sale_detail_quantity);
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- Volcando estructura para disparador frikizone.sales_details_after_update
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `sales_details_after_update` AFTER UPDATE ON `sales_details` FOR EACH ROW BEGIN
CALL procedure_musd(NEW.sale_detail_id,"sale_id",OLD.sale_id,NEW.sale_id);
CALL procedure_musd(NEW.sale_detail_id,"product_id",OLD.product_id,NEW.product_id);
CALL procedure_musd(NEW.sale_detail_id,"currency_id",OLD.currency_id,NEW.currency_id);
CALL procedure_musd(NEW.sale_detail_id,"method_id",OLD.method_id,NEW.method_id);
CALL procedure_musd(NEW.sale_detail_id,"sale_detail_quantity",OLD.sale_detail_quantity,NEW.sale_detail_quantity);
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
