'''
Created on Feb 10, 2019

@author: ITAUser

Algorithm:
1. Make a .json txt file that will store the assignments
2. Import .json file into code
3. create user input for finding assignments
4. find the user's assignment in data
    - If the user's input is in our data
    - the user's input isn't in our data
'''
import json

answer = ""

while(answer != "no"):
    with open("assignments_1.json", "r") as f_r:
        data = json.load(f_r)
        print("\n\nWe have the following assignments due:")
        for i in data:
            print("\n" + i)
        ans = input("\n1. Find an assignment \n2. Add assignment \n\n")
        if ans == '1':
            assignment = input("Enter Assignment:")
            print("The assignment {} due date is {}".format(assignment, data.get(assignment, "not in our database")))
        elif(ans == '2'):
            n = int(input("How many assignments do you want to add?"))
            i = 0
            while i < n:
                print("\n Add Assignment", i+1)
                new_assignment = input ("\nEnter the Assignment:")
                new_dueDate = input ("Enter the due date (m/dd/yy):")
                data[new_assignment] = new_dueDate
                with open("assignments_1.json", "w") as f_w:
                    json.dump(data, f_w)
                    print("Assignment Added!")
                i+=1
            else:
                print("\nInvalid Choice!")
                answer = input ("\nDo you want to use this again?(yes/no)")
                
        