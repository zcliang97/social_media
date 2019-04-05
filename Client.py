# python -m pip install mysql-connector-python
import mysql.connector

class Client:
    def __init__(self):
        self.host="localhost"
        self.user="root"            # enter username
        self.passwd=""    # enter password
        self.db="Project"

    def createDBConn(self):
        db = mysql.connector.connect(host=self.host,
                       user=self.user,
                       passwd=self.passwd,
                       db=self.db)
        return db

    def closeDBConn(self, db):
        db.close()

    # only lastName, firstName are mandatory
    def createUser(self, lastName, firstName, middleName, birthday, sex, age, city, country, job):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO Person(lastName, firstName, middleName, birthday, sex, age, city, country, job)
            VALUES ("{lastName}", "{firstName}", "{middleName}", DATE("{birthday}"), "{sex}", "{age}", "{city}", "{country}", "{job}")
        """.format(
             lastName=lastName, 
             firstName=firstName, 
             middleName=middleName, 
             birthday=birthday, 
             sex=sex, 
             age=age, 
             city=city, 
             country=country, 
             job=job)
        )
        db.commit()

        cursor.execute("""
            SELECT MAX(personID) FROM Person;
        """)

        for row in cursor:
            personID = row[0]

        self.closeDBConn(db)

        print "Added User {lastName}, {firstName}!".format(lastName=lastName, firstName=firstName)
        
        return personID

    def createTopic(self, topicName):
        db = self.createDBConn()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO Topic(topic)
            VALUES ("{topicName}")
        """.format(topicName=topicName)
        )
        db.commit()
        self.closeDBConn(db)

        print "Added topic {topic}!".format(topic=topicName)

    def createSubtopic(self, topicName, parentTopicID):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO Topic(topic)
            VALUES ("{topicName}")
        """.format(topicName=topicName)
        )
        db.commit()

        cursor.execute("""
            SELECT MAX(topicID) FROM Topic;
        """)

        for row in cursor:
            cursor.execute("""
                INSERT INTO Subtopic(subtopicID, topicID)
                VALUES ({subtopicID}, {topicID})
            """.format(subtopicID=row[0], topicID=parentTopicID)
            )
            db.commit()
        self.closeDBConn(db)

        print "Added subtopic {topic}!".format(topic=topicName)

    def createPost(self, personID, topicID, body):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO Post(personID, topicID, body)
            VALUES ({personID}, {topicID}, "{body}")
        """.format(personID=personID, topicID=topicID, body=body))
        db.commit()
        self.closeDBConn(db)

        print "{personID} created post with id {topicID}!".format(personID=personID, topicID=topicID)

    def addFriend(self, personOneID, personTwoID):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO Friend(personOne, personTwo)
            VALUES ({personOne}, {personTwo})
        """.format(personOne=personOneID, personTwo=personTwoID))
        db.commit()
        self.closeDBConn(db)

        print "{personOneID} and {personTwoID} are now friends!".format(personOneID=personOneID, personTwoID=personTwoID)

    def respondToPost(self, personID, postID, topicID, body):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO Post(personID, topicID, body)
            VALUES ({personID}, {topicID}, "{body}")
        """.format(personID=personID, topicID=topicID, body=body))
        db.commit()

        cursor.execute("""
            SELECT MAX(postID) FROM Post;
        """)

        for row in cursor:
            cursor.execute("""
                INSERT INTO Response(responseID, parentPostID)
                VALUES ({responseID}, {parentPostID})
            """.format(responseID=row[0], parentPostID=postID))
            db.commit()
        self.closeDBConn(db)

        print "{personID} responded to post {topicID}!".format(personID=personID, topicID=topicID)

    def createGroup(self, groupName):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO FriendGroup(groupName)
            VALUES ("{groupName}")
        """.format(groupName=groupName))
        db.commit()
        self.closeDBConn(db)

        print "Friend group {groupName} was created!".format(groupName=groupName)

    def joinGroup(self, groupID, personID):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO GroupMember(groupID, personID)
            VALUES ({groupID}, {personID})
        """.format(groupID=groupID, personID=personID))
        db.commit()
        self.closeDBConn(db)

        print "{personID} was addded to {groupID}!".format(personID=personID, groupID=groupID)

    def followTopic(self, personID, topicID):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO FollowedTopic(personID, topicID)
            VALUES ({personID}, {topicID})
        """.format(personID=personID, topicID=topicID))
        db.commit()
        self.closeDBConn(db)

        print "{personID} started following {topicID}!".format(personID=personID, topicID=topicID)

    def getReactTypes(self):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            SELECT * FROM ReactType
        """)

        for row in cursor:
            print row

        self.closeDBConn(db)

    def getPersons(self):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            SELECT personID FROM Person
        """)

        persons = [row[0] for row in cursor]
        self.closeDBConn(db)
        return persons

    def getRelatedPosts(self, personID):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            SELECT 
                Po.postID,
                T.topic,
                CONCAT_WS(" ", Pe.firstName, Pe.lastName),
                Po.body
            FROM (SELECT *
            FROM Post
            WHERE
                topicID IN (SELECT topicID FROM FollowedTopic WHERE personID = {})
                OR personID IN (
                    SELECT personOne as personID from Friend WHERE personTwo = {} 
                    UNION ALL
                    SELECT personTwo as personID from Friend WHERE personOne = {})) AS Po
            LEFT JOIN Person as Pe ON Pe.personID = Po.personID
            LEFT JOIN Topic as T ON T.topicID = Po.topicID
        """.format(personID, personID, personID))

        for row in cursor:
            print "Post #: " + str(row[0])
            print "Topic: " + row[1]
            print "User: " + row[2]
            print row[3] + '\n\n'

        self.closeDBConn(db)

    def getTopics(self):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            SELECT * FROM Topic
        """)

        for row in cursor:
            print "{topicID} - {topic}".format(topicID=row[0], topic=row[1])

        self.closeDBConn(db)

    def getPostTopic(self, postID):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            SELECT topicID FROM Post
            WHERE postID = {}
        """.format(postID))
        for row in cursor:
            topicID = row[0]

        self.closeDBConn(db)
        
        return topicID

    def getGroups(self):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            SELECT * FROM FriendGroup
        """)

        for row in cursor:
            print "{groupID} - {groupName}".format(groupID=row[0], groupName=row[1])

        self.closeDBConn(db)

    def getPotentialFriends(self, personID):
        db = self.createDBConn()
        cursor = db.cursor()

        cursor.execute("""
            SELECT
                personID,
                CONCAT_WS(" ", firstName, lastName)
            FROM Person
            WHERE personID NOT IN (
                SELECT personOne as personID from Friend WHERE personTwo = {} 
                UNION ALL
                SELECT personTwo as personID from Friend WHERE personOne = {})
                AND personID <> {}
        """.format(personID, personID, personID))

        for row in cursor:
            print "{groupID} - {groupName}".format(groupID=row[0], groupName=row[1])

        self.closeDBConn(db)