# coding=utf-8
# -*- coding: utf-8 -*-
"""
JT Budget
Aims to convert raw data provided by an internet bank
into a csv format that allows for easy analysis
Initial iteration created on 9th September
Updated on 6th June
Coded by Jack Trainor
"""
# Time the process
import time
# Various data handling functions
import numpy as np
# .csv data file manipulation
import pandas as pd
# File path management
from os.path import exists

# ASCII terminal art because I can
time.sleep(1)
print("")
time.sleep(0.4)
print("    /$$$$$ /$$$$$$$$       /$$$$$$$                  /$$                       /$$")
time.sleep(0.4)
print("   |__  $$|__  $$__/      | $$__  $$                | $$                      | $$")
time.sleep(0.4)
print("      | $$   | $$         | $$  \ $$ /$$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$")
time.sleep(0.4)
print("      | $$   | $$         | $$$$$$$ | $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/")
time.sleep(0.4)
print(" /$$  | $$   | $$         | $$__  $$| $$  | $$| $$  | $$| $$  \ $$| $$$$$$$$  | $$")
time.sleep(0.4)
print("| $$  | $$   | $$         | $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$_____/  | $$ /$$")
time.sleep(0.4)
print("|  $$$$$$/   | $$         | $$$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$  |  $$$$/")
time.sleep(0.4)
print(" \______/    |__/         |_______/  \______/  \_______/ \____  $$ \_______/   \___/")
time.sleep(0.4)
print("                                                         /$$  \ $$")
time.sleep(0.4)
print("                                                        |  $$$$$$ /")
time.sleep(0.4)
print("                                                         \_______/")
time.sleep(0.4)
print("")
time.sleep(2)


file_present = exists('Input.csv')
if file_present == True:
    input_name = 'Input.csv'
else:
    print('Enter the name of your input csv file:')
    print('e.g. Input')
    input_name = str(input('')) + '.csv'
    file_present = exists(input_name)
    if file_present == False:
        time.sleep(0.5)
        print("-------------------------------------")
        print("                ERROR")
        print(input_name,"not found in directory")
        print("-------------------------------------")
        time.sleep(0.5)
        exit()

# Read in data from a specified csv file
# using Pandas to create relevant string and real arrays
df = pd.read_csv(input_name)
input_array = df.to_numpy(na_value='0.0')
# Ensure not reading blank rows
maxsize = int(len(input_array))
n_el = 0
for i in range(0,maxsize):
    if (input_array[i,0] != '0.0'):
        n_el = n_el + 1

# For Debugging
# print(n_el)
# print(input_array[:,0])
# print(input_array[:,1])
# print(input_array[:,2])
# print(input_array[:,3])
# print(input_array[:,4])
# print(input_array[:,5])

# Input Array Description:
# 0 - Date
# 1 - Type
# 2 - Description
# 3 - Outgoing Amount
# 4 - Incoming Amount
# 5 - Total

# Loop through the provided data
# Descriptions
category_list1 = np.arange(n_el, dtype=object)
# ID of Category
category_list2 = np.arange(n_el, dtype=int)
# Monetary Value
category_list3 = np.arange(n_el, dtype=float)
# Dates
category_date = np.arange(n_el, dtype=object)
category_list4 = np.arange(n_el, dtype=object)

# Loop over each entry i
for i in range(n_el):
    category_list1[i] = str(input_array[i, 2])
    category_date[i] = str(input_array[i, 0])
    temp_string = str(input_array[i, 0])
    category_list4[i] = temp_string[3:-3]
    prev_type = 0
    for j in range(i):
        # Check if the current purchase type has been categorised
        if category_list1[j] == category_list1[i]:
            category_list2[i] = category_list2[j]
            prev_type = 1
            break
    # Program has not seen this description before
    if prev_type == 0:
        # Allow the user to set any new
        # purchase type into a pre-defined category
        print('Categorise the following:')
        print(str(category_list1[i]),' - ',category_date[i])
        print('1)Social  2)Food  3)Personal 4)Activities 5)Travel 6)Bills 7)Savings 8)Holidays 9)Work/Expenses 0)Misc/Unknown')
        category_input = input('')
        while len(category_input) != 1:
            print("Please enter an integer:")
            category_input = input('')
        category_list2[i] = int(category_input)

    temp_string = input_array[i, 3]
    if (category_list3[i] != '0.0'):
        category_list3[i] = float(temp_string.replace('£', ''))

# Sort the data into relevant categories
# Array of floats for each month
month_count = 0
month_str = ''
month_list = ['']
for i in range(n_el):
    if category_list4[i] != month_str:
        month_count = month_count + 1
        month_str = category_list4[i]
        month_list.append(month_str)
