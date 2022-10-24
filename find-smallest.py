numbers = [9,41, 3, 122, 74, -5]

smallest = None

for number in numbers:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number

print(smallest)
