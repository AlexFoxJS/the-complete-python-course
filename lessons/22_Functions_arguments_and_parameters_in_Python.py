def check_if_prime(number):
	for x in range(2, number):
		if number % x == 0:
			print(number, 'equals', x, '*', number // x)
			break
	else:
		# loop fell thought without finding a factor
		print(number, 'is prime number')


def check_primes(limit):
	for n in range(2, limit):
		check_if_prime(n)


check_primes(100)
