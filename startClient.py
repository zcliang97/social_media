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
        print "===== Respond to post        [1]"
        print "===== Create topic           [2]"
        print "===== Create subtopic        [3]"
        print "===== Create friend group    [4]"
        print "===== Join friend group      [5]"
        print "===== Create post            [6]"
        print "===== Add friend             [7]"
        print "===== Follow topic/subtopic  [8]"
        print "===== Exit                   [9]"
        action = raw_input()

        # ACTIONS
        if action == "0":
            client.getRelatedPosts(currentUser)
        elif action == "1":
            postID = raw_input("What is the post # you are responding to? \n")
            topicID = client.getPostTopic(postID)
            body = raw_input("What is your response? \n")
            client.respondToPost(currentUser, postID, topicID, body)
        elif action == "2":
            topic = raw_input("What is the topic? \n")
            client.createTopic(topic)
        elif action == "3":
            client.getTopics()
            parentTopic = raw_input("What is the parent topic? \n")
            subtopic = raw_input("What is the subtopic? \n")
            client.createSubtopic(subtopic, parentTopic)
        elif action == "4":
            groupName = raw_input("What is the group name? \n")
            client.createGroup(groupName)
        elif action == "5":
            client.getGroups()
            groupID = raw_input("What is the group #? \n")
            client.joinGroup(groupID, currentUser)
        elif action == "6":
            client.getTopics()
            topicID = raw_input("What is the topic id? \n")
            body = raw_input("What is the post? \n")
            client.createPost(currentUser, topicID, body)
        elif action == "7":
            client.getPotentialFriends(currentUser)
            personID = raw_input("What is the person ID? ")
            client.addFriend(currentUser, personID)
        elif action == "8":
            client.getTopics()
            topicID = raw_input("What is the topic do you want to follow? ")
            client.followTopic(currentUser, topicID)
        elif action == "9":
            break
        else:
            print "Please enter an appropriate input."
            continue

client = Client()
currentUser = login(client)
main(client, currentUser)