#!/usr/bin/python
# -*- coding: euc-kr -*-

# ===========================================================
"""program"""
__author__ = "young phil, kwon"
__date__ = "creation: 2018-05-24, modification: 2018-05-24"
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

class Robot:
    """
    Robot Class
    """

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """
        constructor
        :param name: name of robot
        """
        # Initializes the data
        self.name = name
        print "(Initializing {})".format(self.name)

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """
        die method
        :param self:
        :return:
        """
        print "{} is being destroyed!".format(self.name)

        Robot.population -= 1

        if Robot.population == 0:
            print "{} was the last one.".format(self.name)
        else:
            print "There are still {:d} robots working.".format(Robot.population)

    def say_hi(self):
        """
        say_hi method
        :param self:
        :return:
        """
        print "Greetings, my masters call me {}".format(self.name)

    @classmethod
    def how_many(cls):
        """
        Prints the current population.
        """
        print "We have {:d} robots.".format(cls.population)

# Program main routine
if __name__ == "__main__":
    droid1 = Robot("R2-D2")
    droid1.say_hi()
    Robot.how_many()

    droid2 = Robot("C-3PO")
    droid2.say_hi()
    Robot.how_many()

    print "\nRobots can do some work here.\n"

    print "Robots have finished their work. So let's destroy them."
    droid1.die()
    droid2.die()

    Robot.how_many()

