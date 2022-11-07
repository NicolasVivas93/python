import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta'
}

states = tuple(capitals_dict)
print(states)

state = random.choice(states)
capital = capitals_dict[state]

print(state,capital)

answer = ''

while answer != capital:
    answer = input(f"What is the capital of {state}?")

