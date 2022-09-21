import itertools
 
for i in itertools.count(start=0, step=2):
  print(i)
  if i >= 20:
    break