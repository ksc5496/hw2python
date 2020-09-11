# Author: Krish Choudhary ksc5496@psu.edu

def getGradePoint(lettergrade):
  if lettergrade == "A":
    return 4.0
  elif lettergrade == "A-":
    return 3.67
  elif lettergrade == "B+":
    return 3.33
  elif lettergrade == "B":
    return 3.0
  elif lettergrade == "B-":
    return 2.67
  elif lettergrade == "C+":
    return 2.33
  elif lettergrade == "C":
    return 2.0
  elif lettergrade == "D":
    return 1.0
  else:
    return 0.0

def run():
  lettergrade = input("Enter your course 1 letter grade: ")
  coursecredit = int(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {getGradePoint(lettergrade)}")
  lettergrade1 = input("Enter your course 2 letter grade: ")
  coursecredit1 = int(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {getGradePoint(lettergrade1)}")
  lettergrade2 = input("Enter your course 3 letter grade: ")
  coursecredit2 = int(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {getGradePoint(lettergrade2)}")
  gpa = (getGradePoint(lettergrade)*coursecredit + getGradePoint(lettergrade1)*coursecredit1 + getGradePoint(lettergrade2)*coursecredit2)/(coursecredit + coursecredit1 + coursecredit2)
  gpa = float(gpa)
  print(f"Your GPA is: {gpa}")

if __name__ == "__main__":
  run()