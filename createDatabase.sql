DROP TABLE IF EXISTS ReadPost;
DROP TABLE IF EXISTS Post;
DROP TABLE IF EXISTS Friend;
DROP TABLE IF EXISTS React;
DROP TABLE IF EXISTS Response;
DROP TABLE IF EXISts Subtopic;

DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Topic;
DROP TABLE IF EXISTS FriendGroup;
DROP TABLE IF EXISTS ReactType;
DROP TABLE IF EXISTS GroupMember;

-- person table
CREATE TABLE IF NOT EXISTS Person(
    personID INT(11) NOT NULL AUTO_INCREMENT,
    lastName VARCHAR(100) NOT NULL,
    firstName VARCHAR(100) NOT NULL,
    middleName VARCHAR(100),
    -- YYYYMMDD
    birthday INT(8),
    -- M/F
    sex VARCHAR(1),
    age INT(11),
    city VARCHAR(100),
    country VARCHAR(100),
    job VARCHAR(100),
    PRIMARY KEY(personID)
);

-- topics people can follow
CREATE TABLE IF NOT EXISTS Topic(
    topicID INT(11) NOT NULL AUTO_INCREMENT,
    topic VARCHAR(100) NOT NULL,
    PRIMARY KEY(topicID)
);

-- groups
CREATE TABLE IF NOT EXISTS FriendGroup(
    groupID INT(11) NOT NULL AUTO_INCREMENT,
    groupName VARCHAR(100) NOT NULL,
    PRIMARY KEY(groupID)
);

-- possible react types to posts
CREATE TABLE IF NOT EXISTS ReactType(
    reactTypeID INT(11) NOT NULL,
    react VARCHAR(100) NOT NULL,
    PRIMARY KEY(reactTypeID)
);

INSERT INTO ReactType (reactTypeID, react) VALUES
(0, 'Thumbs Up'),
(1, 'Thumbs Down'),
(2, 'Useful'),
(3, 'Funny');

-- reacts to posts, each person can only have one reaction to a post
CREATE TABLE IF NOT EXISTS React(
    postID INT(11) NOT NULL,
    personID INT(11) NOT NULL,
    reactTypeID INT(11) NOT NULL,
    CONSTRAINT FK_React_postID FOREIGN KEY (postID) REFERENCES Topic(topicID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_React_personID FOREIGN KEY (personID) REFERENCES Person(personID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_React_reactTypeID FOREIGN KEY (reactTypeID) REFERENCES ReactType(reactTypeID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT PK_React PRIMARY KEY(postID, personID)
);

-- posts
CREATE TABLE IF NOT EXISTS Post(
    postID INT(11) NOT NULL AUTO_INCREMENT,
    -- can only have one topic
    topicID INT(11) NOT NULL,
    personID INT(11) NOT NULL,
    body VARCHAR(255) NOT NULL,
    CONSTRAINT FK_Post_topicID FOREIGN KEY (topicID) REFERENCES Topic(topicID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_Post_personID FOREIGN KEY (personID) REFERENCES Person(personID) ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY(postID)
);

-- shows if an person has read a post
CREATE TABLE IF NOT EXISTS ReadPost(
    postID INT(11) NOT NULL,
    personID INT(11) NOT NULL,
    CONSTRAINT FK_ReadPost_postID FOREIGN KEY (postID) REFERENCES Post(postID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_ReadPost_personID FOREIGN KEY (personID) REFERENCES Person(personID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT PK_ReadPost PRIMARY KEY(postID, personID)
);

-- friend pairs, two people are friends if the two personIDs are either personOne or personTwo
CREATE TABLE IF NOT EXISTS Friend(
    personOne INT(11) NOT NULL,
    personTwo INT(11) NOT NULL,
    CONSTRAINT FK_Friend_personOne FOREIGN KEY (personOne) REFERENCES Person(PersonID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_Friend_personTwo FOREIGN KEY (personTwo) REFERENCES Person(personID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT PK_Friend PRIMARY KEY(personOne, personTwo)
);

-- shows members that are in each group
CREATE TABLE IF NOT EXISTS GroupMember(
    groupID INT(11) NOT NULL,
    personID INT(11) NOT NULL,
    CONSTRAINT FK_GroupMember_personID FOREIGN KEY (personID) REFERENCES Person(personID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_GroupMember_groupID FOREIGN KEY (groupID) REFERENCES FriendGroup(groupID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT PK_GroupMember PRIMARY KEY(groupID, personID)
);

-- shows which posts are responses to other posts
CREATE TABLE IF NOT EXISTS Response(
    responseID INT(11) NOT NULL,
    parentPostID INT(11) NOT NULL,
    CONSTRAINT FK_Response_responseID FOREIGN KEY (responseID) REFERENCES Post(postID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_Response_parentPostID FOREIGN KEY (parentPostID) REFERENCES Post(postID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT PK_Response PRIMARY KEY(responseID, parentPostID)
);

-- links the subtopics to its topics; each subtopic can only have one parent topic
CREATE TABLE IF NOT EXISTS Subtopic(
    subtopicID INT(11) NOT NULL,
    topicID INT(11) NOT NULL,
    CONSTRAINT FK_Subtopic_subtopicID FOREIGN KEY (subtopicID) REFERENCES Topic(topicID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_Subtopic_topicID FOREIGN KEY (topicID) REFERENCES Topic(topicID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT PK_Subtopic PRIMARY KEY(subtopicID, topicID)
);

-- shows all the topics that each person follows
CREATE TABLE IF NOT EXISTS FollowedTopic(
    personID INT(11) NOT NULL,
    topicID INT(11) NOT NULL,
    CONSTRAINT FK_FollowedTopic_personID FOREIGN KEY (personID) REFERENCES Person(personID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_FollowedTopic_topicID FOREIGN KEY (topicID) REFERENCES Topic(topicID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT PK_FollowedTopic PRIMARY KEY(personID, topicID)
);