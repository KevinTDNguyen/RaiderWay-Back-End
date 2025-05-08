import json
from Course import Course

# math1 = Course("Math1", "MTH1")
# math2 = Course("Math2", "MTH2")
# math3A = Course("Math3A", "MTH3A")
# math3B = Course("Math3B", "MTH3B")
# math4 = Course("Math4", "MTH4")

# math4.setPrerequisite(math3A)
# math4.setPrerequisite(math3B)
# math3A.setPrerequisite(math2)
# math3B.setPrerequisite(math2)
# math2.setPrerequisite(math1)

# math4.printPrerequisite()

with open("mathcourses.json", "r") as file:
    data = json.load(file) #turns the JSON data into a python dictionary

for course in data:
    print(course["name"], course["code"])

