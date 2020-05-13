# This Program demonstrates to find USA Phone numbers.

# Importing regex module
import re

message = "Hello this is my Phone number , 404-231-9384 , So call me at 404-231-9384"

# Regex Expression
phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Compile Function passes the String

x = phoneNumber.search(message)  # Search finds only one time
# x = phoneNumber.findall(message)  # findall finds all the Matching Strings

print("Phone Number is:", x.group())  # Use this in Case of using 'search'
# print(x) # Use this in case of findall


#########################################################
# For finding area Code of the Phone Number
phoneNumber1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
y = phoneNumber1.search(message)
print("Area Code for the Phone Number is :", y.group(1))

#########################################################
