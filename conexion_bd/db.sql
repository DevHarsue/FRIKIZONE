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
  `cliente_id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_cedula` int(11) NOT NULL,
  `cliente_nacionalidad` varchar(1) NOT NULL,
  `cliente_nombre` varchar(30) NOT NULL,
  `cliente_apellido` varchar(30) DEFAULT NULL,
  `cliente_direccion` text DEFAULT NULL,
  `cliente_telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cliente_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `clientes` (`cliente_id`, `cliente_cedula`, `cliente_nacionalidad`, `cliente_nombre`, `cliente_apellido`, `cliente_direccion`, `cliente_telefono`) VALUES
	(3, 32325849, 'V', 'HARWING', 'MARTINEZ', '', '04161797833'),
	(4, 30982001, 'V', 'JOSE', 'DAZA', '', '041625424214');

CREATE TABLE IF NOT EXISTS `divisas` (
  `divisa_id` int(11) NOT NULL AUTO_INCREMENT,
  `divisa_nombre` varchar(30) NOT NULL,
  `divisa_relacion` decimal(20,2) NOT NULL,
  PRIMARY KEY (`divisa_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `divisas` (`divisa_id`, `divisa_nombre`, `divisa_relacion`) VALUES
	(1, 'BOLIVAR', 36.00),
	(2, 'COP', 4700.00),
	(3, 'DOLAR', 1.00);

