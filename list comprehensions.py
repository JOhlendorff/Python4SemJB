from typing import SupportsRound
def split(word):
    return [char for char in word]

names = ["Hanne", "Hans", "Mikael", "Nikolaj", "Hannah"]
names_comp = [x for x in names if x[0] == "H"]
print(names)
print(names_comp)

numbers_cubed = [x * x * x for x in range(1,99)]
#print(numbers_cubed)

names_tuple = tuple((len(name), name) for name in names)
print(names_tuple)

txt = "0l dumb4ss b1tch, 57up12 a55 b1tc4, punk a55 b1tc4"
numbers = [int(s) for s in split(txt) if s.isdigit()]
print(numbers)

dice = [(i,j) for i in range(1,7) for j in range(1,7)]
print(dice)

name_dict = {name:len(name) for name in names}
print(f"Names as dictionary: {name_dict}\n")

number_dict = {int(number):math.sqrt(int(number)) for number in numbers}
print(f"Numbers as dictionary: {number_dict}\n")