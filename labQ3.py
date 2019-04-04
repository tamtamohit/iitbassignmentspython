import urllib.request

import sys

url = "https://www.cse.iitb.ac.in/page222?batch=MTech1"
name_to_find = sys.argv[1].strip()
response = urllib.request.urlopen(url)   #request to url
html_text =  response.read()        #read url
if type(html_text) == bytes:
    html_text = html_text.decode('utf-8') #converting bytes response to string

begain = html_text.find(name_to_find)

name_search = html_text[:begain]

username_initial_index = name_search.rfind('href')
username_after_text = name_search[username_initial_index:]
username = username_after_text[username_after_text.rfind("~")+1:username_after_text.rfind("'")]

print(username)