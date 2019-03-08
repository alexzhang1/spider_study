# Host: 127.0.0.1  (Version: 5.6.24)
# Date: 2018-07-24 16:48:42
# Generator: MySQL-Front 5.3  (Build 4.271)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "lianjia_cj"
#

DROP TABLE IF EXISTS `lianjia_cj`;
CREATE TABLE `lianjia_cj` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` char(10) DEFAULT NULL,
  `region` char(10) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `name` char(20) DEFAULT NULL,
  `style` char(20) DEFAULT NULL,
  `area` char(20) DEFAULT NULL,
  `orientation` char(20) DEFAULT NULL,
  `decoration` char(10) DEFAULT NULL,
  `elevator` char(10) DEFAULT NULL,
  `floor` char(10) DEFAULT NULL,
  `build_year` char(20) DEFAULT NULL,
  `sign_time` char(20) DEFAULT NULL,
  `unit_price` char(20) DEFAULT NULL,
  `total_price` char(20) DEFAULT NULL,
  `fangchan_class` char(20) DEFAULT NULL,
  `school` char(20) DEFAULT NULL,
  `subway` char(20) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
