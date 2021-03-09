#adam locke, 2020 July
#SQL query tool, runs SQL queries against a copy of a survey database to allow Genius team members to expand their skillsets.

#import statements
import sqlite3
import time
import csv
from tkinter import *

#global variables
targetdb = ''
entry = ''
results = ''


#sql execute function
def sqlexecute():
    global targetdb
    global entry
    global entry_field
    start = time.time()
    connection = sqlite3.connect(targetdb)
    crsr = connection.cursor()
    entry = entry_field
    command = entry
    crsr.execute(command)
    results = crsr.fetchall()
    connection.commit()
    connection.close()
    finish = time.time()
    duration = finish-start
    print('The quesry took', duration,'seconds to complete.\n\n')
    for entries in results:
        print(entries)

#query results export function

#clear entry function
def clearentry():
    global entry
    entry = ''
    entry_field.delete(0, END)

#save query function
#def savequery():
    

#open saved query function


#||||||||interface
main = Tk()
#main.geomtery('800x600')
main.title('Trouser Report SQL Tool')

#text entry field
reminder_lab = Label(main, text = 'Reminder: all queries must target the \'parking_assistant_survey\ table.')
entry_lab = Label(main, anchor='center', text = 'Query Text')
entry_lab.grid(row=2,column = 0)
entry_field = Text(main, width=180, height=30)
entry_field.grid(row=3, column=0)
clear_but = Button(main, text='Clear Entry Field', command= clearentry())
clear_but.grid(row=2, column= 2)
    

#--------hidden functions----------
#switch database target function
'this function should not be used by the inexperienced user, this can switch the tool to make edits in a live database'
def targetswitch():
    global targetdb
    print('Warning!  Only switch the database target if you have permission to use the database in question.')
    targetdb = (input('Enter the precise file path of the new target database:'))
    input('The target database has been chahnged, note that the quesries will fail if the entered file path is invalid.')

main.mainloop
