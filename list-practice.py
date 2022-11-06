food = ['rice', 'beans']
print(food)

food.append('brocoli')
print(food)

food.extend(['pizza', 'bread'])
print(food)

print(food[:2])
print(food[-1])

breakfast_str = "eggs, fruit, orange juice"

breakfast = breakfast_str.split(",")
print(breakfast)
print(len(breakfast))

lengths = [len(item) for item in breakfast]
print(lengths)