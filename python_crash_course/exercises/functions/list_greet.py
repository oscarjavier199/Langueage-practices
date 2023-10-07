#psssing a list as the argument of a function

def greet(names):
     for name in names:
          print(f"Nice to meet you {name}")
          
list_of_names = ['dexter', 'caroline']
greet(list_of_names)