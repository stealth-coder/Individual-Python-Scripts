import urllib.request

# we are using a website called "https://ident.me" to grab the IP address off of it
# technically we are webscraping our IP

try:
    external_ip = urllib.request.urlopen("https://ident.me").read().decode("utf8")
    print(external_ip)
except Exception as e:
    print(e)
    
