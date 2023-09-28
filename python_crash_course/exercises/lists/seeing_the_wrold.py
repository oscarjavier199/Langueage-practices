#list
places_to_visit = ['oslo', 'copenhagen', 'munich', 'nice', 'sydney']
#print original list
print(f'Original list:', places_to_visit)
#prints sorted list (alphabetical order)
print('sorted list:', sorted(places_to_visit))
#prints original list
print('Original list:',places_to_visit)
#prints reversed alphabetical order
print('reverse sorted:', sorted(places_to_visit, reverse=True))
#prints original list
print('original list', places_to_visit)
#reverses list
places_to_visit.reverse()
#prints reversed list
print('Reversed list:', places_to_visit)
#reverses list again
places_to_visit.reverse()
#prints reversed list
print('reversed list again:', places_to_visit)
#sorts list permanently and alphabetically 
places_to_visit.sort()
#prints sort list 
print('sort alphabetical:', places_to_visit)
#sorts list again in reverse, the list is permanently changed
places_to_visit.sort(reverse=True)
#prints final list
print('reverse sorted:', places_to_visit)