month_list.remove('')

# For Debugging
# print(month_list)
# print(category_list1)
# print(category_list2)
# print(category_list3)
# print(category_list4)

# Generate arrays for the totals
Social_tot = np.arange(month_count, dtype=float)
Food_tot = np.arange(month_count, dtype=float)
Personal_tot = np.arange(month_count, dtype=float)
Activities_tot = np.arange(month_count, dtype=float)
Travel_tot = np.arange(month_count, dtype=float)
Bills_tot = np.arange(month_count, dtype=float)
Savings_tot = np.arange(month_count, dtype=float)
Holidays_tot = np.arange(month_count, dtype=float)
Work_tot = np.arange(month_count, dtype=float)
Misc_tot = np.arange(month_count, dtype=float)

time.sleep(1)
print('Generating csv file...')
time.sleep(1)

# Loop through the lists
for i in range(month_count):
    Social_tot[i] = 0.0
    Food_tot[i] = 0.0
    Personal_tot[i] = 0.0
    Activities_tot[i] = 0.0
    Travel_tot[i] = 0.0
    Bills_tot[i] = 0.0
    Savings_tot[i] = 0.0
    Holidays_tot[i] = 0.0
    Food_tot[i] = 0.0
    Work_tot[i] = 0.0
    Misc_tot[i] = 0.0
for i in range(n_el):
    for j in range(month_count):
        if category_list4[i] == month_list[j]:
            jj = j
    if category_list2[i] == 1:
        Social_tot[jj] = Social_tot[jj] + category_list3[i]
    elif category_list2[i] == 2:
        Food_tot[jj] = Food_tot[jj] + category_list3[i]
    elif category_list2[i] == 3:
        Personal_tot[jj] = Personal_tot[jj] + category_list3[i]
    elif category_list2[i] == 4:
        Activities_tot[jj] = Activities_tot[jj] + category_list3[i]
    elif category_list2[i] == 5:
        Travel_tot[jj] = Travel_tot[jj] + category_list3[i]
    elif category_list2[i] == 6:
        Bills_tot[jj] = Bills_tot[jj] + category_list3[i]
    elif category_list2[i] == 7:
        Savings_tot[jj] = Savings_tot[jj] + category_list3[i]
    elif category_list2[i] == 8:
        Holidays_tot[jj] = Holidays_tot[jj] + category_list3[i]
    elif category_list2[i] == 9:
        Work_tot[jj] = Work_tot[jj] + category_list3[i]
    elif category_list2[i] == 0:
        Misc_tot[jj] = Misc_tot[jj] + category_list3[i]

# Output data to desired csv file
print('Enter the name of your output csv file:')
print('e.g. Output')
output_name = str(input('')) + '.csv'
file_present = exists(output_name)

while file_present == True:
    time.sleep(0.2)
    print("Warning - ",output_name," is already in current directory")
    time.sleep(0.2)
    print("Overwrite File? Y/N")
    YN = str(input(''))
    if (YN == 'Y') or (YN == 'y'):
        time.sleep(0.2)
        break
    elif (YN == 'N') or (YN == 'n'):
        time.sleep(0.2)
        print('Enter the name of your output csv file:')
        print('e.g. Output')
        output_name = str(input('')) + '.csv'
        file_present = exists(output_name)
    else:
        time.sleep(0.2)
        print("Please enter Y or N")


# Output the sorted data into a csv file using pandas
# to sort each and give required formatting
df2 = pd.DataFrame({
    'Months': month_list,
    'Social': Social_tot,
    'Food': Food_tot,
    'Personal': Personal_tot,
    'Activities': Activities_tot,
    'Travel': Travel_tot,
    'Bills': Bills_tot,
    'Savings': Savings_tot,
    'Holidays': Holidays_tot,
    'Work/Expenses': Work_tot,
    'Misc/Unknown': Misc_tot})
df2.to_csv(output_name)

# Closing Code print statements. Allows the code
# To be read if ran in a terminal before it is closed
print('...csv File Generated Successfully')
time.sleep(1)
print('Enter any key to exit the code:')
input_str = str(input(''))
if input_str == 'any key':
    print('haha funny')
    time.sleep(2)
    print('Exiting...')
    time.sleep(2)
    exit()
elif input_str == '69':
    print('nice')
    time.sleep(2)
    print('Exiting...')
    time.sleep(2)
    exit()
else:
    print('Exiting...')
    time.sleep(2)
    exit()
