#a tool to collect survey style true/false statements from the customers and collect their responses in a database

'James is a konami fanboy bitch'

#library imports
from tkinter import *
import sqlite3

#global variables for the interface
user = 'null'
chassis = 'null'
verbatim = 'null'

#global variables for the survey
activation = False
selecting = False
clear_info = False
detection = False
watch_video = False


#functions that makes the buttons toggle their value and text for each question
def toggle_acti():
    global activation
    global acti_button
    if acti_button.config('text')[-1] == 'No':
        acti_button.config(text = 'Yes')
        activation = True
    else:
        acti_button.config(text = 'No')
        activation = False

def toggle_sele():
    global selecting
    global sele_button
    if sele_button.config('text')[-1] == 'No':
        sele_button.config(text = 'Yes')
        selecting = True
    else:
        sele_button.config(text = 'No')
        selecting = False

def toggle_clea():
    global clear_info
    global clea_button
    if clea_button.config('text')[-1] == 'No':
        clea_button.config(text = 'Yes')
        clear_info = True
    else:
        clea_button.config(text = 'No')
        clear_info = False

def toggle_dete():
    global detection
    global dete_button
    if dete_button.config('text')[-1] == 'No':
        dete_button.config(text = 'Yes')
        detection = True
    else:
        dete_button.config(text = 'No')
        detection = False

def toggle_watc():
    global watch_video
    global watc_button
    if watc_button.config('text')[-1] == 'No':
        watc_button.config(text = 'Yes')
        watch_video = True
    else:
        watc_button.config(text = 'No')
        watch_video = False

#debugging function prints the values to the python interpreter to verify that the outputs look correct
def debug():
    retrieve_inputs()
    print('user:',user)
    print('chassis:',chassis)
    print('verbatim:',verbatim)
    print('activation:',activation)
    print('selecting:',selecting)
    print('clear_info:',clear_info)
    print('detection:',detection)
    print('watch_video:',watch_video)
    reset()

#a function for a text entry field to collect strings from entry fields that commits them to variables
def retrieve_inputs():
    global user
    global chassis
    global verbatim
    user = input = Q_num.get()
    chassis = input = chas_field.get()
    verbatim = input = ver_entry.get()
#a function for a button that submits the feedback by committing the values of the variables into SQL and inserting that to a table
def write_to_database():
    global user
    global chassis
    global verbatim
    global activation
    global selecting
    global clear_info
    global detection
    global watch_video
    connection = sqlite3.connect('P:\Customer_Care\IQS and Genius\Genius\Special Projects\Trouser Reports\database\survey_data.db')
    crsr = connection.cursor()
    crsr.execute('INSERT INTO parking_assistant_survey VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (user, chassis, verbatim, activation, selecting, clear_info, detection, watch_video))
    connection.commit()
    connection.close()

#a function called by the Submit function that clears the data and resets the form apart from the Q number submitting the data, this function is also called with an interface button as a reset button that does not submit the data
def reset():
    global chassis
    global activation
    global selecting
    global clear_info
    global detection
    global watch_video
    global verbatim
    global ver_entry
    global chas_field
    chassis = 'nullR'
    verbatim = 'nullR'
    acti_button.config(text = 'No')
    activation = False
    sele_button.config(text = 'No')
    selecting = False
    clea_button.config(text = 'No')
    clear_info = False
    dete_button.config(text = 'No')
    detection = False
    watc_button.config(text = 'No')
    watch_video = False
    ver_entry.delete(0,END)
    chas_field.delete(0, END)
    #debugging elements
    '''print(chassis)
    print(activation)
    print(verbatim)'''

#a function for the submit button that commits all the collected data to the database and then resets the tool for the next survey entry
def submit_survey():
    retrieve_inputs()
    write_to_database()
    reset()

#interface so that agents can easily use it
# establishes window
main = Tk()
main.geometry('500x310')
main.title('Parking Assistant Survey')
#identity entry fields
Q_num = Entry(main)
Q_num.grid(row=0, column=1)
chas_field = Entry(main)
chas_field.grid(row=1, column=1)
#survey question buttons
acti_button = Button(main, text = 'No', width = 20, height = 2, command = toggle_acti)
acti_button.grid(row=2, column = 1)
sele_button = Button(main, text = 'No', width = 20, height = 2, command = toggle_sele)
sele_button.grid(row=3, column = 1)
clea_button = Button(main, text = 'No', width = 20, height = 2, command = toggle_clea)
clea_button.grid(row=4, column = 1)
dete_button = Button(main, text = 'No', width = 20, height = 2, command = toggle_dete)
dete_button.grid(row=5, column = 1)
watc_button = Button(main, text = 'No', width = 20, height = 2, command = toggle_watc)
watc_button.grid(row=6, column = 1)
ver_entry = Entry(main)
ver_entry.grid(row=7, column= 1)
#labels for the interface elements
lab_Qnum = Label(main, text = 'Q Number')
lab_Qnum.grid(row=0,column = 2)
lab_chas = Label(main, text = 'Chassis')
lab_chas.grid(row=1, column=2)
lab_acti = Label(main, text = 'Do you have an issue in activating the parking assistant?')
lab_acti.grid(row=2, column=2)
lab_sele = Label(main, text='Do you have an issue in selecting the proposed parking spaces?')
lab_sele.grid(row=3, column=2)
lab_clea = Label(main, text='Is the parking space information in the central information\n display understandable?')
lab_clea.grid(row=4, column=2)
lab_dete = Label(main, text='Is the detection of free parking spaces understandable?')
lab_dete.grid(row=5, column=2)
lab_watc = Label(main, text ='Did you already watch the How-To-Video?')
lab_watc.grid(row=6, column=2)
lab_verE = Label(main, text='**Copy and paste call notes**')
lab_verE.grid(row=7, column=2)
#reset and submit buttons
reset_button = Button(main, text='Reset\nDiscard Data', command = reset)
reset_button.grid(row=8, column=1)
submit_button = Button(main, text='Submit To\nDatabase', command = submit_survey)
submit_button.grid(row=8, column=2)

#mainloop function to stop the program "crashing"/ending on open
main.mainloop()
