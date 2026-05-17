import re

text ="My name is 12345 and my age is 24"
match = re.search(r"\d+",text)
print(match.group())

print(re.match(r"\d+","hello123"))
print(re.match(r"\d+","123aditya"))

text1 = "Numbers : 12 34 78"
print(re.findall(r"\d+",text1))

text2 = "Hello 123"
result = re.sub(r"\d+","***",text2 )  # r is raw string
print(result)

'''
\w = all characters
\d = digits
\s= space
'''

