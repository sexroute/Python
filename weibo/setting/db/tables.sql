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