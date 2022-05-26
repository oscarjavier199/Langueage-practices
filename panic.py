from cmath import phase
import difflib

#program will transform the string "Don’t panic!" into the string
#"on tap", using only remove, pop, extend and insert

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(0)
plist.pop(3)
plist.pop(2)
plist.pop(2)
plist.pop(2)
plist.pop(4)
plist.pop(4)
plist.pop(3)
plist.insert(2, "T")
plist.insert(4, "p")
plist.insert(2, " " )

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

#other way of doing it is:

# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)
#
# for i in range(4):
#     plist.pop()
# plist.pop(0)
# plist.remove(“ ’ ”)
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))
#
# new_phrase = ''.join(plist)
# print(plist)
# print(new_phrase)