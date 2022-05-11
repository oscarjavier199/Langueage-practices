names = ['Amanda', 'Mercedes', 'Rachel', 'Elisabeth', 'Tay', 'Xavier', 'Joaquin', 'Sam']
 
for name in names:
  if 'x' in name.lower():
      continue
  elif 'o' in name.lower():
      pass
  elif 'x' in name.lower():
      break
  else:
       print(name)