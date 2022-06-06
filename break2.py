items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
 
print("Checking the sale list!")
 
for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
 
print("End of search!")

#program will look for a specific item on a list of items
#then it will break when the item is found and will print
#end of search