'''
#3 Portfolio grade problem
Write a program that inputs a mark from the keyboard for sections of a project: ‘analysis’, ‘design’, ‘implementation’ and ‘evaluation’.  The program should output the total mark, the grade, and how many more marks were needed to get into the next mark band.

Grades are:
		<2	U
		2	  1
		4	  2
		13	3
		22	4
		31	5
		41	6
		54	7
		67	8
		80	9
'''

grades = [2, 4, 13, 22, 31, 41, 54, 67, 80]

analysis = int(input("Enter your marks for the analysis? "))
design = int(input("Enter your marks for the design? "))
implementation = int(input("Enter your marks for the implementation? "))
evaluation = int(input("Enter your marks for the evaluation? "))
#Task 1 - add 3 more inputs for design, implementation and evaluation

#Task 2 - complete the sum to add together the 3 inputs you just made to the analysis
total = analysis + design + implementation + evaluation

if total < 2:
  grade = "U"
  toNextGrade = 2 - total
for i in range(len(grades)):
  #print('i is "%s" and grades[i] is "%s"' % (i, grades[i]))
  if total < grades[i]:
    grade = str(i)
    toNextGrade = grades[i] - total
    break
#Task 3 - complete the selection statement to include the grades 2 to 9


print("Your total mark was", total)
#Task 4 - add the output statement to output how many marks to the next grade. 
print("You achived grade %s, and you needed %s more marks to achive the next grade." % (grade, toNextGrade))