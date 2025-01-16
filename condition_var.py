"""
This script will implent our kn ow knowledge on comditiond and different
data types
"""

print("This IT organization has various skill sets.")
print("Find out your Match")
print("Enter Captitalized values: ")

DevOps = ["Jenkins", "Ainsible", "Bash", "Python", "Puppet", "Docker"]
Development = ("Nodejs", "Angularjs", ".net")
cntr_emp1 = {"Name": "Santa", "skills": "Blockchain", "code": "1024"}
cntr_emp2 = {"Name": "Manzi", "skills": "AI", "code": "1018"}
usr_name = input("Enter Your Name: ")
print(f"Hi {usr_name}")
usr_skill = input("Enter Your desired skill: ")
# print(usr_skill)

# Check in the data base for the matchingsAIAI

if usr_skill in DevOps:
    print(f"we have {usr_skill} in Devops Team.")
elif (usr_skill in Development):
    print(f"We have {usr_skill} in Development Team")

elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(
        f"We have employees with this skill with ypur mentioned skill {usr_skill}")

else:
    print("Skill not found")
    print("Please check your spellings")
    print(f"Please check your spellings Mr/Mrs {usr_name}")
