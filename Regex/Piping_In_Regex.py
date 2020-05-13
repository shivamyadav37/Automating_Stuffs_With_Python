# Created by Shivam Yadav at 13-05-2020
import re

messageString = "Hello Alfred , Please Park the Batmobile , and get the Batcopter fixed"

batRegex = re.compile(r'Bat(man|mobile|copter)')

mo = batRegex.search(messageString)

print("Found", mo.group())
