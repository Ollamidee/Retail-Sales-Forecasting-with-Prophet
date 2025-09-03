DROP DATABASE IF EXISTS `sales_project`;
CREATE DATABASE `sales_project`;

USE sales_project;

CREATE TABLE products (
	product_id VARCHAR(50),
    product_name VARCHAR(200),
    unit_price DECIMAL(10, 2),
    PRIMARY KEY(product_id)
    );
    
CREATE TABLE customers (
	customer_id INTEGER,
    country VARCHAR(50),
    PRIMARY KEY(customer_id)
    );
    
CREATE TABLE invoices (
	invoice_no VARCHAR(50),
    invoice_date DATE,
    customer_id INTEGER,
    PRIMARY KEY(invoice_no),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
    );

CREATE TABLE invoice_item (
	invoice_no VARCHAR(50),
    product_id VARCHAR(50),
    quantity INTEGER,
    PRIMARY KEY(invoice_no, product_id),
	FOREIGN KEY(invoice_no) REFERENCES invoices(invoice_no),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
    )
    
    
    
    