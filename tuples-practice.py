from tabnanny import check
from turtle import position


cardinal_numbers = ('first', 'second', 'third')

print(cardinal_numbers[1])

position1, position2, position3 = cardinal_numbers

print(position1)
print(position2)
print(position3)

my_name = tuple('Nicolas')
print(my_name)

check_existence = 'x' in my_name
print(check_existence)

new_myname = my_name[1:]
print(new_myname)