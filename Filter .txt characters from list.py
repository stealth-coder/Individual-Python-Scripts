

# This list contains things you want to get rid of
Filter = ["text"]


# lets say document "places.txt" contains "\\x00"
f = open("places.txt","rb")
content = f.read()
f.close()
content = str(content)

# we need to encode content with ascii then decode it
# it's a weird way of python requiring encoding and decoding so we can replace
# the documents ascii content
done = content.encode("ascii", errors="ignore").decode()


# this will look through the list and the document, if anything matches it will
# delete the matching object
for x in range (0, len(Filter)):
    done = done.replace(Filter[x], "")



# as mentioned aboce, the document places.txt containes "\\x00", and so does the
# Filter list, this means that "\\x00" will be deleted and new output will be
# added to a new document called "filtered.txt"
new = open("filtered.txt", "w")
new.write(done)
new.close()

