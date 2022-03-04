-- MariaDB dump 10.19  Distrib 10.5.12-MariaDB, for Linux (x86_64)
--
-- Host: mysql.hostinger.ro    Database: u574849695_25
-- ------------------------------------------------------
-- Server version	10.5.12-MariaDB-cll-lve

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ZIP` varchar(25) NOT NULL,
  `city` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `address_unique` (`ZIP`,`city`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` VALUES (54,'02267','Lake Rosalinda'),(113,'02688-0842','Giovaniland'),(114,'02752','Jevonberg'),(58,'03115-5565','Lupefurt'),(86,'03247-3574','Theoborough'),(8,'04038','East Reanna'),(72,'04900-0197','Koeppstad'),(74,'05701','Schimmelville'),(7,'08496','Starkmouth'),(41,'09666','Hayeston'),(12,'10976','New Maryam'),(9,'11317-8531','Jordiborough'),(111,'12654','Annetteland'),(119,'13300-1960','Port Bettyefurt'),(57,'15264-0063','Mathewstad'),(70,'15300','Lake Eulaliaton'),(10,'15484-9782','Lake Dorothea'),(46,'15834-8927','North Arnoldo'),(109,'19206','West Montebury'),(19,'19437','Maxieburgh'),(73,'19970','New Coleman'),(115,'21386-7942','Wavahaven'),(97,'23646-1772','South Eldora'),(98,'24415-8951','East Germanton'),(48,'25137-0640','Manuelview'),(107,'25144','New Jamarcusborough'),(27,'27858-0168','South Zolaview'),(25,'28100-6077','New Deondre'),(59,'29980-3651','Port Marleefurt'),(4,'30020-1331','Cathrineberg'),(26,'31285-9962','East Ambrose'),(90,'31938','South Mollie'),(69,'36062','Stephaniemouth'),(79,'38391','New Pascaleshire'),(105,'39937-6169','East Gladyceton'),(31,'40704','Port Hazelbury'),(116,'45012-9187','West Jerroldshire'),(23,'46325-5407','Chelseymouth'),(21,'46715-8674','North Yvonnestad'),(84,'46727-8375','Raoulfurt'),(101,'46954-8075','Odessaport'),(89,'48298','Wilmaburgh'),(56,'48739','Port Aliashire'),(63,'49496','Lake Corneliusberg'),(92,'49903','Lake Stephaniefort'),(30,'50193-0746','Port Jess'),(83,'51642-9752','Bayerhaven'),(65,'51699-7716','Ziemannview'),(94,'52007','D\'angelomouth'),(76,'52517','Kearaland'),(87,'52757','East Agustina'),(5,'53757-9612','East Javon'),(29,'54666-8200','Willmsport'),(71,'55596','North Kennethmouth'),(81,'55906-6815','East Aldaburgh'),(40,'56075','Kshlerinmouth'),(124,'56699','Port Rorychester'),(64,'57463-6855','Stromanhaven'),(88,'57558','Runteton'),(34,'57565','Normahaven'),(60,'58143','New Johann'),(52,'58297-7641','Bernierbury'),(106,'58366','West Ashley'),(91,'58707-1858','Port Flavio'),(18,'58708-1661','Chynafort'),(122,'58883-3652','West Keon'),(38,'60581-8929','New Bartholome'),(13,'61058','Kiehnstad'),(118,'61333-6590','Helenastad'),(20,'61597-5777','Lake Gregoryhaven'),(102,'62470-5320','Fionastad'),(47,'63283-2148','West Fanny'),(99,'63602-1078','North Valentine'),(50,'64128','Bernhardberg'),(22,'64703','Port Samanthachester'),(32,'65409','Creminbury'),(6,'66020-6585','Beahanhaven'),(62,'66645-0873','Harveyview'),(33,'67255-3532','Quitzonshire'),(85,'67438','North Clemmie'),(121,'67675','Zulaufshire'),(95,'70003-3080','Norvalchester'),(77,'70863-3940','Westonfurt'),(108,'71397-5281','Jabarimouth'),(103,'71519','North Xzavierburgh'),(55,'72185-7718','East Dominic'),(75,'72830','Israelfort'),(78,'72938-4673','South Alanside'),(53,'73109','East Cleora'),(44,'73562-1894','Kelliland'),(123,'74340-0369','Kristown'),(42,'74778-2029','New Giles'),(117,'75064','Jacobiton'),(24,'76094','South Mohamed'),(100,'76893-2051','Angelinemouth'),(39,'77263','South Vergiehaven'),(68,'79678','East Danny'),(80,'79769','Port Lonzo'),(1,'80451','West Lois'),(67,'80823-1001','Amyton'),(49,'80901','South Irwinland'),(45,'81756','North Syble'),(66,'82344-1364','Nikolausberg'),(15,'83016','New Dennis'),(17,'83535-2682','North Pietromouth'),(16,'84136','Raynorstad'),(2,'84614-8206','Lake Deventown'),(82,'85099','East Matteo'),(37,'85951-3169','Jennyferbury'),(120,'86918','East Ivahville'),(28,'88018-9222','Bradtkestad'),(112,'89252-4106','South Tommiehaven'),(125,'89409-0358','Gutkowskistad'),(110,'89512','Lake Elizabeth'),(3,'90183-3220','East Maxieview'),(104,'90916-0083','Martinebury'),(93,'91212','Linaview'),(51,'93185','Maggiofort'),(14,'93616','Aureliaburgh'),(43,'94852-4391','East Odaton'),(36,'95167-5928','Lemkeborough'),(11,'95562-4328','Lake Lee'),(61,'95608-8759','North Keegan'),(96,'97026','Lake Bridgetteville'),(35,'98930-7927','South Fiona');
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-04 13:28:49
