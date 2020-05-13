# This Program demonstrates to find USA Phone numbers.

# Importing regex module
import re

message = "Hello this is my Phone number , 404-231-9384"

# Regex Expression
phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Compile Fuction passes the String

x = phoneNumber.search(message)

print("Phone Number is:", x.group())
