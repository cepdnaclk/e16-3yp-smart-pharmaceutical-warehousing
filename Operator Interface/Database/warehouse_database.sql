-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: inventory_system
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.16.04.1

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin','admin'),(2,'Shamra','1234');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) NOT NULL,
  `stock` int(11) NOT NULL,
  `rackNo` varchar(20) NOT NULL,
  `sectionNo` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'Paracetamol',14290,'A1','1'),(2,'Glucogen',1500,'A1','1'),(3,'Acticin',1010,'A1','2'),(4,'Razadyne ER',100,'A3','1'),(5,'Gantrisin',1555,'A3','2'),(6,'Razadyne ER',160,'A2','5'),(7,'Humulin R',52,'A2','3'),(8,'Omeprezole',55,'A1','2'),(9,'Meloxicam',100,'A4','4'),(10,'Rebif',24,'A1','2'),(11,'Maxair',6666,'A4','1'),(12,'Adalat CC',666,'A4','3'),(13,'Hydralazine',12,'A3','4'),(14,'Gemfibrozil',6,'A2','2'),(15,'Glycomet',200,'A2','2'),(16,'Ecosprin',500,'A3','4'),(17,'Panadol',100,'A2','2'),(18,'New',500,'A3','3'),(19,'ndcnd',24,'4','2'),(20,'de',23,'5','1'),(21,'ff',23,'4','1'),(22,'dddddd',33,'4','1'),(23,'sc',3,'42','1'),(24,'ddijsd',34,'1','3'),(25,'dsd',10,'A4','2'),(26,'vd',5,'3','2'),(27,'sa',25,'4','3'),(28,'hbsa',500,'1','2'),(29,'df',2,'3','4'),(30,'Dibestol',500,'2','1');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `order_Id` varchar(20) NOT NULL,
  `s` varchar(45) NOT NULL,
  `client` varchar(45) NOT NULL,
  `assigned_AGV` varchar(45) NOT NULL,
  PRIMARY KEY (`order_Id`),
  KEY `fk_orders_agv_idx` (`assigned_AGV`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES ('23','Proceeding','ABC','R3,R4'),('4','Done','XYZ',''),('55','Proceeding','PQR','R2,R3'),('66','Pending','MN',''),('88','Proceeding','AZ','R5');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `robotAGV`
--

DROP TABLE IF EXISTS `robotAGV`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `robotAGV` (
  `robotId` varchar(10) NOT NULL,
  `status` varchar(45) NOT NULL,
  `battery` varchar(45) NOT NULL,
  `orderAtHand` varchar(45) NOT NULL,
  PRIMARY KEY (`robotId`),
  UNIQUE KEY `robotId_UNIQUE` (`robotId`),
  KEY `fk_robotAGV_1_idx` (`orderAtHand`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `robotAGV`
--

LOCK TABLES `robotAGV` WRITE;
/*!40000 ALTER TABLE `robotAGV` DISABLE KEYS */;
INSERT INTO `robotAGV` VALUES ('R1','Idle','98','None'),('R10','Idle','50','None'),('R11','Idle','54','None'),('R2',' Busy','55','55'),('R3',' Busy','23','23 55'),('R4',' Busy','72','23'),('R5',' Busy','40','88'),('R6','Busy','99','52'),('R7','Idle','77','None'),('R8','Idle','74','None'),('R9','Idle','75','None');
/*!40000 ALTER TABLE `robotAGV` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `robotArm`
--

DROP TABLE IF EXISTS `robotArm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `robotArm` (
  `robotID` varchar(15) NOT NULL,
  `status` varchar(45) NOT NULL,
  `orderProcessed` varchar(45) NOT NULL,
  PRIMARY KEY (`robotID`),
  KEY `fk_robotArm_1_idx` (`orderProcessed`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `robotArm`
--

LOCK TABLES `robotArm` WRITE;
/*!40000 ALTER TABLE `robotArm` DISABLE KEYS */;
INSERT INTO `robotArm` VALUES ('A1','Busy','55'),('A2','Busy','23'),('A3','Idle','None'),('A4','Busy','52'),('A5','Idle','None'),('A6','Busy','88'),('A7','Idle','None'),('A8','Busy','23'),('A9','Busy','88');
/*!40000 ALTER TABLE `robotArm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'inventory_system'
--

--
-- Dumping routines for database 'inventory_system'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-28 21:50:25
