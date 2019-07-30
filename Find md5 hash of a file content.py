import hashlib

# it's better to find a hash of the files content rather than just the files name
# the below will get the md5 has of the content of the file rather than just it's name

f = open("../../Peoples dissertation.txt", "rb")
content = f.read()
original_md5 = hashlib.md5(content).hexdigest()
print(original_md5)
