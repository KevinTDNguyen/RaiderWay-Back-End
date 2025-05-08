class Course:
    visited = list()

    def __init__(self, name, courseCode):
        self.name = name
        self.courseCode = courseCode
        self.prerequisite = list()
        """
        None is the equivalent of 'null' in java, basically it is the "no-value" value in Python.
        However, you must assign it manually, python DOES NOT automatically assign a variable as None when
        it doesn't exist.
        """

    def setPrerequisite(self, prerequisite):
        self.prerequisite.append(prerequisite)

    def printPrerequisite(self):

        if len(self.prerequisite) != 0:
            for prereq in self.prerequisite:
                if prereq not in Course.visited:
                    Course.visited.append(prereq)
                    obj = prereq
                    obj.printPrerequisite()

        print(self.name)