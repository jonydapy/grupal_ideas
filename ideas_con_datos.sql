-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: ideas
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `campaigns`
--

DROP TABLE IF EXISTS `campaigns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campaigns` (
  `idcampaign` int NOT NULL AUTO_INCREMENT,
  `name_campaing` varchar(150) DEFAULT NULL,
  `description` text,
  `id_strategy` int NOT NULL,
  PRIMARY KEY (`idcampaign`),
  KEY `fk_campaigns_strategies1_idx` (`id_strategy`),
  CONSTRAINT `fk_campaigns_strategies1` FOREIGN KEY (`id_strategy`) REFERENCES `strategies` (`idstrategy`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaigns`
--

LOCK TABLES `campaigns` WRITE;
/*!40000 ALTER TABLE `campaigns` DISABLE KEYS */;
INSERT INTO `campaigns` VALUES (1,'Como reducir costos de ventas','cuentanos tus ideas',1);
/*!40000 ALTER TABLE `campaigns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cluster`
--

DROP TABLE IF EXISTS `cluster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cluster` (
  `idcluster` int NOT NULL AUTO_INCREMENT,
  `name_cluster` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`idcluster`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cluster`
--

LOCK TABLES `cluster` WRITE;
/*!40000 ALTER TABLE `cluster` DISABLE KEYS */;
INSERT INTO `cluster` VALUES (1,'Sin Asignar');
/*!40000 ALTER TABLE `cluster` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `idcomment` int NOT NULL AUTO_INCREMENT,
  `comment` text,
  `user_id` int NOT NULL,
  `idea_id` int NOT NULL,
  PRIMARY KEY (`idcomment`),
  KEY `fk_comments_users1_idx` (`user_id`),
  KEY `fk_comments_ideas1_idx` (`idea_id`),
  CONSTRAINT `fk_comments_ideas1` FOREIGN KEY (`idea_id`) REFERENCES `ideas` (`ididea`),
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,'Esto es muy interesante jejeje',9,1),(2,'No le veo futuro',8,1);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hypothesis`
--

DROP TABLE IF EXISTS `hypothesis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hypothesis` (
  `idhypothesis` int NOT NULL AUTO_INCREMENT,
  `hypothesis` varchar(255) DEFAULT NULL,
  `experiment` varchar(255) DEFAULT NULL,
  `learning` varchar(255) DEFAULT NULL,
  `id_initiative` int NOT NULL,
  PRIMARY KEY (`idhypothesis`),
  KEY `fk_hypothesis_initiative1_idx` (`id_initiative`),
  CONSTRAINT `fk_hypothesis_initiative1` FOREIGN KEY (`id_initiative`) REFERENCES `initiative` (`idinitiative`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hypothesis`
--

LOCK TABLES `hypothesis` WRITE;
/*!40000 ALTER TABLE `hypothesis` DISABLE KEYS */;
INSERT INTO `hypothesis` VALUES (2,'La AI aumentará 10% la experiencia positiva del cliente','encuesta a cliente','Hip rechazada porque los clientes paraguayos tienen miedo',1);
/*!40000 ALTER TABLE `hypothesis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ideas`
--

DROP TABLE IF EXISTS `ideas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ideas` (
  `ididea` int NOT NULL AUTO_INCREMENT,
  `content` text,
  `user_id` int NOT NULL,
  `id_campaign` int NOT NULL,
  `id_cluster` int NOT NULL,
  PRIMARY KEY (`ididea`),
  KEY `fk_ideas_users1_idx` (`user_id`),
  KEY `fk_ideas_campaigns1_idx` (`id_campaign`),
  KEY `fk_ideas_cluster1_idx` (`id_cluster`),
  CONSTRAINT `fk_ideas_campaigns1` FOREIGN KEY (`id_campaign`) REFERENCES `campaigns` (`idcampaign`),
  CONSTRAINT `fk_ideas_cluster1` FOREIGN KEY (`id_cluster`) REFERENCES `cluster` (`idcluster`),
  CONSTRAINT `fk_ideas_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ideas`
--

LOCK TABLES `ideas` WRITE;
/*!40000 ALTER TABLE `ideas` DISABLE KEYS */;
INSERT INTO `ideas` VALUES (1,'Implemen tar AI',9,1,1);
/*!40000 ALTER TABLE `ideas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `initiative`
--

DROP TABLE IF EXISTS `initiative`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `initiative` (
  `idinitiative` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) DEFAULT NULL,
  `id_cluster` int NOT NULL,
  `id_rating` int NOT NULL,
  PRIMARY KEY (`idinitiative`),
  KEY `fk_initiative_cluster1_idx` (`id_cluster`),
  KEY `fk_initiative_ratings1_idx` (`id_rating`),
  CONSTRAINT `fk_initiative_cluster1` FOREIGN KEY (`id_cluster`) REFERENCES `cluster` (`idcluster`),
  CONSTRAINT `fk_initiative_ratings1` FOREIGN KEY (`id_rating`) REFERENCES `ratings` (`idrating`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `initiative`
--

LOCK TABLES `initiative` WRITE;
/*!40000 ALTER TABLE `initiative` DISABLE KEYS */;
INSERT INTO `initiative` VALUES (1,'Implementacion de AI para ventas',1,1);
/*!40000 ALTER TABLE `initiative` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ratings`
--

DROP TABLE IF EXISTS `ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ratings` (
  `idrating` int NOT NULL AUTO_INCREMENT,
  `score` varchar(150) DEFAULT NULL,
  `id_user` int NOT NULL,
  PRIMARY KEY (`idrating`),
  KEY `fk_ratings_users1_idx` (`id_user`),
  CONSTRAINT `fk_ratings_users1` FOREIGN KEY (`id_user`) REFERENCES `users` (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ratings`
--

LOCK TABLES `ratings` WRITE;
/*!40000 ALTER TABLE `ratings` DISABLE KEYS */;
INSERT INTO `ratings` VALUES (1,'Sin Calificar',8);
/*!40000 ALTER TABLE `ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `strategies`
--

DROP TABLE IF EXISTS `strategies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `strategies` (
  `idstrategy` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) DEFAULT NULL,
  `description` text,
  `id_user` int NOT NULL,
  PRIMARY KEY (`idstrategy`),
  KEY `fk_strategies_users1_idx` (`id_user`),
  CONSTRAINT `fk_strategies_users1` FOREIGN KEY (`id_user`) REFERENCES `users` (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `strategies`
--

LOCK TABLES `strategies` WRITE;
/*!40000 ALTER TABLE `strategies` DISABLE KEYS */;
INSERT INTO `strategies` VALUES (1,'Aumentar Ventas','Aumentar ventas sin aumentar costos',8);
/*!40000 ALTER TABLE `strategies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_user`
--

DROP TABLE IF EXISTS `type_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_user` (
  `idtipo` int NOT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idtipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_user`
--

LOCK TABLES `type_user` WRITE;
/*!40000 ALTER TABLE `type_user` DISABLE KEYS */;
INSERT INTO `type_user` VALUES (1,'Admin'),(2,'Director'),(3,'Consejero'),(4,'Lider'),(5,'Normal');
/*!40000 ALTER TABLE `type_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `iduser` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `type_user` int NOT NULL,
  PRIMARY KEY (`iduser`),
  KEY `fk_users_type_user_idx` (`type_user`),
  CONSTRAINT `fk_users_type_user` FOREIGN KEY (`type_user`) REFERENCES `type_user` (`idtipo`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (8,'Poderoso','Admin','admin@admin.com','12345678','2023-03-14 10:56:06','2023-03-14 10:56:06',1),(9,'Usuario','SinPoder','user@user.com','12345678','2023-03-14 10:56:44','2023-03-14 10:56:44',5),(10,'Javier','Irun','javier@gmail.com','$2b$12$kbKFSczNvg9Oxxcb2WdgluX1oUfTOsa3KQA.pxYUhTQKxwHL0GyG2','2023-03-14 11:50:18','2023-03-14 11:50:18',5),(11,'mario','delgado','mario@gmail.com','$2b$12$6E2SbW59Q2ler/2C8Tegxu.gHZyCUjXS8WZcfUEDjP0PRaRJxVTR2','2023-03-14 12:04:58','2023-03-14 12:04:58',5),(12,'juca','asdf','j@dd.com','$2b$12$kVZvsNxv8nXOW8WSOOIAGOW4YqBUrVhIuwK.mEA21r5eZGDB6bhFG','2023-03-14 12:12:38','2023-03-14 12:12:38',5),(13,'ddd','aaaa','k@gmail.com','$2b$12$lxMQvGuVULeDuAoQNq8RNenfQD/NBQcc9TVSwTFxzaAcnOwkZSjn2','2023-03-14 12:13:19','2023-03-14 12:13:19',5);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-14 14:44:09
