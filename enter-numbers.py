number = None

total = 0
count = 0

while number != 'done':
    number = input("Enter a number:")
    try:
        number_conv = int(number)
    except:
        print("Bad data")
    
    total = total + number_conv
    count = count + 1

avg = total / count

print("Count:", count)
print("Total:", total)
print("Average:", avg)