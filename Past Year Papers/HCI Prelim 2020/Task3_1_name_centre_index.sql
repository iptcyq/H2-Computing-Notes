CREATE TABLE `Product` ( 
`ProductCode` TEXT NOT NULL UNIQUE, 
`Name` TEXT NOT NULL, 
`Type` TEXT NOT NULL, 
`Location` TEXT NOT NULL, 
`Price` REAL NOT NULL, 
PRIMARY KEY(`ProductCode`) )

CREATE TABLE `Loaf` ( 
`ProductCode` TEXT NOT NULL UNIQUE, 
`Weight` REAL NOT NULL, 
FOREIGN KEY(`ProductCode`) REFERENCES `Product`(`ProductCode`), 
PRIMARY KEY(`ProductCode`) )

CREATE TABLE "Cake" ( 
`ProductCode` TEXT NOT NULL UNIQUE, 
`ServingSize` INTEGER NOT NULL, 
`Shape` TEXT NOT NULL, 
FOREIGN KEY(`ProductCode`) REFERENCES `Product`(`ProductCode`), 
PRIMARY KEY(`ProductCode`) )

CREATE TABLE `Bun` ( 
`ProductCode` TEXT NOT NULL UNIQUE, 
`PiecesPerPackage` INTEGER NOT NULL, 
FOREIGN KEY(`ProductCode`) REFERENCES `Product`(`ProductCode`), 
PRIMARY KEY(`ProductCode`) )