data = ((1,2),(3,4))
print(data)


for i in range(len(data)):
    suma = sum(data[i])
    print(f"Row {i+1} sum: {suma}")

numbers = [4,3,2,1]
print(numbers)

numbers2 = numbers[:]
print(numbers2)

numbers.sort()
print(numbers)
