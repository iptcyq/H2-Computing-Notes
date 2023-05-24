CREATE TABLE `Device` (
	`SerialNumber`	INTEGER NOT NULL UNIQUE,
	`Type`	TEXT,
	`Model`	TEXT,
	`Location`	TEXT,
	`DateOfPurchase`	TEXT,
	`WrittenOff`	INTEGER,
	PRIMARY KEY(`SerialNumber`)
);
CREATE TABLE `Monitor` (
	`SerialNumber`	INTEGER NOT NULL,
	`DateCleaned`	TEXT,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`)
);
CREATE TABLE `Laptop` (
	`SerialNumber`	INTEGER NOT NULL,
	`WeightKg`	REAL,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`)
);
CREATE TABLE `Printer` (
	`SerialNumber`	INTEGER NOT NULL,
	`Toner`	TEXT,
	`DateChanged`	TEXT,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`)
);