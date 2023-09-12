import itertools
 
odd = [5, 7, 9]
even = {6, 8, 10}
 
all_numbers = itertools.chain(odd, even)
 
for number in all_numbers:
  print(number)