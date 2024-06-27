/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS `frikizone` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `frikizone`;

CREATE TABLE IF NOT EXISTS `clientes` (
  `cliente_id` int(11) NOT NULL,
  `cliente_nacionalidad` varchar(1) NOT NULL,
  `cliente_nombre` varchar(30) NOT NULL,
  `cliente_apellido` varchar(30) DEFAULT NULL,
  `cliente_direccion` text DEFAULT NULL,
  `cliente_telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cliente_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


CREATE TABLE IF NOT EXISTS `divisas` (
  `divisa_id` int(11) NOT NULL AUTO_INCREMENT,
  `divisa_nombre` varchar(30) NOT NULL,
  `divisa_relacion` decimal(20,2) NOT NULL,
  PRIMARY KEY (`divisa_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `divisas` (`divisa_id`, `divisa_nombre`, `divisa_relacion`) VALUES
	(1, 'BOLIVAR', 36.00),
	(2, 'COP', 3700.00),
	(3, 'DOLAR', 1.00);

CREATE TABLE IF NOT EXISTS `productos` (
  `producto_id` int(11) NOT NULL AUTO_INCREMENT,
  `producto_nombre` varchar(30) NOT NULL,
  `producto_descripcion` text DEFAULT NULL,
  `producto_valor` decimal(20,2) NOT NULL,
  PRIMARY KEY (`producto_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


CREATE TABLE IF NOT EXISTS `roles` (
  `rol_id` int(11) NOT NULL AUTO_INCREMENT,
  `rol_nombre` varchar(30) NOT NULL,
  `rol_permisos` text NOT NULL,
  PRIMARY KEY (`rol_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `roles` (`rol_id`, `rol_nombre`, `rol_permisos`) VALUES
	(1, 'SUPERADMIN', 'XD');

CREATE TABLE IF NOT EXISTS `totales_diarios` (
  `total_diario_id` int(11) NOT NULL AUTO_INCREMENT,
  `total_diario_fecha` date NOT NULL,
  `divisa_id` int(11) NOT NULL,
  `total_diario_cantidad` decimal(20,2) NOT NULL,
  PRIMARY KEY (`total_diario_id`) USING BTREE,
  KEY `FK_diarios_divisas` (`divisa_id`),
  CONSTRAINT `FK_diarios_divisas` FOREIGN KEY (`divisa_id`) REFERENCES `divisas` (`divisa_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


CREATE TABLE IF NOT EXISTS `usuarios` (
  `usuario_id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_nombre` varchar(30) NOT NULL,
  `usuario_contraseña` varchar(64) NOT NULL,
  `rol_id` int(11) NOT NULL,
  PRIMARY KEY (`usuario_id`),
  KEY `FK__rols` (`rol_id`) USING BTREE,
  CONSTRAINT `FK__rols` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`rol_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `usuarios` (`usuario_id`, `usuario_nombre`, `usuario_contraseña`, `rol_id`) VALUES
	(1, '999', '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2', 1);

CREATE TABLE IF NOT EXISTS `ventas` (
  `venta_id` int(11) NOT NULL AUTO_INCREMENT,
  `venta_fecha` date NOT NULL DEFAULT current_timestamp(),
  `usuario_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  PRIMARY KEY (`venta_id`),
  KEY `fk_ventas_usuario` (`usuario_id`),
  KEY `fk_clientes_id` (`cliente_id`),
  CONSTRAINT `fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`cliente_id`),
  CONSTRAINT `fk_ventas_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


CREATE TABLE IF NOT EXISTS `ventas_ingresos` (
  `venta_ingreso_id` int(11) NOT NULL AUTO_INCREMENT,
  `venta_id` int(11) NOT NULL,
  `divisa_id` int(11) NOT NULL,
  `venta_ingreso_cantidad` decimal(20,2) NOT NULL,
  PRIMARY KEY (`venta_ingreso_id`),
  KEY `FK_ventas_ingresos_ventas` (`venta_id`),
  CONSTRAINT `FK_ventas_ingresos_ventas` FOREIGN KEY (`venta_id`) REFERENCES `ventas` (`venta_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


CREATE TABLE IF NOT EXISTS `ventas_productos` (
  `venta_producto_id` int(11) NOT NULL AUTO_INCREMENT,
  `venta_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `venta_producto_cantidad` int(11) NOT NULL,
  PRIMARY KEY (`venta_producto_id`) USING BTREE,
  KEY `FK__ventas` (`venta_id`) USING BTREE,
  KEY `FK__productos` (`producto_id`) USING BTREE,
  CONSTRAINT `fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`producto_id`),
  CONSTRAINT `fk_venta_id` FOREIGN KEY (`venta_id`) REFERENCES `ventas` (`venta_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
