#! /usr/bin/env python3
import os
import requests
import re

desc_path = "supplier-data/descriptions/"
web_service_url = "http://34.132.228.57/fruits/"
image_path = 'supplier-data/images/'

text_files = sorted(os.listdir(desc_path))
jpeg_images = sorted([image_name for image_name in os.listdir(image_path) if '.jpeg' in image_name])

# Define a function to read the feedback from a file
list_content = []
image_counter = 0

def read_feedback(file_path):
    with open(file_path, 'r') as feedtxt:
        lines = feedtxt.readlines()
    name = lines[0].strip()
    weight = re.sub("\D", "", lines[1].strip())
    description = lines[2].strip()
    return {
        "name": name,
        "weight": weight,
        "description": description,
     }

# List all files in the directory
files = sorted(os.listdir(desc_path))

# Create a dictionary to store the feedback
data = {}

# Iterate over the files. run your code completely in the iteration
for file in files:

    # Read the feedback from the file. (/data/feedback/007.txt)
    feedback = read_feedback('{}/{}'.format(desc_path,file))
    counter = 0
    # Add the feedback to the dictionary
    data = feedback
    counter += 1

data['image_name'] = jpeg_images[image_counter]
list_content.append(data)
image_counter += 1


# Send a POST request to the web service for each file
for item in list_content:
  response = requests.post(web_service_url, json = item)

    # Check the response status code
  if not response.ok:
      raise Exception("Post failed with status code {} | file {}".format(response.status_code, file))
  print("Description added")
