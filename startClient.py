from Client import Client 

def login(client):
    while True:
        print 'WELCOME TO SOCIAL MEDIA'
        
        # LOGIN/CREATE USER
        print "===== To create user            [0]"
        print "===== To login to existing user [1]"
        action = raw_input()

        if action == "0":
            firstName = raw_input("Enter first name: ")
            lastName = raw_input("Enter last name: ")
            middleNames = raw_input("Enter middle name(s): ") 
            birthday = raw_input("Enter birthday [YYYY-MM-DD]: ")
            sex = raw_input("Enter sex [M/F]:")
            age = int(raw_input("Enter age: "))
            city = raw_input("Enter home city: ")
            country = raw_input("Enter home country: ")
            job = raw_input("Enter job: ")
            
            currentUser = client.createUser(lastName, firstName, middleNames, birthday, sex, age, city, country, job)
            return currentUser

        elif action == "1":
            print "Enter user id:"
            currentUser = int(raw_input())
            if currentUser not in client.getPersons():
                print "User does not exist"
                continue
            print "Selected user {personID}".format(personID=currentUser)
            return currentUser

        else:
            print "Please enter correct input [0/1]."
            continue

def main(client, currentUser):
    while True:
        print "===== View new posts         [0]"
        print "===== View all posts         [1]"
        print "===== Respond to post        [2]"
        print "===== React to post          [3]"
        print "===== Create topic           [4]"
        print "===== Create subtopic        [5]"
        print "===== Create friend group    [6]"
        print "===== Join friend group      [7]"
        print "===== Create post            [8]"
        print "===== Add friend             [9]"
        print "===== Follow topic/subtopic  [10]"
        print "===== Exit                   [11]"
        action = raw_input()

        # ACTIONS
        if action == "0":
            client.getUnreadRelatedPosts(currentUser)
        elif action == "1":
            client.getRelatedPosts(currentUser)
        elif action == "2":
            postID = raw_input("What is the post # you are responding to? \n")
            topicID = client.getPostTopic(postID)
            body = raw_input("What is your response? \n")
            client.respondToPost(currentUser, postID, topicID, body)
        elif action == "3":
            client.getReactTypes()
            postID = raw_input("What post would you like to react to? \n")
            reactTypeID = raw_input("What reaction would you like to use? \n")
            client.reactToPost(postID, currentUser, reactTypeID)
        elif action == "4":
            topic = raw_input("What is the topic? \n")
            client.createTopic(topic)
        elif action == "5":
            client.getTopics()
            parentTopic = raw_input("What is the parent topic? \n")
            subtopic = raw_input("What is the subtopic? \n")
            client.createSubtopic(subtopic, parentTopic)
        elif action == "6":
            groupName = raw_input("What is the group name? \n")
            client.createGroup(groupName)
        elif action == "7":
            client.getGroups()
            groupID = raw_input("What is the group #? \n")
            client.joinGroup(groupID, currentUser)
        elif action == "8":
            client.getTopics()
            topicID = raw_input("What is the topic id? \n")
            body = raw_input("What is the post? \n")
            client.createPost(currentUser, topicID, body)
        elif action == "9":
            client.getPotentialFriends(currentUser)
            personID = raw_input("What is the person ID? \n")
            client.addFriend(currentUser, personID)
        elif action == "10":
            client.getTopics()
            topicID = raw_input("What is the topic do you want to follow? \n")
            client.followTopic(currentUser, topicID)
        elif action == "11":
            break
        else:
            print "Please enter an appropriate input."
            continue

client = Client()
currentUser = login(client)
main(client, currentUser)