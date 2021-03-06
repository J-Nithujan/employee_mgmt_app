-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.27 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Listage de la structure de la table db_employees. addresses
DROP TABLE IF EXISTS `addresses`;
CREATE TABLE IF NOT EXISTS `addresses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ZIP` varchar(25) NOT NULL,
  `city` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `address_unique` (`ZIP`,`city`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table db_employees.addresses : ~50 rows (environ)
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` (`id`, `ZIP`, `city`) VALUES
	(4, '01276', 'Lietzow'),
	(22, '03892', 'Horben'),
	(34, '05167', 'Büren'),
	(17, '05398', 'Bunsoh'),
	(16, '07368', 'Schefflenz'),
	(10, '07414', 'Burbach'),
	(2, '12878', 'Teningen'),
	(13, '14692', 'Argenschwang'),
	(30, '16874', 'Tensbüttel-Röst'),
	(48, '19222', 'Hopsten'),
	(31, '21225', 'Scheeßel'),
	(25, '22003', 'Zwota'),
	(28, '28936', 'Arft'),
	(15, '32014', 'Kablow Ziegelei'),
	(35, '32423', 'Horbach'),
	(38, '33115', 'Winkelbach'),
	(12, '34589', 'Lilienthal'),
	(14, '38957', 'Tennenbronn'),
	(1, '41043', 'Passow'),
	(36, '41781', 'Argenbühl'),
	(23, '45093', 'Greese'),
	(44, '47864', 'Kablow'),
	(46, '48815', 'Käbschütztal'),
	(49, '48963', 'Horath'),
	(47, '49426', 'Passee'),
	(42, '52629', 'Bürchau'),
	(27, '53627', 'Aresing'),
	(9, '61888', 'Winklarn'),
	(40, '62008', 'Scheer'),
	(32, '62767', 'Winkel'),
	(24, '64532', 'Winkelhaid'),
	(18, '69555', 'Greifenberg'),
	(19, '74076', 'Burg'),
	(26, '74351', 'Passade'),
	(3, '75457', 'Scheden'),
	(5, '76086', 'Tensfeld'),
	(8, '78580', 'Limbach-Oberfrohna'),
	(29, '81218', 'Winkelsett'),
	(11, '82169', 'Horb'),
	(43, '82404', 'Passau'),
	(39, '82460', 'Arensnest'),
	(20, '85231', 'Grefrath'),
	(50, '85849', 'Greding'),
	(33, '86820', 'Bürdenbach'),
	(6, '87763', 'Greifenhagen'),
	(41, '91063', 'Teplitz'),
	(45, '92299', 'Winkelstedt'),
	(7, '93070', 'Argenthal'),
	(37, '95261', 'Arenzhain'),
	(21, '97465', 'Limbach');
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;

-- Listage de la structure de la table db_employees. departments
DROP TABLE IF EXISTS `departments`;
CREATE TABLE IF NOT EXISTS `departments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table db_employees.departments : ~12 rows (environ)
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` (`id`, `name`) VALUES
	(10, 'Consulting'),
	(5, 'Customer Support'),
	(1, 'Executive'),
	(3, 'Facilities'),
	(11, 'Finance'),
	(12, 'Human Resources'),
	(6, 'Information Technology'),
	(4, 'Manufacturing'),
	(7, 'Marketing'),
	(9, 'Operations'),
	(2, 'Research and Development'),
	(8, 'Sales');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;

-- Listage de la structure de la table db_employees. employees
DROP TABLE IF EXISTS `employees`;
CREATE TABLE IF NOT EXISTS `employees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `birthdate` date NOT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `road` varchar(75) NOT NULL,
  `hiring_date` date NOT NULL,
  `percentage` decimal(5,2) NOT NULL,
  `salary` decimal(7,2) NOT NULL,
  `holiday_balance` decimal(4,2) DEFAULT '0.00',
  `under_contract` tinyint DEFAULT '1',
  `work_time` decimal(10,0) DEFAULT '0',
  `password` varchar(64) NOT NULL,
  `employee_id` int DEFAULT NULL,
  `address_id` int NOT NULL,
  `job_id` int NOT NULL,
  `department_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `fk_employees_employees_idx` (`employee_id`),
  KEY `fk_employees_addresses1_idx` (`address_id`),
  KEY `fk_employees_job1_idx` (`job_id`),
  KEY `fk_employees_departments1_idx` (`department_id`),
  CONSTRAINT `fk_employees_addresses1` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`),
  CONSTRAINT `fk_employees_departments1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`),
  CONSTRAINT `fk_employees_employees` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `fk_employees_job1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table db_employees.employees : ~53 rows (environ)
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` (`id`, `email`, `firstname`, `lastname`, `birthdate`, `phone_number`, `road`, `hiring_date`, `percentage`, `salary`, `holiday_balance`, `under_contract`, `work_time`, `password`, `employee_id`, `address_id`, `job_id`, `department_id`) VALUES
	(1, 'Conrad_Frizzell61@example.com', 'Paschalis', 'Kleiner', '1980-01-16', '0722457009', '24-36 Wandsworth Bridge Road', '2015-02-14', 15.50, 6871.96, 5.00, 1, 73, '9ff5654065f786b252c6733a6651d87848e6f45603b30cdaec3a42eb47d2de90', NULL, 13, 3, 2),
	(2, 'Schuler@example.com', 'Joerge', 'Zurbriggen', '1986-08-14', '0732447390', '3 Eversholt Street', '2014-12-22', 80.50, 9111.41, 2.00, 1, 6, 'b56ec8f2611887143057b14d11a73910108506c5d8f4d4f4a163b41e3a839cfc', NULL, 29, 7, 10),
	(3, 'ZapataF@example.com', 'Felin', 'Albrecht', '1965-01-14', '0732412758', '5-9 Bishops Square', '2015-04-02', 10.50, 8316.53, 8.00, 1, 8, '49d2262ea6ee5d742e7abdf5116300ebe488ce975af47c64e2af01987ca4316d', NULL, 32, 1, 7),
	(4, 'Sanford549@nowhere.com', 'Balintt ', 'Büchner', '1992-04-27', '0753827508', '2-7 Pretoria Avenue', '2021-06-26', 75.00, 8973.45, 9.50, 1, 39, '45ba5d5e6701537c1121c599ecdcb0023418f47af5ad93d8f993c0eca6e50622', NULL, 48, 9, 8),
	(5, 'Barr@nowhere.com', 'Filiberta', 'Altmann', '1994-02-05', '0742449929', '4 Allsopp Place', '2015-09-11', 50.00, 6338.52, 6.00, 1, 11, '1127319de447cc56fd27680051657a7bb1fbbae8d92165b4f60723867ec71e5b', NULL, 12, 8, 7),
	(6, 'Almanza@example.com', 'Filina', 'Treviranus', '1998-02-27', '0784257658', '3-6 Abyssinia Close', '2016-04-15', 95.50, 9328.78, 6.00, 1, 7, 'd64e9af0a2ecc1590bbe8e50ae76d19b5122ad46c1f9a95f74e188e9ba516ceb', NULL, 33, 13, 7),
	(7, 'Ron.Irish@example.com', 'Gotfrit', 'osenmüller', '1962-03-06', '0758612774', '1 Churchill Place', '2019-09-30', 25.00, 6316.04, 16.00, 0, 12, '89d901648314bc4b42f5752bdb8a7e393c3e7563a48d2986528060a232215e0b', NULL, 4, 14, 1),
	(8, 'ktercnnp_okcisx@example.com', 'Adelisa ', 'Buhmann', '1956-04-10', '0742800522', '1-8 Buckingham Gate', '2014-07-31', 55.50, 9771.07, 18.50, 1, 57, 'c729f8d0dd8d62bb8abf3bfe760ed3e817d1f13927ce9404d104b33507324a02', 1, 4, 15, 11),
	(9, 'mnksgeiq8021@example.com', 'Cathrine', 'choll', '1967-11-30', '0799211908', '32-59 Abbey Lane', '2019-11-24', 40.50, 6134.95, 9.50, 0, 42, '862a285723ca6322c5fab84d62f27bace7ef1bfc7cf52ae7fbbe4b5b95c7b434', 2, 19, 2, 11),
	(10, 'Atwood@nowhere.com', 'Basileo ', 'Leist', '1972-09-28', '0712406901', '5C Clissold Crescent', '2021-02-16', 80.50, 7248.95, 15.00, 0, 12, 'f98002a4bc241df1571efa376aaf456a833a90ad000da9c6a5a8c5c177d1dc93', 3, 1, 11, 2),
	(11, 'Sima_Call6@example.com', 'Elika', 'elke', '1952-01-07', '0757124126', '1 Grasvenor Avenue', '2018-03-31', 25.50, 7015.12, 3.50, 1, 90, 'e9525d1e7db8f5f16498a11b06018d0acb5cc176e87b2f52474cfb1d59413edc', 4, 48, 11, 9),
	(12, 'Kirk.HKoehler@nowhere.com', 'Volkbert', 'Freund', '1982-02-22', '0778544946', '1 A-C Paget Street', '2016-11-05', 60.00, 6532.62, 18.00, 0, 42, 'ae5164f18b01addcb76e8195afb47c43ce6cb7b718497510bec45a366ed3a3b4', 5, 46, 13, 8),
	(13, 'EdmundBenitez631@example.com', 'Waldomir', 'Kleinermann', '1967-09-12', '0722402660', '1 A-D Johnston Road', '2016-03-11', 65.00, 9624.08, 3.50, 0, 94, '2f85ef49537730235d195e929d87b34bc63c5e42f7dbbc169fd933e9b8cfe36f', 6, 47, 16, 5),
	(14, 'Salley69@nowhere.com', 'Burkhard', 'Herzog', '1958-09-07', '0786249631', '700 Albert Basin Way', '2015-03-07', 65.50, 6863.54, 13.50, 1, 158, '0fec9b1807a0026a599bd824b53af8aff8fe4d88c1fbfcd1212099ef5cb899e3', 7, 26, 19, 3),
	(15, 'Kiefer@nowhere.com', 'Jule', 'Leitner', '1967-11-16', '0702466276', '1-8 Christopher Street', '2015-08-13', 40.50, 9102.30, 2.50, 0, 121, '85e28a4d8d14ed39178b292f15f7badb27514f29f564a6bd37cfe5b2090942ab', 1, 10, 12, 5),
	(16, 'ElmerFoley@example.com', 'Santian', 'Anger', '1990-07-07', '0754078495', '1-7 Glen Road', '2021-08-12', 40.50, 6643.83, 13.00, 1, 40, 'c567fdbcc326a2adbb9448fd3c52d327c83491b669a85459892d6d89cba8f0d1', 2, 39, 17, 9),
	(17, 'Brinkman28@example.com', 'Aloysia', 'Kleinmann', '2001-09-19', '0776661092', '14-28 Blenheim Park Road', '2014-05-04', 20.50, 6387.61, 7.00, 1, 2, '05eeb01c5385b2f82e5f09e9858498c0046e4fb9600f8bf1d47adb755785ccd2', 3, 19, 9, 1),
	(18, 'Almeida24@example.com', 'Detmar', 'Bülow', '1961-12-10', '0750812421', '54-58 Aberconway Road', '2019-05-26', 50.50, 9638.56, 5.50, 0, 68, 'e7ab65a659ab8c6f042f3ee81140c77c2f58b8a5237890fc63c1cc0acb7a753c', 4, 24, 16, 2),
	(19, 'LambF@nowhere.com', 'Lowis', 'Lemm', '1970-10-03', '0775399136', '23-28 Creighton Road', '2017-01-07', 90.50, 9187.52, 15.00, 1, 82, '5f0156495ef9bd45e20e15793d04cacb68c24685239c45ac54be3d6b934ad8bc', 5, 11, 5, 2),
	(20, 'ShandraCarranza@nowhere.com', 'Tius', 'össler', '1991-10-04', '0740224365', '1-9 Bishops Way', '2015-11-09', 75.00, 8089.29, 4.50, 1, 131, 'd6b38421528078286304dc3f714b7f280a6dc9f2bb6c715becaf4a0c73b0a5a7', 6, 42, 17, 12),
	(21, 'JeraldAbraham529@example.com', 'Jürg', 'Trübner', '1984-06-13', '0742307122', '3-7 Carisbrooke Road', '2016-07-31', 30.00, 6588.14, 11.50, 0, 4, 'd363aba5208d3e082f04898af31ad16d07886d00ea5d6b52cf9df03e90a7028d', 7, 1, 1, 12),
	(22, 'Abel5@example.com', 'Danja', 'Kleist', '1958-01-06', '0732444816', '1E Hanworth Road', '2015-09-22', 65.00, 6537.42, 7.00, 1, 1, '00ee82054536753e332b5549c00892b99bccc773e73969bf6e49fbe05684ab66', 1, 23, 7, 3),
	(23, 'Bachman@example.com', 'Eckhart', 'chön', '1965-11-20', '0722418815', '1-7 Cowper Road', '2014-08-20', 65.50, 7962.97, 5.00, 0, 86, '4c181a8dfef35b6f1f520c95366efdeec4fb6e4417dd07a1539c1e936d34891d', 2, 25, 12, 2),
	(24, 'FriedaAbreu99@example.com', 'Deborian', 'Angst', '1954-05-17', '0780068061', '35-26 Grays Farm Road', '2020-01-17', 70.50, 6986.71, 5.50, 0, 112, '3eb54f7e95f262c868efc54d100168cf07937e84889c650c52e14acaf93b7ec9', 3, 24, 11, 6),
	(25, 'Barrett_Mcgowan@example.com', 'Dörtlis', 'Burgdorf', '1952-01-07', '0782415538', '3 Buxton Road', '2016-06-20', 10.50, 8617.72, 4.50, 1, 121, 'dd95b8e02334bf13e5036efebe7a5ac2c2960970da6a48cfeb331d0f38ff16d2', 4, 32, 15, 1),
	(26, 'rvxkhcgk5666@example.com', 'Eligius', 'Appel', '2001-10-10', '0797176572', '66 Great Chapel Street', '2020-02-21', 55.50, 6702.92, 2.50, 0, 80, 'a9db687c1bd18c407822470de0892b5a834209744d65a0e32c8be098db37275e', 5, 7, 10, 8),
	(27, 'Dodge@example.com', 'Fritz', 'euenburg', '2001-05-18', '0712461720', '44-48 Curzon Square', '2016-08-04', 90.50, 7964.21, 14.00, 0, 101, '5d43da01f2ec7a2f606eb2a0da241409b8df386f27eed9d38d43dfda48f8c293', 6, 34, 9, 6),
	(28, 'Perkins@example.com', 'Konradin', 'Bürger', '1979-11-02', '0732497232', '35-19 Abbey Lane', '2021-04-18', 30.50, 8462.24, 6.00, 0, 58, '5348ff5842cfb60e9d98d3271ce7b2275da2bb349a46470f88207ebf8be6d890', 7, 24, 11, 4),
	(29, 'NorrisBolt@example.com', 'Caruso', 'otmann', '1957-01-12', '0773125752', '91 Alwyne Road', '2014-03-12', 85.50, 9162.12, 8.50, 0, 3, '01b05435eb831b3103fb7dcd688edf4b81165c413839d4e194e54139c2dd8075', 1, 25, 12, 11),
	(30, 'Barron@nowhere.com', 'Selinda', 'Ude', '1952-01-12', '0752873476', '55-19 Crowndale Road', '2016-03-05', 30.00, 7444.01, 11.00, 0, 130, '3f7c7a77345b3fff16532cf58aafa056d9a675da6751b4062790209cc0ff987d', 2, 2, 17, 9),
	(31, 'Duval@example.com', 'Teoresa', 'chönberg', '1975-07-10', '0776484713', '29 Hughes Walk', '2014-07-12', 5.50, 9608.60, 9.00, 0, 9, 'fda21f95c20bdaa9d41acf61bada847eb5a97d85451e9170630aa5407178ab78', 3, 16, 12, 2),
	(32, 'Zenobia.Brunson@example.com', 'Cornell', 'Lengefeld', '1981-08-21', '0772488652', '2 Gray\'s Inn Road', '2015-12-19', 30.50, 9542.24, 17.50, 0, 159, 'ad77d4e3d5f3b7792316a4de5c0019e8672fd501acc40e3cbaa13d020360b82e', 4, 25, 19, 3),
	(33, 'Adela_Alley61@example.com', 'Miria', 'eumann', '1964-02-27', '0780789140', '53-57 Bray Court', '2014-09-30', 20.50, 6570.35, 13.50, 1, 13, 'c05b0bd81297cd8ee446d857afb32b83f5b78a87d3983d6728afd6b6d27d7b55', 5, 25, 18, 11),
	(34, 'Abel313@example.com', 'Skyla', 'Arnold', '1973-03-07', '0780116765', '21-17 Abbey Street', '2020-05-03', 65.50, 8998.68, 8.00, 1, 134, '92995af8011d71641d03bf47f2c5a17b6a1b0e3216d16532c0de2b4530310e2c', 6, 24, 1, 2),
	(35, 'Suggs@example.com', 'Bärbel', 'otschield', '1999-06-15', '0742453773', '24-16 Magdalen Road', '2016-06-15', 75.00, 6990.01, 1.00, 0, 41, 'd837cea9abda945d242f634b9d98d2ef363acb8fdf2dfe1b8f4e5bfb46091870', 7, 28, 15, 5),
	(36, 'Acker@example.com', 'Helmute', 'Fries', '1954-06-15', '0722475877', '34-39 Portal Way', '2018-06-12', 35.50, 8154.84, 0.00, 1, 6, 'a325b6ddaf297487981b561abd9b44f52c2147736111f8235e99f44013be3d4d', 1, 24, 12, 9),
	(37, 'aweyzjpd3111@example.com', 'Eustachius', 'Burkhard', '2000-10-14', '0786202596', '9 A-C Adelaide Street', '2017-01-07', 30.00, 9504.35, 17.00, 1, 25, '088ba412278fad69e9970a3b873282fba3e96a8247418887edbc6e4677d4b359', 2, 11, 14, 2),
	(38, 'Arthur@example.com', 'Thees', 'Klemperer', '1978-02-23', '0746844643', '1 Adelaide Grove', '2017-02-10', 65.00, 7594.15, 11.00, 0, 97, 'fb58b8f7046043b5262774ba49d6b8800f6ad3bff02b82268d5a3bea4104be3c', 3, 23, 17, 10),
	(39, 'Ruffin@nowhere.com', 'Edelgard', 'euner', '1979-10-30', '0732490621', '12-37 Churchill Place', '2016-12-28', 40.50, 8277.98, 13.00, 0, 149, '655ac869b8fe16713cfd93fcd69f60b486503d70537251b74e933ae2ad7e6c3c', 4, 39, 4, 7),
	(40, 'EleanoreYEscamilla158@example.com', 'Role', 'Assmann', '1960-08-16', '0745200859', '5B Normanton Road', '2015-07-31', 40.50, 8539.33, 16.00, 1, 30, '02749db744317f2b42245e8dddf9c5eb0efda86ab3164a8e433370bfdd4071f7', 5, 27, 3, 3),
	(41, 'JerroldSAkins@example.com', 'Lusia', 'Uhlig', '1960-11-27', '0732433446', '24-29 St Ann\'s Road', '2014-03-03', 30.00, 6447.13, 5.50, 1, 19, 'bb2294064ee66a24171c66d8967a097a1cb91c748a94af370c6bb9af5f2cdb16', 6, 43, 4, 9),
	(42, 'Tackett@example.com', 'Annafee', 'Hess', '1952-03-02', '0742982816', '42-28 Abbeville Road', '2019-04-15', 25.50, 7425.90, 2.50, 1, 107, '67575251f71eae3a795ce1468129cbc576413c53823ce3e07ffe65dea55fac27', 7, 49, 4, 11),
	(43, 'Chasidy.Nye82@example.com', 'Jolena', 'Lenz', '1989-11-18', '0779549452', '2 A-C Stoke Newington Road', '2018-02-03', 20.50, 9475.07, 18.50, 1, 152, 'd24250ce89d80224a9d00a6176f68110f4ed79d541454db3ee16f4607e1505e8', 1, 14, 5, 3),
	(44, 'wawwcqng.wmbvidy@example.com', 'Sonja', 'Frisch', '1967-11-20', '0750526737', '1-7 St. John\'s Court', '2016-05-03', 25.00, 9883.08, 8.00, 0, 92, '7632f0c684f6e2d275937e5f410bb9a9986c495d4157a18da28a2a722c38859d', 2, 7, 10, 6),
	(45, 'Abney@example.com', 'Suso', 'Hesse', '1991-03-18', '0792486004', '7 Clara Place', '2016-04-28', 25.50, 8462.63, 2.00, 1, 73, '5e87be131b8189e1d344b9a2711a45de15d3bc69c92bfc48d084c6c6d7bec919', 3, 10, 20, 5),
	(46, 'Joseph.Trapp@example.com', 'Dorit', 'Dahrendorf', '1968-04-15', '0786252747', '9 Singleton Close', '2016-11-05', 5.50, 6069.42, 9.00, 0, 96, '21c73787330e9b2d0de3c72bab8a24d28aa6765490b9ed621766f148ff886b78', 4, 13, 20, 4),
	(47, 'Calkins615@example.com', 'Waldefried', 'Auerbach', '1974-03-14', '0702497977', '6 Amwell Street', '2018-07-04', 45.00, 7342.56, 9.00, 1, 152, 'ec9f2c99c3b82593c2ec02eca8befb138e1acb844330000ef8bb581cd04b2298', 5, 20, 18, 9),
	(48, 'AntoineLittlefield@nowhere.com', 'Kresandra', 'Fuchs', '1967-03-18', '0758602395', '9 St. Alban\'s Place', '2014-06-27', 95.00, 6191.46, 5.00, 0, 112, '1d34fec2f9bd590700efc740ec1a03f726cf2bd835663e8ca92404e7dd085481', 6, 26, 7, 2),
	(49, 'jfhbwpxk.jxmonkyjvl@example.com', 'Rüder', 'üdiger', '1957-02-26', '0702495807', '12-17 Bishop\'s Bridge Road', '2020-04-13', 60.50, 7634.27, 8.00, 1, 87, '1f678b3f6ec73c5b9544c76354758cb82f8d1196fa68c43acc435aa7aa898ce8', 7, 37, 19, 9),
	(50, 'pqjndav80@example.com', 'Eyck', 'Heuer', '1971-01-29', '0778825391', '1 A-B Guilford Street', '2016-09-16', 70.00, 8998.51, 14.50, 0, 20, '89c195f17b27f42399098f9b743291dc04d7c7567b2cbbe8c509ea66a5a1cb3c', 1, 6, 14, 7),
	(51, 'john.smith@example.com', 'John', 'Smith', '1971-01-29', '0778825391', '1 A-B Guilford Street', '2016-09-16', 70.00, 8998.51, 14.50, 1, 23, '97c94ebe5d767a353b77f3c0ce2d429741f2e8c99473c3c150e2faa3d14c9da6', 7, 24, 17, 12),
	(52, 'mona.dupree@example.com', 'Mona', 'Dupree', '1971-01-29', '0778825391', '1 A-B Guilford Street', '2016-09-16', 70.00, 8998.51, 14.50, 1, 21, '97c94ebe5d767a353b77f3c0ce2d429741f2e8c99473c3c150e2faa3d14c9da6', 7, 24, 17, 9),
	(53, 'test1.1tset@example.com', '1tset', 'Test1', '1960-01-10', '', 'Road 66', '2021-09-27', 100.00, 9999.00, 0.00, 1, 0, '69aa423272eacf55bcbc6c36fc3923868565a2d2dc7ce18c1db1f9a44ac07f95', NULL, 1, 1, 1),
	(54, 'Christophine.Jeanne@example.com', 'Christophine', 'Jeanne', '1996-10-29', '071 435 32 23', 'Rue du Beau Site 12', '2022-03-30', 90.00, 9999.00, 0.00, 1, 0, 'b0f12793f06d849b8aa8b9d511f6995b38f53b6300085bad91f7e76467d12fd2', 53, 1, 13, 1),
	(55, 'sathu.jega@bg.com', 'Sathujan', 'Jegatheeswaran', '2002-06-02', '0772233212', 'Beacon Hills Steet 3', '2022-03-31', 10.00, 90000.00, 0.00, 1, 11, '6263496816cc4ab323e6a5a2357fc4e93200087e5b7e1099a97782c4cf5dc9c0', NULL, 1, 12, 1);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;

