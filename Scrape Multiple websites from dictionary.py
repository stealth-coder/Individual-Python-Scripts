import urllib.request
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

DDD = {"GitHub": "https://www.github.com",

       "Google": "https://www.google.com",

       "Facebook": "https://www.facebook.com",

       "YouTube": "https://www.yourube.com",
}

length = len(DDD)

for x in DDD:
    try:
        URLLink = DDD[x]
        print(URLLink)
        # query the website and return the html to the variable "page"
        page = urllib.request.urlopen(URLLink)

        # prase the html using beautiful soup and store in variable "soup"
        # if you print the variable "soup" it will output organized html code
        URL = BeautifulSoup(page, 'html.parser')
        strsoup = str(URL)
        f = open("{0}.html".format(x),"w")
        f.write(strsoup)
        f.close()
        
    except:
        print("error")


