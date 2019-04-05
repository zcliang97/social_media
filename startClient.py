from Client import Client 

client = Client()
currentUser = None

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
    elif action == "1":
        print "Enter user id:"
        currentUser = int(raw_input())
        if currentUser not in client.getPersons():
            print "User does not exist"
            continue
        print "Selected user {personID}".format(personID=currentUser)
    else:
        print "Please enter correct input [0/1]."
        continue

    print "===== View new posts         [0]"
    print "===== Respond to post        [1]"
    print "===== Create topic           [2]"
    print "===== Create subtopic        [3]"
    print "===== Create friend group    [4]"
    print "===== Join friend group      [5]"
    print "===== Create post            [6]"
    print "===== Add friend             [7]"
    print "===== Follow topic/subtopic  [8]"
    action = raw_input()

    # ACTIONS
    if action == "0":
        client.getPosts()
    elif action == "1":
        client.respondToPost()
    elif action == "2":
        client.createTopic()
    elif action == "3":
        client.createSubtopic()
    elif action == "4":
        client.createGroup()
    elif action == "5":
        client.joinGroup()
    elif action == "6":
        client.createPost()
    elif action == "7":
        client.addFriend()
    elif action == "8":
        client.followTopic()
    
    # client.getReactTypes()
    # client.createUser("Saget", "Bob", None, "1997-06-04", None, None, None, None, None)
    # client.createUser("Liang", "Frank", "", "1997-06-04", "M", 21, "Waterloo", "Canada", "Student")
    # client.createUser("Ko", "Young", "Test", "1997-01-20", "M", 21, "Waterloo", "Canada", "Student")
    # client.createUser("Li", "Michael", "", "1997-11-21", "M", 22, "Waterloo", "Canada", "Student")

    # client.createTopic("Art", None)
    # client.createTopic("Hockey", 1)
    # client.createTopic("Paintings", 3)
    # client.createTopic("Disasters", 2)
    # client.createTopic("Basketball", 1)

    # client.addFriend(6, 7)
    # client.addFriend(8, 7)

    # client.createPost(6, 5, "Does anyone know when the upcoming hockey game is?")
    # client.createPost(7, 5, "I believe the game is on April 1st, 2019. You can find out on the website.")

    # client.createGroup("Waterloo")
    # client.addToGroup(1, 6)
    # client.addToGroup(1, 7)

    # client.followTopic(6, 1)
    # client.followTopic(6, 3)
    # client.followTopic(7, 3)
    # client.followTopic(8, 5)
    # client.followTopic(8, 6)

    break