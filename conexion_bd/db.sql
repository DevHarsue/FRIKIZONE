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

CREATE TABLE IF NOT EXISTS `auditoria_actualizar_detalles_ventas` (
  `adv_id` int(11) NOT NULL AUTO_INCREMENT,
  `venta_detalle_id` int(11) NOT NULL,
  `adv_fecha` datetime NOT NULL,
  `adv_columna` varchar(30) NOT NULL,
  `adv_viejo_valor` int(11) NOT NULL,
  `adv_nuevo_valor` int(11) NOT NULL,
  `usuario_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`adv_id`) USING BTREE,
  KEY `FK__usuarios` (`usuario_id`) USING BTREE,
  KEY `FK__ventas_detalles` (`venta_detalle_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `auditoria_borrar_detalles_ventas` (
  `bdv_id` int(11) NOT NULL AUTO_INCREMENT,
  `venta_detalle_id` int(11) NOT NULL,
  `bdv_fecha` datetime NOT NULL,
  `venta_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `divisa_id` int(11) NOT NULL,
  `metodo_id` int(11) NOT NULL,
  `venta_detalle_cantidad` int(11) NOT NULL,
  `usuarios_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`bdv_id`) USING BTREE,
  KEY `FK__ventas_detalles` (`venta_detalle_id`) USING BTREE,
  KEY `FK__usuarios` (`usuarios_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `clientes` (
  `cliente_id` int(11) NOT NULL,
  `cliente_nombre` varchar(30) NOT NULL,
  `cliente_apellido` varchar(30) NOT NULL,
  `cliente_direccion` text DEFAULT NULL,
  `cliente_telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cliente_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `divisas` (
  `divisa_id` int(11) NOT NULL AUTO_INCREMENT,
  `divisa_nombre` varchar(30) NOT NULL,
  `divisa_relacion` decimal(10,2) NOT NULL,
  PRIMARY KEY (`divisa_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `metodos` (
  `metodo_id` int(11) NOT NULL AUTO_INCREMENT,
  `metodo_nombre` varchar(30) NOT NULL,
  `metodo_descripcion` text NOT NULL,
  PRIMARY KEY (`metodo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `productos` (
  `producto_id` int(11) NOT NULL AUTO_INCREMENT,
  `producto_nombre` varchar(30) NOT NULL,
  `producto_descripcion` text NOT NULL,
  `producto_valor` decimal(10,2) NOT NULL,
  PRIMARY KEY (`producto_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `roles` (
  `rol_id` int(11) NOT NULL AUTO_INCREMENT,
  `rol_nombre` varchar(30) NOT NULL,
  `rol_permisos` text NOT NULL,
  PRIMARY KEY (`rol_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `usuarios` (
  `usuario_id` int(11) NOT NULL,
  `usuario_nombre` varchar(30) NOT NULL,
  `usuario_apellido` varchar(30) NOT NULL,
  `usuario_direccion` text NOT NULL,
  `usuario_telefono` varchar(20) NOT NULL DEFAULT '',
  `usuario_contraseña` varchar(64) NOT NULL,
  `usuario_salt` varchar(16) NOT NULL,
  `rol_id` int(11) NOT NULL,
  PRIMARY KEY (`usuario_id`),
  KEY `FK__rols` (`rol_id`) USING BTREE,
  CONSTRAINT `FK__rols` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`rol_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `ventas` (
  `venta_id` int(11) NOT NULL AUTO_INCREMENT,
  `venta_fecha` datetime NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  PRIMARY KEY (`venta_id`),
  KEY `fk_ventas_usuario` (`usuario_id`),
  KEY `fk_clientes_id` (`cliente_id`),
  CONSTRAINT `fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`cliente_id`),
  CONSTRAINT `fk_ventas_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `ventas_detalles` (
  `venta_detalle_id` int(11) NOT NULL AUTO_INCREMENT,
  `venta_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `divisa_id` int(11) NOT NULL,
  `metodo_id` int(11) NOT NULL,
  `venta_detalle_cantidad` int(11) NOT NULL,
  PRIMARY KEY (`venta_detalle_id`) USING BTREE,
  KEY `FK__ventas` (`venta_id`) USING BTREE,
  KEY `FK__productos` (`producto_id`) USING BTREE,
  KEY `FK__divisas` (`divisa_id`) USING BTREE,
  KEY `FK__metodos` (`metodo_id`) USING BTREE,
  CONSTRAINT `fk_divisa_id` FOREIGN KEY (`divisa_id`) REFERENCES `divisas` (`divisa_id`),
  CONSTRAINT `fk_metodo_id` FOREIGN KEY (`metodo_id`) REFERENCES `metodos` (`metodo_id`),
  CONSTRAINT `fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`producto_id`),
  CONSTRAINT `fk_venta_id` FOREIGN KEY (`venta_id`) REFERENCES `ventas` (`venta_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

DELIMITER //
CREATE PROCEDURE `insertar_en_adv`(
	IN `venta_detalle_id` INT,
	IN `col` TEXT,
	IN `viejo_v` INT,
	IN `nuevo_v` INT
)
BEGIN
	INSERT INTO auditoria_actualizar_detalles_ventas(venta_detalle_id,adv_fecha,adv_columna,adv_viejo_valor,adv_nuevo_valor)
	VALUES (venta_detalle_id,NOW(),col,viejo_v,nuevo_v);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `procedimiento_adv`(
	IN `venta_detalle_id` INT,
	IN `col` TEXT,
	IN `viejo_v` INT,
	IN `nuevo_v` INT
)
BEGIN

CALL viejo_nuevo_igual(nuevo_v,viejo_v,@resultado);
IF @resultado = FALSE THEN 
CALL insertar_en_adv(venta_detalle_id,col,viejo_v,nuevo_v);
END IF;

END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `viejo_nuevo_igual`(
	IN `viejo_valor` TEXT,
	IN `nuevo_valor` TEXT,
	OUT `resultado` BIT
)
BEGIN 
	IF viejo_valor = nuevo_valor THEN
		SET resultado = TRUE;
	ELSE
		SET resultado = FALSE;
	END IF;
END//
DELIMITER ;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `ventas_detalles_despues_actualizar` AFTER UPDATE ON `ventas_detalles` FOR EACH ROW BEGIN
CALL procedimiento_adv(NEW.venta_detalle_id,"venta_id",OLD.venta_id,NEW.venta_id);
CALL procedimiento_adv(NEW.venta_detalle_id,"producto_id",OLD.producto_id,NEW.producto_id);
CALL procedimiento_adv(NEW.venta_detalle_id,"divisa_id",OLD.divisa_id,NEW.divisa_id);
CALL procedimiento_adv(NEW.venta_detalle_id,"metodo_id",OLD.metodo_id,NEW.metodo_id);
CALL procedimiento_adv(NEW.venta_detalle_id,"venta_detalle_id",OLD.venta_detalle_id,NEW.venta_detalle_id);
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `ventas_detalles_despues_borrar` AFTER DELETE ON `ventas_detalles` FOR EACH ROW BEGIN
	INSERT INTO auditoria_borrar_detalles_ventas
	(bdv_fecha,venta_detalle_id,venta_id,producto_id,divisa_id,metodo_id,venta_detalle_cantidad)
	VALUES (NOW(),OLD.venta_detalle_id,OLD.venta_id,OLD.producto_id,OLD.divisa_id,OLD.metodo_id,OLD.venta_detalle_cantidad);
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
