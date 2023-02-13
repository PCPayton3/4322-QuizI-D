'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file
infile = open('employee_data.csv', 'r', newline='')
employees = csv.reader(infile, delimiter=',')
next(employees)

# create an empty dictionary
employee_dict = {}

# use a loop to iterate through the csv file
bonus = "Marketing"

for emp in employees:
    if emp[3] in bonus:
        name = str(emp[1]) + ' ' + str(emp[2])
        dep = emp[3]
        salary = emp[5]
        pb = .1
        new_sal = (float(salary) * float(pb)) + float(salary)

    # check if the employee fits the search criteria
        print()
        print('=========================================')
        print()
        print("Name: ", name)
        print("Old Salarr: ", salary)

        employee_dict = {'Name': name,
                         "New Salary": new_sal}

        print()
        for k, v in employee_dict.items():
            print(k + ":", v)
        # print(employee_dict)


# iternate through the dictionary and print out the key and value as per printout
