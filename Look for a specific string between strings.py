
# this can be done with a document too, just open the doc and read it

s = "Hello there Ray"

start = 'Hello'
end = 'Ray'

filtered = s.split(start)[1].split(end)[0]
print(filtered)
