class FixedFloat:
	def __init__(self, amount):
		self.amount = amount

	def __repr__(self):
		return f'<FixedFloat {self.amount:.2f}>'

	@classmethod
	def from_sum(cls, val_1, val_2):
		return cls(val_1 + val_2)


test_1 = FixedFloat(25.1231231)
test_2 = FixedFloat.from_sum(25.1231, 32.13213213)

print('1.', test_1)
print('2.', test_2)


class Euro(FixedFloat):
	def __init__(self, amount):
		super().__init__(amount)
		self.symbol = '€'

	def __repr__(self):
		return f'<Euro {self.symbol}{self.amount:.2f}>'


money = Euro.from_sum(21.123, 21.213213)

print('3.', money)
