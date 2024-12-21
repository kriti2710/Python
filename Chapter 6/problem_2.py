marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))
marks3 = int(input("Enter your marks: "))

total_percentage = (marks1 + marks2 + marks3)*100/300

if(total_percentage >= 40 and marks1>33 and marks2>33 and marks3>33):
    print("you passed the exam", total_percentage)


else:
    print("you failed, try again next year", total_percentage)