class Movie:
	def __init__(self, name, year):
		self.name = name
		self.year = year


the_matrix = Movie('The Matrix', '1999')

print(f"Movie name: {the_matrix.name}")
