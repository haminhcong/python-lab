DROP TABLE IF EXISTS customer;
CREATE TABLE customer(
  id INTEGER not null PRIMARY KEY autoincrement,
  customer_name VARCHAR(30) not NULL,
  account_name VARCHAR(30) not NULL,
  email VARCHAR(30) NOT NULL ,
  password VARCHAR (30) not null,
  mobile_phone VARCHAR(30) NOT NULL ,
  address varchar(60) NOT NULL

);
DROP TABLE IF EXISTS role;
CREATE TABLE role(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
  name VARCHAR(30) NOT NULL
);
DROP TABLE IF EXISTS account_role;
CREATE TABLE account_role(
  account_id INTEGER NOT NULL ,
  role_id INTEGER NOT NULL ,
  PRIMARY KEY (account_id,role_id),
  FOREIGN KEY (account_id) REFERENCES customer(id),
  FOREIGN KEY (role_id) REFERENCES role(id)
);
DROP TABLE IF EXISTS customer_order;
CREATE TABLE customer_order(
  id INTEGER not null PRIMARY KEY autoincrement,
  order_date DATE not null,
  total INTEGER not null,
  customer_id INTEGER not NULL,
  FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);
DROP TABLE IF EXISTS item;
CREATE TABLE item(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
  product_code VARCHAR(30) NOT NULL ,
  product_name VARCHAR(40) NOT NULL ,
  quantity INTEGER NOT NULL ,
  price INTEGER NOT NULL ,
  order_id INTEGER NOT NULL ,
  FOREIGN KEY (order_id) REFERENCES customer_order(id)
);
DROP TABLE IF EXISTS manufacture;
CREATE TABLE manufacture(
  id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT ,
  name VARCHAR(30) NOT NULL
);
DROP TABLE IF EXISTS product;
CREATE TABLE product(
  product_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
  product_code VARCHAR(30) NOT NULL,
  product_name VARCHAR(40) NOT NULL ,
  price INTEGER NOT NULL ,
  description VARCHAR(400) NOT NULL ,
  promotion VARCHAR(300) NOT NULL ,
  image VARCHAR(40) NOT NULL,
  warranty INTEGER NOT NULL ,
  manufacture_id INTEGER NOT NULL,
  FOREIGN KEY (manufacture_id) REFERENCES manufacture(id)
);
DROP TABLE IF EXISTS product_image;
CREATE TABLE product_image(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  product_id INTEGER NOT NULL,
  location_directory VARCHAR(100) NOT NULL,
  FOREIGN KEY (product_id) REFERENCES product(product_id)
);
DROP TABLE IF EXISTS comment;
CREATE TABLE comment(
  product_id INTEGER NOT NULL PRIMARY KEY ,
  content VARCHAR(300)NOT NULL,
  FOREIGN KEY (product_id) REFERENCES product(product_id)
);
DROP TABLE IF EXISTS laptop_screen;
CREATE TABLE laptop_screen(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
  screen_size  FLOAT NOT NULL,
  resolution_width INTEGER NOT NULL ,
  resolution_height INTEGER NOT NULL
);
DROP TABLE IF EXISTS laptop;
CREATE TABLE laptop(
  product_id INTEGER NOT NULL PRIMARY KEY ,
  processor_name VARCHAR(40) NOT NULL ,
  memory VARCHAR(40) NOT NULL,
  storage VARCHAR(40) NOT NULL,
  graphic_card VARCHAR(40) NOT NULL,
  screen_id INTEGER NOT NULL,
  FOREIGN KEY (product_id) REFERENCES product(product_id),
  FOREIGN KEY (screen_id) REFERENCES laptop_screen(id)
);

DROP TABLE IF EXISTS best_seller_product;
CREATE TABLE best_seller_product(
  id INTEGER NOT NULL PRIMARY KEY ,
  FOREIGN KEY (id) REFERENCES product(id)
)