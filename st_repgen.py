#FIXME same index to some names error
#TODO add students Grade (Class)

#Import Moduls and Libreries
from unicodedata import name
from win32api import GetSystemMetrics
import os
import time
from time import sleep
from tqdm import tqdm
from prettytable import PrettyTable
from pyfiglet import figlet_format
from termcolor import colored
from random import randint
import random

#tool name
text = "strepgen 1 . 0"

# This colors will apllied on your text1
colors = ['red', 'green', 'yellow', 'blue', 'cyan', 'white' ,'magenta']

#select random color
random.shuffle(colors)
random_color = randint(0,6)

# message what you want print using ASCII
ascii_text = figlet_format(text, font="slant")

# Message in colorized
colored_ascii = colored(ascii_text, color = colors[random_color])
tool = colored_ascii[5:]
tool_name = tool[:-5]
# Result
print(tool_name)
time.sleep(2)
print("\n")

#Tool About
screen_Width = GetSystemMetrics(0)
#print(screen_Width)
safe_area = screen_Width - 10
#print(safe_area)
line = int(safe_area/2)
#print(line)
print("*" * int(line/6))
print("2021 Copyright (C) Dev - Darshana Wishwajith. All rights reserved.")
print("\n")
time.sleep(0.25)
print("-->> Instructions for use this tool")
print("\n")
print("""-----\"Student Report Generator\"-----\n\n\t# This tool  made for  get students' marks report automatically can analize comma seperated values file.\n\t# you must format your data  to csv file like example csv file.\n\t# you can find it in tool's  directory.\n\t# Then you can input data file path to system.\n\t# Then this tool can analize your data and generate report for one student or all students in class.\n\t# if you want to write reports to text files you can do it via this tool.\n\t# So there we go""")
print("\n")
time.sleep(1)

