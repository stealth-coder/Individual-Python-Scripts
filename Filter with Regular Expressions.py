import re

f = open("places.txt", "rb")
content = f.read()
f.close()

content = str(content)

filtered = re.sub("[0-5][0-9]", "", content)   # replace any number between 00 and 59 with nothing
filtered = filtered.replace("\\x", "")         # replace \\x with nothing
filtered = filtered.replace("http", "\nhttp")  # replace http to \nhttp which means new line before http

doc = open("Filtered.txt", "w") # output the filtered into a new doc
doc.write(filtered)
doc.close()
