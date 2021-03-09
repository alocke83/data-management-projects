import sqlite3

#global variables for the variable injection test
user = 'tester'
chassis = 'fiddycar'
verbatim = 'tika tika slim shady'
activating = 1
selecting = 1
clear_info = 1
detection = 1
watch_video = 1

connection = sqlite3.connect('P:\Customer_Care\IQS and Genius\Genius\Special Projects\Trouser Reports\database\survey_data.db')
crsr = connection.cursor()

def populate_fields():
    command = 'CREATE TABLE parking_assistant_survey (user VARCHAR(10), chassis VARCHAR(7), verbatim VARCHAR(8000), activation BIT(1), selecting BIT(1), clear_info BIT(1), detection BIT(1), watch_video BIT(1))'
    crsr.execute(command)

#uncomment this line to create a table with the fields described
#populate_fields()

def test_data():
    command = 'INSERT INTO parking_assistant_survey VALUES ("adam", "toolongcar", "some feedback that can be 8000 characters long", "0", "0", "0", "0", "0")'
    crsr.execute(command)

#uncomment this line to add a test record to the table
#test_data()

def variable_data_test():
    global user
    global chassis
    global verbatim
    global activating
    global selecting
    global clear_info
    global detection
    global watch_video
    crsr.execute('INSERT INTO parking_assistant_survey VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (user, chassis, verbatim, activating, selecting, clear_info, detection, watch_video))

#uncomment this line to add a test record reliant upon global variables
#variable_data_test()

def pull_all_data():
    crsr.execute('SELECT * FROM parking_assistant_survey')
    results = crsr.fetchall()
    for i in results:
        print(i)

#uncomment this line to pull all data from the parking assistant survey
pull_all_data()

#this function is not complete
#this function is designed to take everything in the database and store it to a variable with comma delimiting, it is the first step in creating digestible output.
'''def extract_data():
    for row in crsr:
        comma_data = ','.join(row)'''
    

connection.commit()
connection.close()
