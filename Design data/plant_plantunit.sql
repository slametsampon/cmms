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
-- Table structure for table `plantunit`
--

DROP TABLE IF EXISTS `plantunit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plantunit` (
  `UnitId` int(11) NOT NULL,
  `AreaName` varchar(50) DEFAULT NULL,
  `AreaId` int(11) NOT NULL,
  PRIMARY KEY (`UnitId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plantunit`
--

LOCK TABLES `plantunit` WRITE;
/*!40000 ALTER TABLE `plantunit` DISABLE KEYS */;
INSERT INTO `plantunit` VALUES (1,'Desulphurization/ Reforming',1),(2,'C02 Removal',1),(3,'Membrane Unit',1),(4,'PSA Unit',1),(5,'Guard Bed',1),(10,'Oxo Reaction Section',2),(11,'Oxo Reaction Section',2),(12,'Oxo Reaction Section',2),(13,'Oxo Reaction Section',2),(14,'Aldehyde Separation Section',2),(15,'Aldehyde Separation Section',2),(16,'Aldehyde Separation Section',2),(20,'Catalyst Recovery Section',2),(21,'Catalyst Recovery Section',2),(22,'Catalyst Recovery Section',2),(23,'Catalyst Recovery Section',2),(24,'Catalyst Recovery Section',2),(25,'Catalyst Recovery Section',2),(30,'Condensation Reaction Section',2),(31,'Condensation Reaction Section',2),(32,'Condensation Reaction Section',2),(40,'2EH Section',2),(41,'2EH Section',2),(42,'2EH Section',2),(43,'2EH Section',2),(44,'2EH Section',2),(45,'2EH Section',2),(50,'NBA Section',2),(51,'NBA Section',2),(52,'NBA Section',2),(53,'NBA Section',2),(54,'NBA Section',2),(55,'NBA Section',2),(60,'IBA Section',2),(61,'IBA Section',2),(62,'IBA Section',2),(63,'IBA Section',2),(64,'IBA Section',2),(71,'Propylene Receiving',4),(72,'Product Stroge & Shipping',4),(73,'Laboratory Facilities',11),(74,'Maintenance Facilities',13),(75,'Safety/ Fire Fighting Facilities',12),(76,'Administration Facilities',5),(77,'General',6),(80,'WWT (Activated Sludge)',3),(85,'WWT (Incinerator)',3),(91,'Power Generation & Distribution',3),(92,'Boiler',3),(93,'Water receiving, potable water & Demin Water',3),(94,'Cooling Water & Chilled Water System',3),(95,'Flare system',3),(96,'Fuel gas/ Fuel Oil System',3),(97,'WWT in Process Area',3),(98,'WWT in Process Area',3),(99,'Plant air, Instrument air, N2 distribution system',3);
/*!40000 ALTER TABLE `plantunit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-01-30 13:52:33
