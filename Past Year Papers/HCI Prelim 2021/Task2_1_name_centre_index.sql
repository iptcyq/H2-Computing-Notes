CREATE TABLE `Log` (
	`LogID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`Sender`	TEXT NOT NULL,
	`AccessDate`	TEXT NOT NULL,
	`Status`	INTEGER NOT NULL,
	`AppType`	TEXT
);