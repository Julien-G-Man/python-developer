# Code for finding CWA of a Student
import statistics as stx
from statistics import mean

print("******* CWA Calculator ********")  

subjects = []
num_subjects = int(input("How many subjects do you offer? "))

for i in range(num_subjects):
    print("------------")
    n = i+1
    name = input(f"Subject #{n}: ")
    score = float(input(f"{name} Score: "))
    credit = float(input(f"{name} Credit: "))
    subjects.append({'name': name, 'score':score, 'credit': credit, 'id':n})
    subject_n = name
    
total_weighted_score = sum(sub['score'] * sub['credit'] for sub in subjects)
total_credits = sum(sub['credit'] for sub in subjects)

if total_credits == 0:
    print("Total credits cannot be zero.")
else:
    cwa = total_weighted_score / total_credits
    print("-----------------")
    for subject in subjects:
        print(f"Subject: {name} Score: {score} Credit: {credit}")
    print("-----------------")
    print(f" Your CWA is: {cwa:.2f}")    
   