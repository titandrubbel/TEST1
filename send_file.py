import requests
import os

url = "http://localhost:5000/api/classification/classify"

#fin = open('example.yaml', 'rb')
#files = {'file': fin}

files = os.listdir("/projects/test")
files = {'file': open('{}'.format(files[1]), 'rb')}

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
