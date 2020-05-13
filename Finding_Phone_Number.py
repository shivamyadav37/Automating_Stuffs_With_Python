# This Program demonstrates to find USA Phone numbers.

# Importing regex module
import re

message = "Hello this is my Phone number , 404-231-9384 , So call me at 404-231-9384"

# Regex Expression
phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Compile Function passes the String

# x = phoneNumber.search(message)
x = phoneNumber.findall(message)

# print("Phone Number is:", x.group())
print(x)
