import re

# open the sample file used
file = open('..\\data\\names.txt', "r", encoding="utf-8")

# read the content of the file opened
content = file.readlines()

result = []
for i in content:
    new_line = "".join(re.split("[^a-zA-Zа-яА-Я]*", i))
    if new_line != '':
        result.append(new_line)

print(result)

"""
# Python code to demonstrate
# to get characters from string
import re

# initialising string
ini_string = "123()#$ABGFDabcjw"
ini_string2 = "abceddfgh"

# printing strings
print("initial string : ", ini_string, ini_string2)

# code to find characters in string
res1 = "".join(re.split("[^a-zA-Z]*", ini_string))
res2 = "".join(re.split("[^a-zA-Z]*", ini_string2))

# printing resultant string
print("first string result: ", str(res1))
print("second string result: ", str(res2))
"""