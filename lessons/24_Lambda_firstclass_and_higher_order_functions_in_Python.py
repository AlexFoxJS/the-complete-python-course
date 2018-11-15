userData = {'name': 'Alex', 'surname': 'Fox'}


def add_two(x, y):
	return x + y


print(add_two(10, 5))
print((lambda x, y: x + y)(10, 5))

add = lambda x, y: x + y


def who(data, identify):
	return identify(data)


# def identify_function(data):
# 	return data['name']
#
#
# print(identify_function(userData))

print(who(userData, lambda x: x['name']))
