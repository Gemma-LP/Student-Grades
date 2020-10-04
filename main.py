#ask studens for a % mark and convert this to a grade
#mark_grade function for conversion
#ask for target grade & print this with their mark
# if their target grade = exam grade, display a suitable message
#if target grade<exam grade dispaly a suitbale message 

mark = float(input("Enter your mark"))
if(mark >= 90):
  print("You achieved Grade A")
elif(mark >= 80):
  print("You achieved Grade B")
elif(mark >= 70):
  print("You achieved Grade C")
elif(mark >= 60):
  print("You achieved Grade D")
elif (mark >= 50):
  print("You achieved Grade E")
else:
  print("You score was fail")

target = float(input("Enter your target grade"))
if(mark == target):
  print("Well done, you achieved your target!")
elif(mark>target):
  print("Well done, you exceeded your target! Good work!")
elif(mark < target):
  print("You didn't reach your target grade this time.")
  


