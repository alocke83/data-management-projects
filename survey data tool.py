# a program to submit data to the databases I make for special reporting projects.

#import statements
import sqlite3
from tkinter import *

#global variables needed for the tool to operate

'crsr = connection.cursor()'
connection = 'null'
pull_script = 'null'
data = 'null'
#when data is imported the type of the data variable will change from string to list

#a fucntion to choose which database is targeted
'by using a function to choose specific surveys it becomes possible to expand the tool utility as more survey tools are made, it is modular'
def choose_parking_assistant_survey():
    global connection
    global pull_script
    #THE SCRIPT WILL NOT WORK WHILE THIS IS STILL A COMMENT
    #The user should supply the absolute address of the data base in question
    connection = sqlite3.connect('INSERT DATABASE ABSOLUTE ADDRESS')
    pull_script = ('SELECT * FROM parking_assistant_survey')

#a function to pull all the data into a variable
def pull_all_data_to_variable():
    global connection
    global pull_script
    global data
    connection = connection
    crsr = connection.cursor()
    crsr.execute(pull_script)
    results = crsr.fetchall()
    data = results
    connection.commit()
    connection.close()
    
#a function to slice the data from the string in the data variable into individual lists of data points for population to a spreadsheet

#a function that uses a library compatible with excel 2013 to use the lists I split out to populate a spreadsheet

#a test function to print the variable to the terminal for debugging
def test_pull_to_variable():
    'this function simply confirms that the data is being successfully imported into a variable for manipulation'
    global data
    print (data)
#a test function to slice the string into copy-paste compatible elements for excel manual entry
def excel_slice():
    'This function has no practical use as the data variable becomes a list after the database is pulled, converting it back to string does not seem helpful in exporting to excel by copy paste from the terminal'
    global data
    data = str(data)
    print(' ',data.replace('(', '')
    .replace('), ', '\n')
          #.replace(',', '   ')
          .replace('\'','')
          )
#a test function to export the data to a spreadsheet file
'I know this is a for loop of some kind, but I need it to use the data in my list by putting each entry separated by () into a separate row, and each item within each () into its own column'
def list_printing():
    global data
    for entry in data:
        print(entry)
    

#mainline
'code segments that are commented out are debugging functions'
choose_parking_assistant_survey()
pull_all_data_to_variable()
#excel_slice()
#test_pull_to_variable()
list_printing()




#an interface so that bosses can easily use it
'''
main = Tk()
main.geometry('600x400')
main.title('Trouser Reports Data Tool')
'''
#a dropdown selection to choose which report database is used

#a button to export as excel

#a button to export as PDF

#a text output field that reports the file location of the exported file in case the user cannot find it
