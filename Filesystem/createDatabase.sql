DROP TABLE IF EXISTS Directory;
DROP TABLE IF EXISTS File;
DROP TABLE IF EXISTS Folder;

-- will only have one row, the current directory
CREATE TABLE IF NOT EXISTS Directory(
    directory VARCHAR(500) NOT NULL PRIMARY KEY
);

-- list of all folders and their paths
CREATE TABLE IF NOT EXISTS Folder(
    folderID INT(11) NOT NULL AUTO_INCREMENT,
    path VARCHAR(500) NOT NULL,
    folderName VARCHAR(100) NOT NULL,
    PRIMARY KEY(folderID)
);

-- list of all files and their folders
CREATE TABLE IF NOT EXISTS File(
    fileID INT(11) NOT NULL AUTO_INCREMENT,
    folderID VARCHAR(500) NOT NULL,
    fileName VARCHAR(100) NOT NULL,
    permissionModes VARCHAR(9),
    numLinks INT(10),
    owner VARCHAR(100),
    group VARCHAR(100),
    size INT(100),
    type VARCHAR(10),
    dateModified datetime,
    PRIMARY KEY(fileID),
    FOREIGN KEY (folderID) REFERENCES Folder(folderID) ON UPDATE CASCADE ON DELETE CASCADE
);