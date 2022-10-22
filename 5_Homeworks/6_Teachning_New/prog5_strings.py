theString = input("Enter some string: ")
subString = input("Enter sub-string to check for: ")

if subString in theString:
    print("Sub-string {} exists in main string".format(subString))
    howMany = theString.count(subString)
    print("Sub-string '{}' occurs {} times!".format(subString, howMany))
    where = theString.find(subString)
    print("Sub-string '{}' first occurence starts at location: {}".format(subString, where))
else:
    print("Sub-string '{}' DOES NOT exist in main string".format(subString))