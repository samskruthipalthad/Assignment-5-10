# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
# Get total classes held in school
totalClassesHeld = eval(input("Enter total number of classes held in school : "))
totalClassesAttend = eval(input("Enter total number of classes attended by the student : "))
percent = (totalClassesAttend / totalClassesHeld) * 100
if percent < 75:
    print("You cannot sit in the exams as your attendance is too low!")
else:
    print("You can sit in the exams as your attendance is fine.")