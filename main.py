import json
from Course import Course

"""
Below was the ancient way of initializing prerequisites and courses
"""
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

"""
Revised way of initializing and setting prerequisites
"""
allCourses = dict() # init dictionary w/ course objects

with open("proof.json", "r") as file:
    course_data = json.load(file) #turns all json data in one dictionary

for course in course_data: #this loop initiates all objects
    allCourses[course["code"]] = Course(course["name"], course["code"])

#inits prereqs
for jsonObj in course_data:
    course = allCourses[jsonObj["code"]] #gets the current course object in the allCourses dictionary using the obj["code"] as a key
    for prereqCode in jsonObj["prereq"]:
        prereqObj = allCourses[prereqCode] #redundant for clarity
        course.setPrerequisite(prereqObj)

for course in allCourses:
    prereqStr = ""
    for prereq in allCourses[course].prerequisite:
        prereqStr += prereq.courseCode + " "
    print(course + ": " + prereqStr)

"""
to quickly view the contents of the dictionary copy & paste the loop below
"""
# for item in allCourses:
#     print(item + ": " + allCourses[item].name)




