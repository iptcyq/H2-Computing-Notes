CREATE DATABASE 'JPFashion.db';

CREATE TABLE `Customer` (
	`Email`	TEXT,
	`FirstName`	TEXT,
	`LastName`	TEXT,
	`ContactNumber`	TEXT,
	`DOB`	TEXT,
	`Address`	TEXT,
	PRIMARY KEY(`Email`)
);

CREATE TABLE `Product` (
	`CatalogueNumber`	INTEGER,
	`Category`	TEXT,
	`Brand`	TEXT,
	`Size`	INTEGER,
	`Fee`	INTEGER,
	PRIMARY KEY(`CatalogueNumber`)
);

CREATE TABLE `CustomerRental` (
	`ID`	INTEGER,
	`Email`	TEXT,
	`StartDate`	INTEGER,
	`EndDate`	INTEGER,
	PRIMARY KEY(`ID`),
	FOREIGN KEY(`Email`) REFERENCES `Customer`(`Email`)
);

CREATE TABLE `ProductRental` (
	`ID`	INTEGER,
	`CatalogueNumber`	INTEGER,
	`Returned`	TEXT,
	PRIMARY KEY(`ID`,`CatalogueNumber`),
	FOREIGN KEY(`ID`) REFERENCES `CustomerRental`(`ID`)
);