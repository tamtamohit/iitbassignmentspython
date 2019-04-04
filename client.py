import sys,requests

port = '5000'
text_content = 'mohima'
# text_content = sys.argv[1]
url = 'http://0.0.0.0:%s'%(port)
json_data = {
    'string':text_content
}

response = requests.post(url=url,json=json_data)

if response.json()['result']:
    print("String is a palindrome")
else:
    print("String is not a palindrome")