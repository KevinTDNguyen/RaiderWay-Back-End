class Course:
    visited = list()
    
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.prerequisites = list()
        """
        None is the equivalent of 'null' in java, basically it is the "no-value" value in Python.
        However, you must assign it manually, python DOES NOT automatically assign a variable as None when
        it doesn't exist.
        """
    
    def addPrerequisite(self, prerequisite):
        self.prerequisites.append(prerequisite)

    def toDict(self):
        prereqCodeStr = ""
        for prereq in self.prerequisites:
            prereqCodeStr += (prereq.code + " ")

        prereqCodeStr = prereqCodeStr[0: len(prereqCodeStr)-1]    

        return {"name" : self.name, "code" : self.code, "prereq" : prereqCodeStr}

