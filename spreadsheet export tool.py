#import statements
import sqlite3
from tkinter import *
import csv


#global variables
data_list = []
data_holder = []

#code to access the database and pull the information ito a variable for use

connection = sqlite3.connect('P:\Customer_Care\IQS and Genius\Genius\Special Projects\Trouser Reports\database\survey_data.db')
crsr = connection.cursor()

def pull_all_data():
    global data_list
    crsr.execute('SELECT * FROM parking_assistant_survey')
    results = crsr.fetchall()
    for lines in results:
        data_list.append(lines)
    for lines in data_list:
        data_holder.append(lines)

def csv_convert(list_var):
    global data_holder
    try:
        result = open('parking assistant survey.csv', mode = 'w', newline='')
        olorin = csv.writer(result)
        for lines in data_holder:
            olorin.writerow(lines)
        result.close()
    except FileNotFoundError:
            print('The CSV file is not in the proper directory\nPlease put the file \'parking assistant survey data.csv\' into the directory folder and try again.')
        
        


def test_print():
    print(data_list)

pull_all_data()
test_print()

#code that closes the connection when the data has been pulled
connection.commit()
connection.close()


#code to write information from the variable into a CSV

#interface so that bosses can easily use it
# establishes window
main = Tk()
main.geometry('500x310')
main.title('Parking Assistant Survey Spreadsheet Tool')
#identity entry fields
#survey question buttons
CSV_button = Button(main, text = 'Export', width = 20, height = 2, command = csv_convert(data_holder))
CSV_button.grid(row=1, column = 1)
'''sele_button = Button(main, text = 'No', width = 20, height = 2, command = toggle_sele)
sele_button.grid(row=3, column = 1)
clea_button = Button(main, text = 'No', width = 20, height = 2, command = toggle_clea)
clea_button.grid(row=4, column = 1)
dete_button = Button(main, text = 'No', width = 20, height = 2, command = toggle_dete)
dete_button.grid(row=5, column = 1)
watc_button = Button(main, text = 'No', width = 20, height = 2, command = toggle_watc)
watc_button.grid(row=6, column = 1)
ver_entry = Entry(main)
ver_entry.grid(row=7, column= 1)'''
#labels for the interface elements
lab_Qnum = Label(main, text = 'CSV format')
lab_Qnum.grid(row=1,column = 2)
'''lab_chas = Label(main, text = 'Export survey data as CSV')
lab_chas.grid(row=1, column=2)
lab_acti = Label(main, text = 'Export as CSV')
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
lab_verE.grid(row=7, column=2)'''
#reset and submit buttons
'''reset_button = Button(main, text='Reset\nDiscard Data', command = reset)
reset_button.grid(row=8, column=1)
submit_button = Button(main, text='Submit To\nDatabase', command = submit_survey)
submit_button.grid(row=8, column=2)'''
main.mainloop()
