class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)


alex = Student('Alex', 'MIT')

alex.marks.append(10)
alex.marks.append(32)

print('1.', alex.average())
print('2.', Student.average(alex))


class Foo:
	@classmethod
	def hi_1(cls):
		print('3.', cls.__name__)

	@staticmethod
	def hi_2():
		print('4. Some static text value')


foo_object = Foo()
foo_object.hi_1()
foo_object.hi_2()
