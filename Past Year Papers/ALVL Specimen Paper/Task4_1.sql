CREATE TABLE `Device` ( 
`SerialNumber` INTEGER, 
`Type` TEXT, 
`Model` TEXT, 
`Location` TEXT, 
`DateOfPurchase` INTEGER, 
`WrittenOff` TEXT, 
PRIMARY KEY(`SerialNumber`) )

CREATE TABLE `Monitor` ( 
`SerialNumber` INTEGER, 
`DateCleaned` INTEGER, 
PRIMARY KEY(`SerialNumber`), 
FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`) )

CREATE TABLE `Laptop` ( 
`SerialNumber` INTEGER, 
`WeightKg` INTEGER, 
FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`), 
PRIMARY KEY(`SerialNumber`) )

CREATE TABLE `Printer` ( 
`SerialNumber` INTEGER, 
`Toner` TEXT, 
`DateChanged` INTEGER, 
FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`), 
PRIMARY KEY(`SerialNumber`) )