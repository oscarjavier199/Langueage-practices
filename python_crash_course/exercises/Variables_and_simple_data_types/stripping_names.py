#stripping methods:

name = '  \tCharlie Brown        '

print('original str: ', name)

new_name = name.rstrip()
print('rstrip:', new_name)
new_name = name.lstrip()
print('ltrip:',new_name)
new_name = name.strip()
print('strip:', new_name)