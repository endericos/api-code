# https://www.youtube.com/watch?v=tb8gHvYlCFs&t=120s

import requests
# import json

### GET REQUEST
r = requests.get("https://xkcd.com/353/")

# List of properties available with their explanations
print(dir(r))
print(help(r))

# Content of response in unicode
print(r.text)

# 200 success, 300 redirects, 400 client error, 500 server error
print(r.status_code)

# Returns true for anything less than 400 response
print(r.ok)

# List of headers of the response
print(r.headers)

# Get the pic as bytes, write bytes to a png file
r = requests.get("https://imgs.xkcd.com/comics/python.png")

# Content of response in bytes
print(r.content)

with open("comic.png", "wb") as f:
    f.write(r.content)

# A simple HTTP Request & Response Service
# HTTPbin responses a json info of what we sent in request, so we can set all params properly
# http://httpbin.org/

# we can add params to url directly, but prone to mistakes httpbin.org/get?page=2&count=25,
# instead requests can generate url params for us
payload = {"page": 2, "count": 25}
r = requests.get("https://httpbin.org/get", params=payload)

print(r.text)
print(r.url)
print(r.headers)

### POST REQUEST

# Example of form-based auth
payload = {"username": "corey", "password": "testing"}
r = requests.post("https://httpbin.org/post", data=payload)

# This is same as r_dict = json.loads(r.text)
r_dict = r.json()

print(r.json())
print(r_dict["form"])

### PUT REQUEST
payload = {"page": 2, "count": 25}
r = requests.put("https://httpbin.org/put", params=payload)

r = requests.get(
    url="http://httpbin.org/basic-auth/corey/testing",
    auth=("corey", "testing"),  # update as coreyms and run again
)
print(r)

# Almost always add timeout
r = requests.get(url="http://httpbin.org/delay/6", timeout=3)
print(r)
