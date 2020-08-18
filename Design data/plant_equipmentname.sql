CREATE DATABASE  IF NOT EXISTS `plant` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `plant`;
-- MySQL dump 10.13  Distrib 5.5.16, for Win32 (x86)
--
-- Host: localhost    Database: plant
-- ------------------------------------------------------
-- Server version	5.5.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `equipmentname`
--

DROP TABLE IF EXISTS `equipmentname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipmentname` (
  `EqpId` int(11) NOT NULL,
  `EqpName` varchar(50) DEFAULT NULL,
  `Initial` varchar(5) DEFAULT NULL,
  `EqpCatId` int(11) NOT NULL,
  PRIMARY KEY (`EqpId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipmentname`
--

LOCK TABLES `equipmentname` WRITE;
/*!40000 ALTER TABLE `equipmentname` DISABLE KEYS */;
INSERT INTO `equipmentname` VALUES (1,'Battery Charger','BCH',1),(2,'Capacitor Bank','CBK',1),(3,'Cathodic Protection','CPN',1),(4,'Centrifugal Compressor','CPR',1),(5,'Emergency Diesel Generator','EDG',1),(6,'Lighting','LTH',1),(7,'MCC','MCC',1),(8,'Motor - DC','MDC',1),(9,'Motor - AC','MAC',1),(10,'Motor - Stepper','MST',1),(11,'Neutral Grounding System','GRD',1),(12,'Switchgear','SCG',1),(13,'Transformer','TRF',1),(14,'UPS','UPS',1),(15,'Computer','COM',3),(16,'DCS','DCS',3),(17,'HMI','HMI',3),(18,'PHD','PHD',3),(19,'PLC','PLC',3),(20,'Air Damper','ADP',2),(21,'Analyzer','ALY',2),(22,'Control Valve','CV',2),(23,'Flow Transmitter','FT',2),(24,'Gas Detector','GD',2),(25,'Impact Transmitter','IT',2),(26,'Level Gauge','LG',2),(27,'Level Switch','LS',2),(28,'Level Transmitter','LT',2),(29,'On Off Valve','OOV',2),(30,'Pitch Control','PTC',2),(31,'Positioner','PSR',2),(32,'Press. Transmitter','PT ',2),(33,'Pressure Gauge','PG',2),(34,'Pressure Switch','PSR',2),(35,'Rod Drop','RD',2),(36,'Solenoid Valve','SV',2),(37,'Temperature Gauge','TG',2),(38,'Temperature instrument','TI',2),(39,'Temperature Switch','TS',2),(40,'Vibration Switch','VS',2),(41,'Air Cooled Heat Exchanger','ACH',5),(42,'Blower','BLW',5),(43,'Canned Pump','CP',5),(44,'Centrifugal Compressor','CC',5),(45,'Centrifugal Pump','CFP',5),(46,'Convection Coil Heater','CCH',5),(47,'Drum','DRM',5),(48,'Ejector','EJR',5),(49,'Filter','FLT',5),(50,'Metering Pump','MP',5),(51,'Plate Heat Exchanger','PHE',5),(52,'Reactor','RCR',5),(53,'Reciprocating Compressor','RPC',5),(54,'Screw Compressor','SCP',5),(55,'Separator','SPR',5),(56,'Shell & Tube Heat Exchanger','STHE',5),(57,'Tank','TANK',5),(58,'Tower','TOWER',5),(59,'Air Conditioner','AC ',4),(60,'Fire Alarm','FA',4),(61,'HT','HT',4),(62,'PABX','PABX',4),(63,'Paging System','PGS',4),(64,'Tool','TOOL',4),(65,'Building','BLD',6),(66,'Road','ROAD',6),(67,'Foundation','FDN',6),(68,'General','GEN',9);
/*!40000 ALTER TABLE `equipmentname` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-01-30 13:52:34
