#testdb的创建脚本

#创建表和索引
#创建表  lianjia_cj
	DROP TABLE  IF EXISTS testdb.lianjia_cj;
	CREATE TABLE testdb.lianjia_cj (
		id int(11) NOT NULL AUTO_INCREMENT,
	    city CHAR(10),
        region CHAR(10),
        href VARCHAR(255),
        name CHAR(20),
        style CHAR(20),
        area CHAR(20),
        orientation CHAR(20),
        decoration CHAR(10),
        elevator CHAR(10),
        floor CHAR(10),
        build_year CHAR(20),
        sign_time CHAR(20),
        unit_price CHAR(20),
        total_price CHAR(20),
        fangchan_class CHAR(20),
        school CHAR(20),
        subway CHAR(20),
		PRIMARY KEY (id  )	USING BTREE
	)ENGINE=InnoDB  DEFAULT CHARSET=utf8;