#!/usr/bin/python
# -*- coding : euc-kr -*-

# ===========================================================
"""program information"""
__author__ = "young phil, kwon"
__date__ = "creation: 2018-05-28, modification: 2018-05-24"
__copyright__ = "Copyright 2018, The StartPy Project"
__credits__ = ["young phil kwon", "Star Play Lab"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "young phil kwon"
__email__ = "yfkwon@starplay.io"
__status__ = "Test Bed"
# ===========================================================

# ===========================================================
# imports
# ===========================================================

# ===========================================================

# ===========================================================
# Class Defined
class SchoolMember:
    """
    Represents any school member.
    """
    def __init__(self, name, age):
        """
        constructor
        :param name:
        :param age:
        """
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: {})'.format(self.name)

    def tell(self):
        """
        Tell my details.
        :return:
        """
        print 'Name:"{}" Age:"{}"'.format(self.name, self.age)


class Teacher(SchoolMember):
    """
    Represents a teacher.
    """

    def __init__(self, name, age, salary):
        """
        Constructor
        :param name:
        :param age:
        :param salary:
        """
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)

class Student(SchoolMember):
    """
    Represents a student.
    """
    def __init__(self, name, age, marks):
        """
        Constructor
        :param name:
        :param age:
        :param marks:
        """
        SchoolMember.__init__(self, name, age)
        self.makrs = marks
        print '(Initialized Student: {})'.format(self.name)

    def tell(self):
        """
        tell method
        :return:
        """
        SchoolMember.tell(self)
        print 'Marks: "{:d}"'.format(self.makrs)

# Program main routine
if __name__ == "__main__":
    t = Teacher('Mrs. Shrvidya', 40, 30000)
    s = Student('Swaroop', 25, 75)

    print

    members = [t, s]
    for member in members:
        # Works for both Teachers and Students
        member.tell()






