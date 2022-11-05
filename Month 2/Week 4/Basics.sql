create table basic_sql.student (
student_id int primary key,
student_name varchar (20),
major varchar (20)
);

describe basic_sql.student;

DROP TABLE basic_sql.student;

alter table basic_sql.student add gpa decimal (3,2);

alter table basic_sql.student drop column gpa;


INSERT INTO basic_sql.student VALUES(1, 'Jack', 'Biology');
INSERT INTO basic_sql.student VALUES(2, 'Kate', 'Sociology');
INSERT INTO basic_sql.student (student_id, student_name) VALUES(3, 'Claire');
INSERT INTO basic_sql.student VALUES(4, 'Jack', 'Biology');
INSERT INTO basic_sql.student VALUES(5, 'Mike', 'Computer Science');


CREATE TABLE basic_sql.student (
  student_id INT PRIMARY KEY AUTO_INCREMENT,
  student_name VARCHAR(40) NOT NULL,
  -- name VARCHAR(40) UNIQUE,
  major VARCHAR(40) DEFAULT 'undecided'
);

INSERT INTO basic_sql.student (student_name, major) VALUES('Jack', 'Biology');
INSERT INTO basic_sql.student (student_name, major) VALUES('Kate', 'Sociology');
INSERT INTO basic_sql.student (student_name, major) VALUES('Blake', 'Biology');
INSERT INTO basic_sql.student (student_name, major) VALUES('Mike', 'Computer Science');


update basic_sql.student 
set  major = 'Bio'
WHERE major = 'Biology';

UPDATE student
SET student_name = 'Johnny'
WHERE student_id = 4;


UPDATE student
SET major = 'Undecided', student_name = 'Tom'
WHERE student_id = 4;


DELETE FROM student
WHERE student_id = 4;

SET SQL_SAFE_UPDATES=0;
DELETE FROM student
WHERE major = 'Sociology' AND student_name = 'Kate';
SET SQL_SAFE_UPDATES=1;


SELECT *
FROM student;

SELECT student.student_name, student.major
FROM student;

SELECT *
FROM student
WHERE student_name = 'Jack';

SELECT *
FROM student
WHERE student_id > 2;

SELECT *
FROM student
WHERE major = 'Biology' AND student_id > 1;


select * from basic_sql.student;