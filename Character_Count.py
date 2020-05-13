# This Program Counts Number of Characters Passed in 'message'(String) Variable

print("Enter The Message/String Value:")
# You can enter your Custom Message
message = input().lower()
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
