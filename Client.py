# python -m pip install mysql-connector-python
import mysql.connector

class Client:
    def __init__(self):
        self.host="localhost"
        self.user="root"            #enter username
        self.passwd=""              #enter password
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

        print "{personOneID} and {personTwoID} are now friends!".format(personOne=personOneID, personTwo=personTwoID)

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

    def addToGroup(self, groupID, personID):
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