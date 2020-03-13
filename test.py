import requests
import os

url = "http://localhost:5000/"
fin = open('main.py', 'rb')
files = {'file': fin}

#files = os.listdir("/projects/test")
#files = {'file': open('{}'.format(files[1]), 'rb')}

try:
  r = requests.post(url, files=files)
	(r.status_code)
	print(r.text)
finally:
	fin.close()
