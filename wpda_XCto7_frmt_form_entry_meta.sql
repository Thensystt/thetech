/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Create table `XCto7_frmt_form_entry_meta`
--
CREATE TABLE `XCto7_frmt_form_entry_meta` (
  `meta_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `entry_id` bigint(20) unsigned NOT NULL,
  `meta_key` varchar(191) DEFAULT NULL,
  `meta_value` longtext DEFAULT NULL,
  `date_created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `date_updated` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`meta_id`),
  KEY `meta_key` (`meta_key`),
  KEY `meta_entry_id` (`entry_id`),
  KEY `meta_key_object` (`entry_id`,`meta_key`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Export table `XCto7_frmt_form_entry_meta`
--
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (1,1,'name-1','luihbli','2024-01-27 20:13:35','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (2,1,'radio-1','Подписать через QR Egov','2024-01-27 20:13:35','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (3,1,'upload-1','a:1:{s:4:\"file\";a:5:{s:7:\"success\";b:1;s:9:\"file_name\";s:34:\"fG7KPo6qhPVB-Alimov-Madiyar-CV.pdf\";s:8:\"file_url\";s:138:\"https://halyklife.thetech.kz/wp-content/uploads/forminator/298_1f19f5ad7e51cdd1126de9fd17d6f44b/uploads/fG7KPo6qhPVB-Alimov-Madiyar-CV.pdf\";s:7:\"message\";s:0:\"\";s:9:\"file_path\";s:153:\"/var/www/vhosts/thetech.kz/halyk.thetech.kz/wp-content/uploads/forminator/298_1f19f5ad7e51cdd1126de9fd17d6f44b/uploads/fG7KPo6qhPVB-Alimov-Madiyar-CV.pdf\";}}','2024-01-27 20:13:35','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (4,1,'consent-1','проверено','2024-01-27 20:13:35','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (5,1,'_forminator_user_ip','89.250.83.178','2024-01-27 20:13:35','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (6,2,'radio-1','Подписать через QR Egov','2024-01-27 20:25:31','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (7,2,'consent-1','проверено','2024-01-27 20:25:31','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (8,2,'text-1','021117550190','2024-01-27 20:25:31','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (9,2,'_forminator_user_ip','89.250.83.178','2024-01-27 20:25:31','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (10,3,'radio-1','Подписать через ЭЦП Ключ','2024-01-27 20:43:28','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (11,3,'upload-1','a:1:{s:4:\"file\";a:5:{s:7:\"success\";b:1;s:9:\"file_name\";s:20:\"pe1hicHiZW7X-634.png\";s:8:\"file_url\";s:124:\"https://halyklife.thetech.kz/wp-content/uploads/forminator/298_1f19f5ad7e51cdd1126de9fd17d6f44b/uploads/pe1hicHiZW7X-634.png\";s:7:\"message\";s:0:\"\";s:9:\"file_path\";s:139:\"/var/www/vhosts/thetech.kz/halyk.thetech.kz/wp-content/uploads/forminator/298_1f19f5ad7e51cdd1126de9fd17d6f44b/uploads/pe1hicHiZW7X-634.png\";}}','2024-01-27 20:43:28','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (12,3,'text-1','878767867868','2024-01-27 20:43:28','0000-00-00 00:00:00');
INSERT INTO `XCto7_frmt_form_entry_meta` (`meta_id`, `entry_id`, `meta_key`, `meta_value`, `date_created`, `date_updated`) VALUES (13,3,'_forminator_user_ip','89.250.83.178','2024-01-27 20:43:28','0000-00-00 00:00:00');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
