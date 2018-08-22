1.
datadir           数据库存放路径：默认值 /var/lib/mysql
general_log_file  通用日志路径：默认值 /var/log/mysql/mysql.log
port              端口号：默认值 3306
bind-address      数据库服务端IP地址：默认值 127.0.0.1
log_err           错误日志：默认值 /var/log/mysql/error.log
2. 记录，字段，数据表，数据表库，主键
3. sudo service mysql start/stop/restart
4. mysql -u root -p(密码)
5.
show databases;
use xxx;
select database();
create database xxx charset=utf8;
drop database xxx;
6.
create database python charset=utf8;
7.
show tables;
desc xxx;
drop table xxx;
8.
create table classes(
  id int unsigned primary key not null auto_increment,
  name varchar(20) not null
);
9.
insert into xxx(xxx) value(xxx);
update xxx set xxx=xxx where xxx;
delete from xxx where xxx;
select * from classes;
10.
insert into classes(name) values ("python1"), ("python2"), ("python3");
11.
create table students(
  id int unsigned primary key not null auto_increment,
  name varchar(20) not null,
  birth date,
  gender enum("男", "女", "中性", "保密") default "保密",
  hometown varchar(40) default " ",
  cls_id int unsigned not null
);
12.1
insert into students values (0,"郭靖",1156-06-03,1,"蒙古",1);
insert into students values (0,"黄蓉",1160-01-10,2,"桃花岛",1);
12.2
insert into students(name,gender,cls_id) values ("杨过",1,2);
insert into students(name,gender,cls_id) values ("小龙女",2,2);
12.3
insert into students(name,cls_id) values ("黄药师",0),("洪七公",1),("洪七婆",1);
12.4
alter table students modify hometown varchar(30);
13
select name, birth from students;
14
select name, year(now())-year(birth) as age from students;
-- select name, floor(datediff(CURRENT_DATE, birth))/365 as age from students;
15
delete from students where name="洪七婆";
16
update students set gender=1 where name="洪七公";
17
create table subjects(
  id int unsigned primary key not null auto_increment,
  name varchar(40) not null,
  is_delete bit default 0
)
18
insert into subjects (name) values ("Python"),("数据库"),("前端");
19
create table grades(
  id int unsigned primary key not null auto_increment,
  std_id int unsigned not null,
  sub_id int unsigned not null,
  grade decimal(4,1),
  is_delete bit
)
alter table students change std_id stu_id int unsigned not null;
alter table students drop is_delete;

