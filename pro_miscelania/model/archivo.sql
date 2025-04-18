create database miscelania;
use miscelania;

USE miscelania;

create table Ciudad(
	Ciud_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Ciud_Nom VARCHAR(60)
);

CREATE TABLE Cliente (
    Cliente_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    Cliente_Nom VARCHAR(60) NOT NULL,
    Cliente_Mail VARCHAR(60) NOT NULL,
    Cliente_Tel VARCHAR(60),
    Cliente_Direc VARCHAR(200),
    Ciud_Id INT,
    FOREIGN KEY (Ciud_id) REFERENCES Ciudad(Ciud_id)
    );
    
CREATE TABLE Proveedor (
    Prove_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Prove_Nom VARCHAR(60) NOT NULL,
    Prove_Mail VARCHAR(60) NOT NULL,
    Prove_Tel VARCHAR(60),
    Prove_Direc VARCHAR(200)
);

CREATE TABLE Categoria (
    Cate_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Cate_Nom VARCHAR(50) NOT NULL
);    

CREATE TABLE Producto (
    Producto_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Producto_Nom VARCHAR(50) NOT NULL,
    Producto_Precio INT NOT NULL,
    Cate_Id INT,
    FOREIGN KEY (Cate_Id) REFERENCES Categoria(Cate_Id)
);
    
CREATE TABLE Producto_Provedor (
	Producto_Id INT,
    Prove_Id INT,
    FOREIGN KEY (Producto_Id) REFERENCES Producto(Producto_Id),
    FOREIGN KEY (Prove_Id) REFERENCES Proveedor(Prove_Id)
);

CREATE TABLE Compra (
	Compra_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Compra_fecha DATE,
    Prove_Id INT,
    FOREIGN KEY (Prove_Id) REFERENCES Proveedor(Prove_Id)
);

CREATE TABLE Factura_Venta (
	Factura_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Factura_Fecha DATE,
	Cliente_Id INT,
	FOREIGN KEY (Cliente_Id) REFERENCES Cliente(Cliente_Id)
);

CREATE TABLE Factura_Producto (
	Factura_Id INT,
    Producto_Id INT,
    Cantidad INT,
    FOREIGN KEY (Factura_Id) REFERENCES Factura_Venta(Factura_Id),
    FOREIGN KEY (Producto_Id) REFERENCES Producto(Producto_Id)
);

CREATE TABLE Factura_Compra_Producto (
	Factura_Id INT,
    Producto_Id INT,
    Cantidad_Producto INT,
    Valor_Compra INT,
    FOREIGN KEY (Factura_Id) REFERENCES Factura_Venta(Factura_Id),
    FOREIGN KEY (Producto_Id) REFERENCES Producto(Producto_Id)
);    

CREATE TABLE Envios (
	Envi_Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Envi_Fecha DATE,
	Factura_Id INT,
	Cliente_Id INT,
	Ciud_Id INT,
	FOREIGN KEY (Factura_Id) REFERENCES Factura_Venta(Factura_Id),
	FOREIGN KEY (Cliente_Id) REFERENCES Cliente(Cliente_Id),
	FOREIGN KEY (Ciud_Id) REFERENCES Ciudad(Ciud_Id)
);