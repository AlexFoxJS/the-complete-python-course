# student_1 = {
# 	'name': 'Alex Fox',
# 	'grades': [20, 40, 88, 90]
# }
#
#
# def average_grade(student):
# 	return sum(student['grades']) / len(student['grades'])
#
#
# print(average_grade(student_1))


# OOP
class Student:
	def __init__(self, name, grades):
		self.name = name
		self.grades = grades

	def avarage(self):
		return sum(self.grades) / len(self.grades)


student_1 = Student('Alex Fox', [20, 40, 88, 90])
student_2 = Student('Axel Xof', [50, 31, 68, 110])

print(f"Name: {student_1.name}, Avarage: {student_1.avarage()}, Class: {student_1.__class__}")
print(f"Name: {student_2.name}, Avarage: {student_2.avarage()}, Class: {student_2.__class__}")
