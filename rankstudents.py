# Read the Names And total Marks Scored By The Stundents Of Your Class OF At Least 3 or more  students
# Rank The Top 3 Students of Your Class
# Provide A Cash reward oF $500 to the First Rank , $300 To The Second Rank And $ 100 To The Third Rank . The Value Of Cash Reward Cannot Be Modified
# Make A Statement OF Appreciation To The Students Who Scored 950 Marks And Above
# Lets Start....

import operator
import random

def readStudentDetails():
    print()
    # { 'John': 600, 'Ben': 800, 'David': 950, 'Mark': 980}
    print("Enter the number of students: ")
    numberOfStudents = int(input())
    studentRecord = {}
    for student in range(0, numberOfStudents):
        print("Enter the name of the student: ")
        name = input()
        print("Enter the marks of students: ")
        marks = int(input())
        studentRecord[name] = marks
    print()
    return studentRecord

def rankStudents(studentRecord):
    try:
        print()
        # [('Mark', 980), ('David', 950), ('Ben', 800), ('John', 600)]
        sortedStudentRecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse = True)
        print(sortedStudentRecord)
        print("{} has secured first rank, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print("{} has secured second rank, scoring {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print("{} has secured third rank, scoring {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        print()
        return sortedStudentRecord
    except IndexError:
        print("Enter a minimum of 3 students")
        quit()


def rewardStudents(sortedStudentRecord, reward):
    print()
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
    print()


def appreciateStudents(sortedStudentRecord):
    print()
    for record in sortedStudentRecord:
        if record[1] >= 950:
            print("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
        else:
            break
    print()


studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)
