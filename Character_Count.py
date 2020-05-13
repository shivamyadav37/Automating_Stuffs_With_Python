# This Program Counts Number of Characters Passed in 'message'(String) Variable

message = 'Hello alice , how ya doing , have a great day ahead' #you can have your own custom message
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
