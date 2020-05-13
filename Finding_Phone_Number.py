import re

message = "Hello this is my Phone number , 404-231-9384"

phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

x = phoneNumber.search(message)

print("Phone Number is:", x.group())
