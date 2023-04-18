a = "Learning"
b = "Python"
c = "is"
d = "Amazing"
e = " - ".join([a, b, c, d])

# to find the index number of given character, if doesn't find the text returns -1 instead of error
result = e.find("i")

# replace text is with Bishnu

newText = e.replace("is", "Bishnu")
print(newText)

# print(e)
