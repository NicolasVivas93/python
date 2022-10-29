file = input("Enter file name:")

try:
    fhand = open(file, 'r')
except:
    print("File not found")
    quit()
    
for line in fhand:
    line = line.rstrip().upper()
    print(line)

