Social Media Project
====================

To run the code, make sure Python 2.7 is installed.

1. Install python package mysql-connector-python
python -m pip install mysql-connector-python

2. Open the Client.py file and enter database connection details in the __init__ function.
We used the following parameters but please update to your database.
    self.host="localhost"
    self.user="root"            # enter username
    self.passwd="#######"       # enter password
    self.db="Project"

3. To use the sample data we created, run the insert script on your database.
File is: insertSampleData.sql

4. Run the python script to start the client.
python startClient.py

5. Two options when running the client: create or login as an user.

6. Once logged in, can start using the social media platform with the given instructions in the program.