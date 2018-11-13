# frends = ['alex', 'ralf', 'bob']
# gests = ['rafael', 'bob', 'ralf', 'greg', 'alex']
#
# gests_lower = {name.lower() for name in gests}
# present_frends = [name.capitalize() for name in gests if name.lower() in gests_lower]
#
# print(present_frends)
# ----------------------------------------------------------------------------------------------------------------------

# names = ['alex', 'ralf', 'bob']
# time_last_seen = [10, 5, 8]
#
# frends_last_seen = {names[i]: time_last_seen[i] for i in range(len(names))}
#
# print(frends_last_seen)
# ----------------------------------------------------------------------------------------------------------------------

names = ['alex', 'ralf', 'bob']
time_last_seen = [10, 5, 8]

frends_last_seen = dict(zip(names, time_last_seen))

print(frends_last_seen)
# ----------------------------------------------------------------------------------------------------------------------
