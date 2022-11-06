# Exercise 1
captains = {}

# Exercise 2
captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'

print(captains)

# Exercise 3
if 'Enterprise' not in captains:
    captains['Enterprise'] = 'unknown'

if 'Discovery' not in captains:
    captains['Discovery'] = 'unknown'

print(captains)

#Exercise 4
for ship,captain in captains.items():
    print(f"The {ship} is captained by {captain}.")

#Exercise 5
del captains['Discovery']
print(captains)

# Exercise 6
captains = dict((('Enterprise', 'Picard'), ('Voyager', 'Janeway'), ('Defiant', 'Sisko')))
print(captains)
