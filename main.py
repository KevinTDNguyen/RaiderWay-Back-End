from flask import Flask, jsonify
import json
from Course import Course

"""
this is the flask constructor for the Flask class --> it is good form to do __name__ but 
any string works :D
"""
app = Flask(__name__) 

#python flask torture
@app.route("/getprereqs/<coursecode>", methods = ["GET"])
def getPrereqs(coursecode): # need to make a way to pass a local argument
    
    prereqList = list()
    dictList = list()
    obj = allCourses.get(coursecode)
    while True:
        if len(obj.prerequisites) == 0:
            for courseObj in prereqList:
                dictList.append(courseObj.toDict())
            return jsonify(dictList)
        
        for i in range(len(obj.prerequisites)):
            prereqList.append(obj.prerequisites[i])
            if i == len(obj.prerequisites) - 1:
                obj = obj.prerequisites[i]     
          
# @app.route("/")
# def printHi():
#     return allCourses.get("MTH1").name # DICTIONARIES ARE ALL GLOBAL IN PYTHON AND CAN BE ACCESSED ANYWHERE

"""
Revised way of initializing and setting prerequisites
"""

allCourses = dict() # init dictionary w/ course objects

with open("proof.json", "r") as file:
    course_data = json.load(file) #turns all json data in one dictionary

for course in course_data: #this loop initiates all objects
    allCourses[course["code"]] = Course(course["name"], course["code"])

#inits prereqs database
for jsonObj in course_data:
    course = allCourses[jsonObj["code"]] #gets the current course object in the allCourses dictionary using the obj["code"] as a key
    for prereqCode in jsonObj["prereq"]:
        prereqObj = allCourses.get(prereqCode) #.get() prevents crashes when a key doesn't exist --> this keeps the course prereq field empty
        if prereqObj:
            course.addPrerequisite(prereqObj)

# localList = getPrereqs(allCourses["MTH4"])

# for item in localList:
#     print(item["name"])

app.run(host="0.0.0.0", port=80)
"""
Prints out all courses and prereqs
"""
# for course in allCourses:
#     prereqStr = ""
#     for prereq in allCourses[course].prerequisite:
#         prereqStr += prereq.code + " "
#     print(course + ": " + prereqStr)

"""
-NOTES-
use .get(key) method when accessing a potentially non-existant key
""" 