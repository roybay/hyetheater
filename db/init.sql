USE db;

CREATE TABLE members (
  member_id INT AUTO_INCREMENT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(100),
  PRIMARY KEY (member_id)
);

INSERT INTO members (
  first_name, 
  last_name, 
  email
) VALUES (
  'John', 
  'Doe', 
  'john.doe@example.com'
);

INSERT INTO members (
  first_name, 
  last_name, 
  email
) VALUES (
  'Roy', 
  'Boy', 
  'roy.boy@example.com'
);

INSERT INTO members (
  first_name, 
  last_name, 
  email
) VALUES (
  'Tom', 
  'Cruz', 
  'tom.cruz@example.com'
);