while True:  
    #Input Data file path 
    print("You can input your data (csv) file path like below examples ;\n")
    print("\t1st method - C:\Program Files\Python\Student Report Generator\data.txt\n\t2nd method - data.txt (default path)\n\t3nd method - d")
    print("\t\td = data.txt (default path)\n")
    sucess = False


    path = input("Enter your Data File path : ")
    if path == "d":
        path = "data.txt"

    #Open Data file and validate it
    lines = None
    #this loop for data file validation
    while True:
        try:
            with open(path, 'r') as file:
                lines = file.readlines()
                sucess = True
        except:
            print("\n")
            print(f"{path}, is not a Valid path.\n\nPlease Enter a valid Data file path : ", end = "")
            path = input()
            if path == "d":
                path = "data.txt"
        if sucess == True:
            break

    #check CSV file lines are empty or no
    c = True
    error = bool
    while c == True :
        csv = lines[2:]
        for i , line in enumerate(csv) :
            if len(line) < 5:
                print("\n")
                print(f"** Attention Here!!! -->> line {i+1} in Data(CSV) file is empty or invalid format.\n\tPlease check your Data (CSV) file and try again!\n")
                print("\n")
                error = True
            else:
                c = False
    if error == True :
        continue
    
    #this loop for check data file is not empty
    while True:
        file_size = os.path.getsize(path)
        if file_size == 0:
            print(f"{path} , Data file is empty!\n \t Please enter a valid Data File path")
            path = input("Enter your Data File path : ")
            if path == "d":
                path = "data.txt"
        else:
            print("\n")
            time.sleep(1)
            print("-->> Access to Data File Successfully!")
            break
        
    #Scling Processable data from Data File
    data = lines[2:]
    #print(data)
    print("\n")
    time.sleep(2)
    print("-->> Data Slicing Completed!")
    print("\n")

    #Defining Dictionaries
    divide_by_subject = {}
    divide_by_student = {}
    indexing = {}
    
    #This funtion  for progress counter
    def progress_counter() -> str :
        for i in range(0,101) :
            print("\r", i,"%", end = "")
            time.sleep(0.01)
    
    #Data iteration
    counter = 1

    for row in data:
        seperated_elements = row.split(',')
        #print(seperated_elements)
        
        index = seperated_elements[0].strip()
        st_name = seperated_elements[1].strip()
        subject = seperated_elements[2].strip()
        mark = int(seperated_elements[3].strip())

        #print(st_name, subject, mark)

        if subject not in divide_by_subject:
            divide_by_subject[subject] = {}
            #print(data_set)
        divide_by_subject[subject] [st_name] = mark
        
        indexing[index] = st_name
        #print(indexing)
        #get all indexes
        indexes = []
        for id, name in indexing.items():
            indexes.append(id)

        if index not in divide_by_student:
            divide_by_student[index] = {}
        
        divide_by_student[index] [subject] = mark
        #print(divide_by_student)
        print("\t"), progress_counter()
        print(f"    -->> {counter} Data Row Analized")
        counter += 1

    print("\n")
    time.sleep(2)
    print("-->> Data Analizing Completed!")
    print("\n")
    
    #This fucntion can get student's name in index
    def get_stName(index:str) -> str :
        for index1 , names in indexing.items() :
            if index1 == index :
                name = names
                return name
    

    #This fuction can get subject and marks of each student
    def get_one_student_marks(index:str) -> tuple : 

        for index2, sub_marks in divide_by_student.items():
            if index2 == index:
                subject_mark = [(sub, mark) for sub , mark in sub_marks.items()]

        return subject_mark

    #This fuction can get Total and Average of each student
    def get_total_and_avg(index:str) -> tuple :
        total = 0
        for ind1, sub_marks in divide_by_student.items():
            if ind1 == index:
                marks = [mark for sub , mark in sub_marks.items()]

        for mark in marks:
            total += mark 

        avg = total/len(marks)

        return total, avg

    #This fuction can find index is validated or no
    def check_index(index:str) -> bool :
        keys = divide_by_student.keys()
        for i in keys:
            if index == i :
                check = True
                break
            else:
                check = False

        return check
    #This fuction can grades of all subjects
    def get_grade(mark:int) -> str:

        if mark >= 75 :
            grade = "A"
        elif mark >= 65 :
            grade = "B"
        elif mark >= 55 :
            grade = "C"
        elif mark >= 35 :
            grade = "S"
        else:
            grade = "W"
        
        return grade 
    #this fuction can calulate students count
    def get_students_count() -> int :
        keys = list(indexing.keys())
        st_count = (len(keys))
        return st_count
    
    #This function can get mai max for one student
    def get_min_max(index:str) ->tuple:
        min , max = 100, 0
        for ind1, sub_marks in divide_by_student.items():
            if ind1 == index:
                for subject, mark in sub_marks.items() :
                    if mark > max :
                        max = mark
                        max_sub = subject
                    if mark < min :
                        min = mark 
                        min_sub = subject
        
        return max_sub, max, min_sub, min
    
    #this fuction can get subject count 
    def get_sub_count(index:str) -> int:
        subjects = []
        for keys, data in divide_by_student.items():
            for subs, mark, in data.items():
                if keys == index :
                    subjects.append(subs)
        lenth = len(subjects)             
        return lenth
    
    #this function for get key of tuple list for sorting
    def get_key_for_sort(places:tuple):
        return places[1]
        
    #this Fuction can get student's place
    def get_place(index:str) :
        places = []
        for ind in indexes :
            total, avg = get_total_and_avg(ind)
            places.append((ind,total))
        places.sort(key = get_key_for_sort, reverse = True)
        for id, place in enumerate(places):
            if place[0] == index :
                place1 = int(id) + 1 
        return place1

    #this fuction can get 1st place and avg
    def get_first_place():
        places = []
        for ind in indexes :
            total, avg = get_total_and_avg(ind)
            places.append((ind,total,avg))
        places.sort(key = get_key_for_sort, reverse = True)
        first = places[0]
        id , tot, av = first 
        name = get_stName(id)
        return name , av
    #This funtion for print report of one student
    def print_one_student_report(index:str) -> list[str] :

        marks_list = (get_one_student_marks(index))
        total , avg = get_total_and_avg(index)
        name = get_stName(index)
        
        #print anlized data Starting...
        print("\n")
        print(f"Index : {index}\t\tStudent's Name : {name}")
        print("\n")
        
        table = PrettyTable(['Subject', 'Mark', 'Grade', 'Total', 'Average'])
        for subs_marks in marks_list:
            subject, mark = subs_marks
            grade = get_grade(mark)
            avg = round(avg,2)
            table.add_row([subject, mark, grade, total, avg])
        print(table)
        print("\n")
        st_count = get_students_count() 
        max_sub, max, min_sub, min = get_min_max(index)
        print("Maximum Mark : %s - %d" % (max_sub, max), "\t\tMinmum Mark : %s - %d" %(min_sub, min))
        print("\n")
        place = get_place(index)
        print("students' Count : %d\t\tPlace : %d" % (st_count,place)) 
        print("\n")
        n, av = get_first_place() 
        print("First Place : %s\t\t Average of top student : %.2f" % (n,av))       
        #print anlized data Ending...

    
    #This funtion for print report of one student
    def write_one_student_report(index):

        marks_list = (get_one_student_marks(index))
        total , avg = get_total_and_avg(index)
        name = get_stName(index) 
        
        with open(f"{name}'s sudent_report.txt" , 'w') as file :
            #write anlized data Starting...
            file.write("\n")
            file.write(f"Index : {index}\t\tStudent's Name : {name}")
            file.write("\n")
            file.write("\n")
            table = PrettyTable(['Subject', 'Mark', 'Grade', 'Total', 'Average'])
            for subs_marks in marks_list:
                subject, mark = subs_marks
                grade = get_grade(mark)
                avg = round(avg,2)
                table.add_row([subject, mark, grade, total, avg])
            file.write(str(table))
            file.write("\n")
            file.write("\n")
            st_count = get_students_count()
            max_sub, max, min_sub, min = get_min_max(index)
            file.write("Maximum Mark : %s - %d" % (max_sub, max))
            file.write("\t\tMinimum Mark : %s - %d" %(min_sub, min))
            file.write("\n\n")
            place = get_place(index)
            file.write("students' Count : %d\t\tPlace : %d" % (st_count,place))
            file.write("\n\n")
            n, av = get_first_place() 
            file.write("First Place : %s\t\t Average of top student : %.2f" % (n,av))  
            #write anlized data Ending...

    #mode Selection
    print("Now you can select 2 modes for process your data ;\n")
    print("\t1st mode - Get One Student's Report\n\t2nd mode - Get Reports of all Students in class onece\n")
    print("\t\t1 = 1st mode\n\t\t2 = 2nd mode\n") 
    print("Select : ", end = '')
    mode = input()

    #this loop for mode validation
    while True:
        if mode == "1" :
            break
        elif mode == "2":
            break
        else:
            print(f"{mode} , is not a valid mode")
            print("\n")
            print("Please enter a valid Mode : ", end = '')
            mode = input()

    #check modes and processing data
    if mode == '1':
        time.sleep(0.25)
        print("\nNow enter the index number of stundet whose you want to get a report ;\n")
        print("So you can use indexes in below - \n")
        indexes = []
        for id, name in indexing.items():
            indexes.append(id)
        print(indexes)
        print("\n")
        index = input("Enter Student's Index : ")
        print("\n")

        checking_index = check_index(index)
        
        #this loop for check index is valid or no
        while True:
            if checking_index == False:
                print(f"{index} , is not a valid Index number for Student")
                index = input("Enter a valid Student's Index : ")
                print("\n")
                checking_index = check_index(index) 
            else:
                break
        subs_count = get_sub_count(index)
        for i in tqdm(range(subs_count)):
            sleep(0.5)
        print_one_student_report(index)
        print("\n")
        name = get_stName(index)
        print(f"\t\t--> {name}'s Report is Processing Completed!")
        print("\n")
        time.sleep(0.25)
        print("Now you can write this report to text file ; \n")
        print("Do you want write this report to txt file ?\n")
        print("\t 1 = Yes\n\t 2 = No\n")
        answer = input("Select : ")
        #this loop for validate answer 
        while True:
            if answer == "1":
                subs_count = get_sub_count(index)
                for i in tqdm(range(subs_count)):
                    sleep(0.5)
                write_one_student_report(index)
                print("\n")
                print(f"\t\t--> {name}'s Report is Writing Completed!")
                print("\n")
                break
            elif answer == "2" :
                break
            else:
                print(f"{answer}, Your input is invalid!\n")
                answer = input("Please enter a valid input : ")

    elif mode == "2" :
        time.sleep(0.25)
        keys = list(indexing.keys())

        for key in keys :
            index = key
            name = get_stName(index)
            subs_count = get_sub_count(index)
            for i in tqdm(range(subs_count)):
                sleep(0.25)
            print("\n")
            print_one_student_report(index)
            print("\n")
            print(f"\t\t--> {name}'s Report is Processing Completed!")
            print("\n")

        time.sleep(0.25)
        print("You can write reports of all students\n\n")
        print("Do you want to write reports of all sudents ?\n")
        print("\t\t 1 = Yes\n\t\t 2 = No\n")
        answer = input("Select : ")
        print("\n")
        while True:
            if answer == "1" :
                names = []
                for key in keys :
                    index = key
                    name = get_stName(index)
                    names.append(name)
                    subs_count = get_sub_count(index)
                    for i in tqdm(range(subs_count)):
                        sleep(0.5)
                    print("\n")
                    write_one_student_report(index)
                    print(f"\t\t--> {name}'s File is Writing Completed!")
                    print("\n")
                    print("-->> The following students' reports were generated to text files!")
                    print("\n")
                    print(names)
                    print("\n")
                break
            elif answer == "2" :
                break
            else:
                print(f"{answer}, Your input is invalid!\n")
                answer = input("Please enter a valid input : ")
                
    #program ending or reseting algorithum
    print("\n")
    time.sleep(0.25)
    print("-->> This Program is End!\n\nYou can stop or reset program\n\n\t 1 = Stop\n\t 2 = Reset\n")
    while True:
        fun_mode = input("What you want to do : ")
        print("\n")
        if fun_mode == "1" :
            mod = "1"
            break
        elif fun_mode == "2" :
            mod = "2"
            break
        else:
            print(f"\n{fun_mode}, Your input is invalid.\n\nEnter a valid input : \n")

    if mod == "1" :
        break
    elif mod == "2" :
        continue
time.sleep(0.25)
print("-->> Press any key to exit......")
input()