saveChangesInTheEditor = str(input())
#s = "saveChangesInTheEditor"
count = 1
for i in saveChangesInTheEditor:
    if i.isupper():
        count += 1
print(count)