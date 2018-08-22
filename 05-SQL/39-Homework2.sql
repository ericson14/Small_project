1.
create table student(
  id int(10) not null unique primary key,
  name varchar(20) not null,
  gender varchar(4),
  birth year,
  department varchar(20),
  address varchar(50)
);
create table score(
    id int(10) not null unique primary key auto_increment,
    stu_id int(10) not null,
    c_name varchar(20),
    grade int(10)
);
insert into student values
( 901,'张老大','男',1985,'计算机系','北京市海淀区'),
( 902,'张老二', '男',1986,'中文系', '北京市昌平区'),
( 903,'张三', '女',1990,'中文系', '湖南省永州市'),
( 904,'李四', '男',1990,'英语系', '辽宁省阜新市'),
( 905,'王五', '女',1991,'英语系', '福建省厦门市'),
( 906,'王六', '男',1988,'计算机系', '湖南省衡阳市');
insert into score values
(NULL,901, '计算机',98),
(NULL,901, '英语', 80),
(NULL,902, '计算机',65),
(NULL,902, '中文',88),
(NULL,903, '中文',95),
(NULL,904, '计算机',70),
(NULL,904, '英语',92),
(NULL,905, '英语',94),
(NULL,906, '计算机',90),
(NULL,906, '英语',85);

select * from student;
select * from student limit 1,3;
select id,name,department from student;
select * from student where department="英语系" or department="计算机系";
select * from student where year(now())-birth between 22 and 28;
select department,count(*) from student group by department;
select max(grade), c_name from score group by c_name;
select c_name, grade from score where stu_id=(select s.id from student as s where name="李四");
select * from student as s inner join score as t on s.id=t.stu_id;
select b.name, sum(grade) from score as a inner join student as b on a.stu_id=b.id group by a.stu_id;
select c_name, avg(grade) from score group by c_name;
select * from student where id in (select stu_id from score where grade<95 and c_name='计算机');
select grade from score where c_name='计算机' and stu_id = (select s.id from student as s) order by grade desc;
select name, department, b.grade, b.c_name  from student as s left join score as b on s.id=b.stu_id where name rlike '^(张|王).*';
select name, department, (year(now())-s.year) as age, b.grade, b.c_name from student as s left join score as b on s.id=b.stu_id where s.address like '湖南%';

create table temp (p int)select id from test where id not in (select min(id) from test group by code);

delete from test where id in temp.id;





