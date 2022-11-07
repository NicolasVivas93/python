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
capital_lower = capital.lower()
while answer != capital_lower:
    answer = input(f"What is the capital of {state}?").lower()

    if answer == 'exit':
        print(f"The correct answer is: {capital}")
        print("Goodbye")
        break

if answer == capital_lower:
    print("Correct")


