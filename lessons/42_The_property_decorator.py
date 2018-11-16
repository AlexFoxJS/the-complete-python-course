class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
	def __init__(self, name, school, salary):
		super().__init__(name, school)
		self.salary = salary

	@property
	def weekly_salary(self):
		return self.salary * 7


alex = WorkingStudent('Alex', 'MIT', 15)

print('1.', alex.weekly_salary)