CREATE TABLE IF NOT EXISTS `productos` (
  `producto_id` int(11) NOT NULL AUTO_INCREMENT,
  `producto_nombre` varchar(30) NOT NULL,
  `producto_descripcion` text DEFAULT NULL,
  `producto_valor` decimal(20,2) NOT NULL,
  PRIMARY KEY (`producto_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `productos` (`producto_id`, `producto_nombre`, `producto_descripcion`, `producto_valor`) VALUES
	(5, 'Franelas', ',wdgqwkgfqjdhshsjb hasgnsz dshvxz chavdnasg vub vandmvgrwf', 1.00),
	(7, 'ZAPOs', '', 3.00),
	(8, 'Calzon', 'Noc', 1.50);

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
  `usuario_nombre` varchar(64) NOT NULL,
  `usuario_contraseña` varchar(64) NOT NULL,
  `usuario_rol` varchar(64) NOT NULL,
  PRIMARY KEY (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `usuarios` (`usuario_id`, `usuario_nombre`, `usuario_contraseña`, `usuario_rol`) VALUES
	(1, '999', '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2', 'SUPERADMIN');

CREATE TABLE IF NOT EXISTS `ventas` (
  `venta_id` int(11) NOT NULL AUTO_INCREMENT,
  `venta_fecha` date NOT NULL DEFAULT current_timestamp(),
  `cliente_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`venta_id`),
  KEY `fk_ventas_usuario` (`usuario_id`),
  KEY `fk_clientes_id` (`cliente_id`),
  CONSTRAINT `fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`cliente_id`),
  CONSTRAINT `fk_ventas_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `ventas` (`venta_id`, `venta_fecha`, `cliente_id`, `usuario_id`) VALUES
	(38, '2024-06-30', 4, 1),
	(39, '2024-06-30', 3, 1),
	(40, '2024-06-30', 3, 1),
	(41, '2024-06-30', 3, 1),
	(42, '2024-06-30', 4, 1),
	(43, '2024-06-30', 4, 1),
	(44, '2024-06-30', 4, 1),
	(45, '2024-06-30', 4, 1),
	(46, '2024-06-30', 3, 1);

CREATE TABLE IF NOT EXISTS `ventas_ingresos` (
  `venta_ingreso_id` int(11) NOT NULL AUTO_INCREMENT,
  `venta_id` int(11) NOT NULL,
  `divisa_id` int(11) NOT NULL,
  `venta_ingreso_cantidad` decimal(20,2) NOT NULL,
  PRIMARY KEY (`venta_ingreso_id`),
  KEY `FK_ventas_ingresos_ventas` (`venta_id`),
  CONSTRAINT `FK_ventas_ingresos_ventas` FOREIGN KEY (`venta_id`) REFERENCES `ventas` (`venta_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `ventas_ingresos` (`venta_ingreso_id`, `venta_id`, `divisa_id`, `venta_ingreso_cantidad`) VALUES
	(109, 38, 1, 514.80),
	(110, 38, 2, 8000.00),
	(111, 38, 3, 13.00),
	(112, 39, 1, 0.00),
	(113, 39, 2, 0.00),
	(114, 39, 3, 5.80),
	(115, 40, 1, 626.40),
	(116, 40, 2, 0.00),
	(117, 40, 3, 12.18),
	(118, 41, 1, 856.08),
	(119, 41, 2, 0.00),
	(120, 41, 3, 0.00),
	(121, 42, 1, 300.96),
	(122, 42, 2, 20000.00),
	(123, 42, 3, 10.00),
	(124, 43, 1, 250.56),
	(125, 43, 2, 0.00),
	(126, 43, 3, 0.00),
	(127, 44, 1, 626.40),
	(128, 44, 2, 0.00),
	(129, 44, 3, 0.00),
	(130, 45, 1, 0.00),
	(131, 45, 2, 81800.00),
	(132, 45, 3, 0.00),
	(133, 46, 1, 0.00),
	(134, 46, 2, 65400.00),
	(135, 46, 3, 0.00);

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

INSERT INTO `ventas_productos` (`venta_producto_id`, `venta_id`, `producto_id`, `venta_producto_cantidad`) VALUES
	(47, 38, 5, 13),
	(48, 38, 7, 2),
	(49, 38, 8, 4),
	(50, 39, 5, 5),
	(51, 40, 8, 7),
	(52, 40, 7, 5),
	(53, 41, 8, 5),
	(54, 41, 7, 3),
	(55, 41, 5, 4),
	(56, 42, 5, 6),
	(57, 42, 8, 3),
	(58, 42, 7, 3),
	(59, 43, 8, 4),
	(60, 44, 7, 5),
	(61, 45, 7, 5),
	(62, 46, 7, 4);

DELIMITER //
CREATE PROCEDURE `calcular_cliente`(
	IN `año` VARCHAR(4),
	IN `mes` VARCHAR(2)
)
BEGIN
SELECT c.cliente_id,concat(cliente_nacionalidad,cliente_cedula) cedula, c.cliente_nombre,c.cliente_apellido,vi.divisa_id,SUM(venta_ingreso_cantidad) AS total
FROM ventas_ingresos vi JOIN ventas v JOIN clientes c
ON vi.venta_id=v.venta_id AND v.cliente_id = c.cliente_id
WHERE v.venta_fecha>= CONCAT(año,"-",mes,"-00") AND v.venta_fecha <= CONCAT(año,"-",mes,"-31")
GROUP BY c.cliente_id,divisa_id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `calcular_diario`(
	IN `fecha` DATE
)
BEGIN
SELECT divisa_id,SUM(venta_ingreso_cantidad) total FROM 
ventas v JOIN ventas_ingresos vi ON v.venta_id=vi.venta_id
WHERE venta_fecha = fecha
GROUP BY divisa_id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `calcular_frecuencia_clientes`(
	IN `año` VARCHAR(4),
	IN `mes` VARCHAR(2)
)
BEGIN
SELECT cliente_id,count(cliente_id) AS veces FROM ventas
WHERE venta_fecha> CONCAT(año,"-",mes,"-00") AND venta_fecha <= CONCAT(año,"-",mes,"-31")
GROUP BY cliente_id
ORDER BY veces DESC;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `calcular_mes`(
	IN `año` VARCHAR(4),
	IN `mes` VARCHAR(2)
)
BEGIN
SELECT divisa_id,SUM(venta_ingreso_cantidad) total FROM 
ventas v JOIN ventas_ingresos vi ON v.venta_id=vi.venta_id
WHERE v.venta_fecha> CONCAT(año,"-",mes,"-00") AND v.venta_fecha <= CONCAT(año,"-",mes,"-31")
GROUP BY divisa_id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `calcular_producto_mes`(
	IN `año` VARCHAR(4),
	IN `mes` VARCHAR(2)
)
BEGIN
SELECT p.producto_id,producto_nombre,SUM(venta_producto_cantidad) total FROM 
ventas_productos vp JOIN ventas v JOIN productos p
ON vp.venta_id=v.venta_id AND vp.producto_id=p.producto_id
WHERE v.venta_fecha> CONCAT(año,"-",mes,"-00") AND v.venta_fecha <= CONCAT(año,"-",mes,"-31")
GROUP BY p.producto_id
ORDER BY total DESC;
END//
DELIMITER ;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
