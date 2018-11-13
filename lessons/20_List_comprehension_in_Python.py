# test_1 = list(range(20))
# test_2 = [n*2 for n in test_1 if n %2 == 1]
#
# print(test_2)
#
# ----------------------------------------------------------------------------------------------------------------------

frends = ['alex', 'ralf', 'bob']
gests = ['Rafael', 'bob', 'Ralf', 'Greg', 'Alex']

# present_frends = []
#
# for frend in frends:
#   for gest in gests:
#     if frend.lower() == gest.lower():
#       present_frends.append(gest.title())

present_frends = [name.capitalize() for name in gests if name.lower() in frends]

print(present_frends)