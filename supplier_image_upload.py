#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module
directory_path = 'supplier-data/images/'

url = "http://localhost/upload/"
images = os.listdir(directory_path)

for file in images:
  if '.jpeg' in file:
    with open('{}/{}'.format(directory_path,file), 'rb') as opened:
      r = requests.post(url, files={'file': opened})



    if not r.ok:
       raise Exception("Post failed with status code {} | file {}".format(r.status_code, file))
    print("Image added")
