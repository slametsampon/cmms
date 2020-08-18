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
-- Table structure for table `tg`
--

DROP TABLE IF EXISTS `tg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tg` (
  `Tagnumber` varchar(16) NOT NULL DEFAULT '',
  `PressNorm` varchar(15) DEFAULT NULL,
  `TempNorm` varchar(15) DEFAULT NULL,
  `MFG` varchar(25) DEFAULT NULL,
  `SensorModel` varchar(50) DEFAULT NULL,
  `RangeLow` varchar(10) DEFAULT NULL,
  `RangeHigh` varchar(10) DEFAULT NULL,
  `RangeUnit` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Tagnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tg`
--

LOCK TABLES `tg` WRITE;
/*!40000 ALTER TABLE `tg` DISABLE KEYS */;
INSERT INTO `tg` VALUES ('TG-0256B','-','-','-','THI 100 A+AMX','0','60','o C'),('TG-0262B','-','-','-','-','0','60','o C'),('TG-0281-1','3.5','52','NKS','TB44-309','0','100','o C'),('TG-0281-2','3','57','NKS','TB44-309','0','100','o C'),('TG-0281-3','3','57','NKS','TB44-309','0','100','o C'),('TG-0281-4','3','57','NKS','TB44-309','0','100','o C'),('TG-0281-5','3','57','NKS','TB44-309','0','100','o C'),('TG-0281-6','3.1','55','NKS','TB44-309','0','100','o C'),('TG-0281-7','2.8','52','NKS','TB44-309','0','100','o C'),('TG-0283-1','3.5','52','NKS','TB44-309','0','100','o C'),('TG-0283-2','3','57','NKS','TB44-309','0','100','o C'),('TG-0283-3','3','57','NKS','TB44-309','0','100','o C'),('TG-0283-4','3.1','55','NKS','TB44-309','0','100','o C'),('TG-0283-5','2.8','52','NKS','TB44-309','0','100','o C'),('TG-1171-1','-','-','-','-','60','90','o C'),('TG-1171-2','-','-','-','-','60','90','o C'),('TG-1571-1','3.1','55','NKS','TB44-309','0','100','o C'),('TG-1571-2','2.8','52','NKS','TB44-309','0','100','o C'),('TG-1571-3','3.5','52','NKS','TB44-309','0','100','o C'),('TG-1571-4','3','57','NKS','TB44-309','0','100','o C'),('TG-1571-5','ATM','63','NKS','TB44-309','0','100','o C'),('TG-4181-1','3.1','55','NKS','TB44-309','0','100','o C'),('TG-4181-2','2.8','52','NKS','TB44-309','0','100','o C'),('TG-8151','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-8551','2.5','80','-','TEMP. GAUGE','0','100','o C'),('TG-8552','2.4','60','-','TEMP. GAUGE','0','100','o C'),('TG-8553','3.5','32','-','TEMP. GAUGE','0','100','o C'),('TG-8554','3','40','-','TEMP. GAUGE','0','100','o C'),('TG-9113','-','-','-','-','0','120','o C'),('TG-9171A','-','-','-','-','-','-','-'),('TG-9171B','-','-','-','-','-','-','-'),('TG-9251','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-9252','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-9261A','-','-','-','-','-','-','-'),('TG-9261B','-','-','-','-','-','-','-'),('TG-9261C','-','-','-','-','-','-','-'),('TG-9261D','-','-','-','-','-','-','-'),('TG-9261F','-','-','-','-','-','-','-'),('TG-9381','-','-','-','-','-','-','-'),('TG-9451','-','-','-','-','-','-','-'),('TG-9452','-','-','-','-','-','-','-'),('TG-9454','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-9456','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-9462','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-9652A','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-9652B','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-9660','-','-','-','SUS-2','0','100','o C'),('TG-9851','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-9852','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-9853','-','-','-','THI 100 A+AMX','0','100','o C'),('TG-E719','-','-','-','A52','0','60','o C');
/*!40000 ALTER TABLE `tg` ENABLE KEYS */;
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