-- Listage de la structure de la table db_employees. employee_has_task
DROP TABLE IF EXISTS `employee_has_task`;
CREATE TABLE IF NOT EXISTS `employee_has_task` (
  `id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `task_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_employees_has_tasks_tasks1_idx` (`task_id`),
  KEY `fk_employees_has_tasks_employees1_idx` (`employee_id`),
  CONSTRAINT `fk_employee_has_task_employees1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `fk_employee_has_task_tasks1` FOREIGN KEY (`task_id`) REFERENCES `tasks` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table db_employees.employee_has_task : ~56 rows (environ)
/*!40000 ALTER TABLE `employee_has_task` DISABLE KEYS */;
INSERT INTO `employee_has_task` (`id`, `employee_id`, `task_id`) VALUES
	(1, 3, 7),
	(2, 23, 28),
	(3, 18, 27),
	(4, 42, 45),
	(5, 20, 1),
	(6, 46, 28),
	(7, 30, 21),
	(8, 18, 23),
	(9, 19, 42),
	(10, 47, 11),
	(11, 39, 4),
	(12, 3, 37),
	(13, 27, 8),
	(14, 11, 21),
	(15, 10, 42),
	(16, 19, 3),
	(17, 2, 5),
	(18, 34, 24),
	(19, 29, 33),
	(20, 24, 33),
	(21, 14, 4),
	(22, 10, 32),
	(23, 33, 22),
	(24, 12, 23),
	(25, 15, 47),
	(26, 34, 13),
	(27, 32, 41),
	(28, 20, 40),
	(29, 34, 37),
	(30, 36, 47),
	(31, 5, 13),
	(32, 16, 46),
	(33, 8, 19),
	(34, 44, 28),
	(35, 10, 19),
	(36, 22, 19),
	(37, 1, 4),
	(38, 41, 20),
	(39, 13, 43),
	(40, 41, 1),
	(41, 5, 20),
	(42, 30, 17),
	(43, 3, 12),
	(44, 44, 15),
	(45, 4, 4),
	(46, 25, 47),
	(47, 34, 8),
	(48, 36, 48),
	(49, 43, 2),
	(50, 24, 17),
	(51, 51, 51),
	(52, 51, 52),
	(53, 52, 53),
	(54, 52, 54),
	(55, 51, 55),
	(56, 51, 56),
	(57, 51, 57),
	(58, 55, 58),
	(59, 55, 59),
	(60, 55, 60);
/*!40000 ALTER TABLE `employee_has_task` ENABLE KEYS */;

-- Listage de la structure de la table db_employees. jobs
DROP TABLE IF EXISTS `jobs`;
CREATE TABLE IF NOT EXISTS `jobs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table db_employees.jobs : ~20 rows (environ)
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
INSERT INTO `jobs` (`id`, `name`) VALUES
	(4, 'Application Development Supervisor'),
	(6, 'Application Engineer'),
	(19, 'Area Administrator'),
	(8, 'Assistant Vice President'),
	(15, 'Chief Technology Officer'),
	(11, 'Communication Consultant'),
	(2, 'Computer Operator'),
	(16, 'Contract Advisor'),
	(14, 'Contract Manager'),
	(20, 'Finance Controller'),
	(5, 'Marketing Manager'),
	(17, 'Network Administrator'),
	(10, 'QA Engineer'),
	(13, 'Secretary'),
	(12, 'Senior Specialist'),
	(9, 'Service Manager'),
	(7, 'Technical Manager'),
	(18, 'Technical Specialist'),
	(3, 'Travel Agent'),
	(1, 'Vice President');
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;

-- Listage de la structure de la table db_employees. payslips
DROP TABLE IF EXISTS `payslips`;
CREATE TABLE IF NOT EXISTS `payslips` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file_path` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `employee_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `file_path_UNIQUE` (`file_path`),
  KEY `fk_payslips_employees1_idx` (`employee_id`),
  CONSTRAINT `fk_payslips_employees1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table db_employees.payslips : ~50 rows (environ)
/*!40000 ALTER TABLE `payslips` DISABLE KEYS */;
INSERT INTO `payslips` (`id`, `file_path`, `date`, `employee_id`) VALUES
	(1, '\\payslips\\3\\FEB-16.pdf', '2001-02-20', 3),
	(2, '\\payslips\\13\\NOV-17.pdf', '2001-04-20', 13),
	(3, '\\payslips\\33\\APR-17.pdf', '2001-07-20', 33),
	(4, '\\payslips\\39\\FEB-21.pdf', '2001-01-20', 39),
	(5, '\\payslips\\38\\NOV-19.pdf', '2001-02-20', 38),
	(6, '\\payslips\\28\\JUN-15.pdf', '2001-03-20', 28),
	(7, '\\payslips\\28\\JUN-18.pdf', '2001-03-20', 28),
	(8, '\\payslips\\46\\APR-20.pdf', '2001-08-20', 46),
	(9, '\\payslips\\28\\MAY-21.pdf', '2001-08-20', 28),
	(10, '\\payslips\\21\\SEP-20.pdf', '2001-04-20', 21),
	(11, '\\payslips\\37\\JAN-20.pdf', '2001-09-20', 37),
	(12, '\\payslips\\20\\MAY-21.pdf', '2001-04-20', 20),
	(13, '\\payslips\\12\\NOV-20.pdf', '2001-09-20', 12),
	(14, '\\payslips\\28\\SEP-20.pdf', '2001-01-20', 28),
	(15, '\\payslips\\20\\MAR-21.pdf', '2001-07-20', 20),
	(16, '\\payslips\\7\\JAN-20.pdf', '2001-06-20', 7),
	(17, '\\payslips\\23\\JAN-20.pdf', '2001-08-20', 23),
	(18, '\\payslips\\4\\JAN-16.pdf', '2001-06-20', 4),
	(19, '\\payslips\\23\\NOV-20.pdf', '2001-05-20', 23),
	(20, '\\payslips\\2\\DEC-20.pdf', '2001-01-20', 2),
	(21, '\\payslips\\28\\OCT-20.pdf', '2001-01-20', 28),
	(22, '\\payslips\\48\\OCT-21.pdf', '2001-09-20', 48),
	(23, '\\payslips\\32\\JUL-15.pdf', '2001-01-20', 32),
	(24, '\\payslips\\7\\OCT-17.pdf', '2001-09-20', 7),
	(25, '\\payslips\\28\\DEC-21.pdf', '2001-03-20', 28),
	(26, '\\payslips\\43\\JUN-21.pdf', '2001-09-20', 43),
	(27, '\\payslips\\30\\JUL-20.pdf', '2001-04-20', 30),
	(28, '\\payslips\\28\\AUG-19.pdf', '2001-07-20', 28),
	(29, '\\payslips\\40\\MAR-21.pdf', '2001-01-20', 40),
	(30, '\\payslips\\30\\SEP-20.pdf', '2001-04-20', 30),
	(31, '\\payslips\\28\\AUG-18.pdf', '2001-03-20', 28),
	(32, '\\payslips\\5\\MAY-20.pdf', '2001-04-20', 5),
	(33, '\\payslips\\36\\AUG-20.pdf', '2001-12-20', 36),
	(34, '\\payslips\\18\\JUL-19.pdf', '2001-05-20', 18),
	(35, '\\payslips\\17\\APR-18.pdf', '2001-07-20', 17),
	(36, '\\payslips\\9\\JAN-18.pdf', '2001-07-20', 9),
	(37, '\\payslips\\26\\OCT-20.pdf', '2001-05-20', 26),
	(38, '\\payslips\\5\\NOV-21.pdf', '2001-04-20', 5),
	(39, '\\payslips\\31\\APR-20.pdf', '2001-08-20', 31),
	(40, '\\payslips\\45\\JUN-21.pdf', '2001-01-20', 45),
	(41, '\\payslips\\15\\NOV-15.pdf', '2001-04-20', 15),
	(42, '\\payslips\\20\\FEB-16.pdf', '2001-09-20', 20),
	(43, '\\payslips\\49\\APR-20.pdf', '2001-06-20', 49),
	(44, '\\payslips\\26\\MAY-20.pdf', '2001-01-20', 26),
	(45, '\\payslips\\50\\JAN-21.pdf', '2001-02-20', 50),
	(46, '\\payslips\\2\\JUN-20.pdf', '2001-08-20', 2),
	(47, '\\payslips\\34\\DEC-19.pdf', '2001-07-20', 34),
	(48, '\\payslips\\34\\JUN-18.pdf', '2001-11-20', 34),
	(49, '\\payslips\\45\\OCT-19.pdf', '2001-05-20', 45),
	(50, '\\payslips\\42\\OCT-21.pdf', '2001-08-20', 42);
/*!40000 ALTER TABLE `payslips` ENABLE KEYS */;

-- Listage de la structure de la table db_employees. tasks
DROP TABLE IF EXISTS `tasks`;
CREATE TABLE IF NOT EXISTS `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `project` varchar(45) NOT NULL,
  `title` varchar(45) NOT NULL,
  `description` tinytext,
  `validation` tinyint(1) DEFAULT '0',
  `since` datetime NOT NULL,
  `until` datetime NOT NULL,
  `duration` time NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_tasks` (`project`,`title`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table db_employees.tasks : ~56 rows (environ)
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` (`id`, `project`, `title`, `description`, `validation`, `since`, `until`, `duration`) VALUES
	(1, 'EVDF93', 'Omnis et neque.', 'Quibusdam eos reprehenderit.', 1, '2015-01-01 00:00:02', '2015-01-02 15:17:29', '00:34:26'),
	(2, 'GMXT83', 'Enim minus.', 'Cumque et iusto fuga aut.', 1, '2021-03-25 23:42:05', '2021-03-30 22:41:06', '05:43:28'),
	(3, 'ITEI83', 'Libero.', 'Ut molestiae.', 1, '2021-04-06 04:42:35', '2021-04-08 21:46:26', '17:53:53'),
	(4, 'AAGP43', 'Et harum in;', 'Et aperiam.', 0, '2015-01-01 01:40:13', '2015-01-02 17:51:11', '16:30:24'),
	(5, 'ZATO33', 'Dolore ea.', 'Ipsa repellendus quas tempora.', 1, '2015-01-01 00:00:04', '2015-01-03 16:48:53', '23:29:01'),
	(6, 'WLCI83', 'Ea facere.', 'Qui quis voluptate tempore ut.', 1, '2016-02-04 18:21:11', '2016-02-08 19:51:12', '00:42:09'),
	(7, 'GIEV63', 'Nemo culpa sit.', 'Consectetur molestiae ut.', 1, '2019-09-06 03:33:55', '2019-09-10 14:46:31', '02:07:25'),
	(8, 'GFLP33', 'Quasi nulla.', 'Earum dolore ipsam maiores.', 0, '2017-05-15 00:16:32', '2017-05-19 10:10:07', '21:01:00'),
	(9, 'YQPP13', 'Ex maiores.', 'Sunt sed. Nulla alias quidem...', 1, '2016-02-17 13:53:20', '2016-02-21 10:57:28', '02:59:43'),
	(10, 'RCFQ43', 'Fugit et.', 'Dolor ea aut perspiciatis;', 1, '2019-05-05 05:23:27', '2019-05-08 13:10:07', '09:13:45'),
	(11, 'LFXM63', 'Magni dolore;', 'Voluptas perspiciatis.', 1, '2015-01-01 00:09:49', '2015-01-05 21:25:48', '00:00:05'),
	(12, 'SAFL93', 'Sint error.', 'Sed eaque sed sapiente alias.', 1, '2017-11-10 04:35:16', '2017-11-11 14:15:44', '11:57:44'),
	(13, 'FHDI23', 'Error et.', 'Quidem illo sunt magni.', 1, '2015-01-01 00:00:58', '2015-01-03 13:55:52', '14:08:53'),
	(14, 'IMXR83', 'Molestiae enim.', 'Consequatur illum. Ut.', 1, '2021-02-12 06:22:36', '2021-02-14 16:04:19', '23:49:19'),
	(15, 'AJNM93', 'At et ut.', 'Ut vel. Sit dolorum!', 1, '2016-02-18 22:12:40', '2016-02-23 05:04:59', '00:03:03'),
	(16, 'XMFO63', 'Sit ullam;', 'Non nemo illo dolor...', 0, '2015-01-01 00:13:13', '2015-01-02 21:17:13', '19:39:40'),
	(17, 'LAVQ13', 'Natus aut cum.', 'Explicabo repudiandae ab.', 1, '2015-01-01 02:23:33', '2015-01-04 20:09:58', '00:09:26'),
	(18, 'VDDZ63', 'Nam sint.', 'Quo exercitationem. Molestias?', 1, '2020-12-13 17:38:22', '2020-12-17 23:32:02', '18:59:22'),
	(19, 'AJZG63', 'Voluptatem;', 'Et quod; accusantium.', 0, '2019-05-21 07:42:49', '2019-05-23 06:19:44', '22:46:40'),
	(20, 'LNJP13', 'Omnis.', 'Repudiandae laboriosam.', 1, '2017-10-10 09:08:03', '2017-10-12 18:27:41', '00:49:10'),
	(21, 'RJSZ93', 'Et est ut quo.', 'Maiores reprehenderit et.', 1, '2015-01-01 00:16:33', '2015-01-04 12:45:25', '12:01:14'),
	(22, 'GDJG33', 'Labore hic qui.', 'Aliquam sit. Recusandae est.', 1, '2015-01-01 02:07:36', '2015-01-05 07:02:31', '00:00:10'),
	(23, 'CUQL43', 'Saepe in aut.', 'Quaerat minima et ut...', 1, '2015-11-22 12:29:38', '2015-11-25 13:25:21', '00:00:24'),
	(24, 'TLHU83', 'Repudiandae;', 'Sit numquam laborum...', 1, '2015-01-01 00:00:08', '2015-01-02 21:09:49', '18:36:26'),
	(25, 'KLRV13', 'Laudantium.', 'Aut rerum. Ipsam omnis sed.', 1, '2020-12-19 00:51:22', '2020-12-20 20:21:00', '21:39:52'),
	(26, 'UDRC93', 'Quis.', 'Magni ut saepe. Sequi aliquam.', 1, '2019-05-21 12:10:05', '2019-05-24 01:51:38', '03:59:38'),
	(27, 'LJPD13', 'Nostrum.', 'Unde sit voluptatem;', 1, '2018-08-06 19:45:14', '2018-08-09 18:03:56', '04:02:53'),
	(28, 'DDFO33', 'Natus.', 'Non rem.', 1, '2019-12-17 18:43:43', '2019-12-20 22:05:36', '21:46:03'),
	(29, 'FEPM43', 'Omnis itaque.', 'Nam itaque non debitis.', 1, '2020-03-26 21:06:57', '2020-03-28 08:19:30', '14:26:15'),
	(30, 'CRLB93', 'Sit blanditiis;', 'Voluptatem ea eius soluta.', 0, '2021-06-08 15:00:19', '2021-06-12 18:50:22', '00:01:22'),
	(31, 'FMZE43', 'Earum quia.', 'Quos eius. Quis eum.', 1, '2015-01-01 00:00:01', '2015-01-04 07:11:55', '14:01:02'),
	(32, 'TQPY23', 'Ipsa vero et.', 'Cum sit ipsa ut rem.', 1, '2015-01-01 00:01:40', '2015-01-04 01:36:26', '00:10:28'),
	(33, 'RFFA53', 'Ut qui ipsam.', 'Quia est. Perferendis!', 1, '2015-12-05 05:05:28', '2015-12-09 08:05:42', '00:19:33'),
	(34, 'HVVB13', 'Beatae.', 'Nihil ab. Velit magnam!', 1, '2015-01-01 00:00:40', '2015-01-05 04:32:14', '01:48:41'),
	(35, 'PVXO33', 'Voluptates.', 'Omnis ipsum; architecto.', 1, '2019-12-09 04:31:53', '2019-12-12 02:34:12', '12:00:52'),
	(36, 'FIQV13', 'Quae sit odio.', 'In quasi; deleniti rem.', 1, '2015-01-01 00:06:37', '2015-01-03 23:07:59', '14:34:47'),
	(37, 'NTLH23', 'Ab dolor neque.', 'Odio ad. Explicabo illum.', 1, '2020-09-14 11:15:56', '2020-09-15 20:43:36', '15:00:49'),
	(38, 'BJMU93', 'Et ut officiis.', 'Quam est quae odio est.', 1, '2016-12-03 10:37:31', '2016-12-05 03:45:04', '20:59:29'),
	(39, 'IYXW33', 'Molestiae.', 'Possimus eveniet adipisci qui.', 1, '2017-01-27 04:32:08', '2017-01-28 22:19:24', '10:48:45'),
	(40, 'SUWW73', 'Odio odit.', 'Officiis odit vel. Voluptas...', 1, '2015-01-01 00:00:10', '2015-01-03 18:04:39', '07:29:08'),
	(41, 'EDIF53', 'Sed est.', 'Qui unde quibusdam sunt;', 0, '2021-09-08 15:45:10', '2021-09-12 00:37:03', '00:12:49'),
	(42, 'IQQA73', 'Sed aliquid.', 'Dolorem doloribus; et maiores.', 1, '2016-05-26 10:22:00', '2016-05-27 10:58:21', '01:48:22'),
	(43, 'ZRNF63', 'Maxime illo.', 'Fugiat perferendis;', 1, '2015-01-01 06:27:14', '2015-01-02 11:25:51', '09:57:04'),
	(44, 'ZMES63', 'Facere quis.', 'Perspiciatis voluptas omnis.', 1, '2015-01-01 00:01:21', '2015-01-03 18:37:30', '20:36:58'),
	(45, 'MZOT93', 'Qui ut.', 'Itaque quisquam.', 1, '2015-10-08 17:40:13', '2015-10-11 09:24:32', '00:08:18'),
	(46, 'VLBM93', 'Et sed.', 'Laboriosam obcaecati.', 1, '2015-01-01 00:01:44', '2015-01-05 00:10:41', '19:15:33'),
	(47, 'MTGZ33', 'Quia.', 'Hic sit.', 1, '2015-01-01 00:05:01', '2015-01-04 06:28:32', '00:01:34'),
	(48, 'IJVR23', 'Eum.', 'Sit eos veritatis unde magnam.', 1, '2015-01-01 00:00:07', '2015-01-02 13:34:12', '01:08:03'),
	(49, 'HDYC33', 'Autem magni.', 'Sint quae architecto ipsa.', 1, '2020-09-26 02:45:24', '2020-09-28 05:46:55', '02:12:08'),
	(50, 'JMFT93', 'Est dolore.', 'Deleniti ut. Sit cupiditate.', 1, '2021-01-28 09:00:08', '2021-01-30 18:01:53', '06:57:33'),
	(51, 'AB23', 'creation dépôt git', '', 0, '2022-03-28 08:00:00', '2022-03-28 08:05:00', '00:05:00'),
	(52, 'ABC Project', 'Secret', '', 0, '2022-03-28 10:00:00', '2022-03-28 11:00:00', '01:00:00'),
	(53, 'test1', 'task1', 'adfafdafafdaffd', 0, '2022-03-28 08:00:00', '2022-03-28 09:10:00', '01:10:00'),
	(54, 'Test1', 'task2', '                                                                                 \r\n                                        ', 0, '2022-03-28 10:00:00', '2022-03-28 10:01:00', '00:01:00'),
	(55, 'Pré-TPI', 'Archivage d\'employés', 'fonction permettant d\'archiver un/e employé/e de la liste des employés', 0, '2022-03-29 23:00:00', '2022-03-29 23:15:00', '00:15:00'),
	(56, 'Pré-TPI', 'Test de caracères spéciaux', '[!@#$%^&*(),.?":{}|<>]', 0, '2022-03-29 23:15:00', '2022-03-29 23:17:00', '00:02:00'),
	(57, 'Pré-TPI', 'Conception', '', 0, '2022-02-11 11:15:00', '2022-02-11 12:15:00', '01:00:00'),
	(58, 'entrer dans la légende', 'La légende', 'Comme le projet l\'indique\r\n', 0, '2022-12-13 12:12:00', '2022-12-13 12:13:00', '00:01:00'),
	(59, 'Entrer chez les Heros', 'Héros', 'Je rentre actuellement dans la légende\r\nmaintenant les héros', 0, '2022-06-30 09:59:00', '2022-06-30 10:00:00', '00:01:00'),
	(60, 'entrer chez moi', 'chez moi', 'la c\'est chaud faut que je rentre chez moi', 0, '2022-06-20 09:00:00', '2022-06-20 20:00:00', '11:00:00');
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
