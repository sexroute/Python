drop database if exists test;
create database test default character set utf8;

use test;
drop table tweet;
create table tweet (
	uid bigint auto_increment primary key,
	id bigint,
	tweet varchar(150),
	created_date datetime
)engine=innodb;

drop table comment;
create table comment (
	uid bigint auto_increment primary key,
	id bigint,
	comment varchar(150),
	created_date datetime
)engine=innodb;


select * from tweet;
select * from comment;

INSERT INTO weibo (id,tweet,comment) values (373944822506238000,'生命，始于吸气。终于呼出最后一口气。一呼一吸间，经历高低起伏，品味悲欢离合。我们只得任脚走，憋住气去走人生路。《人间小团圆》透过郑家三代貌似风平浪静的安逸生活，带出各人成长中隐藏的伤痕与阴影，从中领略各自成长的释怀和感悟。郑惠清（杨千嬅 饰）任职博物馆导赏员，与丈夫邱健章（曾志伟）','生命，始于吸气。终于呼出最后一口气。一呼一吸间，经历高低起伏，品味悲欢离合。我们只得任脚走，憋住气去走人生路。《人间小团圆》透过郑家三代貌似风平浪静的安逸生活，带出各人成长中隐藏的伤痕与阴影，从中领略各自成长的释怀和感悟。郑惠清（杨千嬅 饰）任职博物馆导赏员，与丈夫邱健章（曾志伟）');





USE test;
drop table dmoz;
CREATE TABLE dmoz (
   id  INT AUTO_INCREMENT PRIMARY KEY,
   titile VARCHAR(100),
   link VARCHAR(255),
   description  TEXT,
   created DATETIME
)ENGINE=InnoDB; 

select * from dmoz;