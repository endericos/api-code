# following redirects with http.client Python module
# https://dev.to/tallesl/following-redirects-with-httpclient-python-module-439j

from http.client import HTTPSConnection
from urllib.parse import urljoin

def get(host, url):
    print(f"GET {url}")

    conn = HTTPSConnection(host)
    conn.request("GET", url)
    
    response = conn.getresponse()
    location_header = response.getheader("location")

    if location_header is None:
        return response
    else:
        location = urljoin(url, location_header)
        return get(host, location)

response = get("en.wikipedia.org", "/api/rest_v1/page/random/summary")

print(response.read())

# Following Redirects with Curl
# https://reqbin.com/req/python/c-bvijc9he/curl-follow-redirect#:~:text=To%20follow%20redirects%20with%20Curl,with%20the%20Location%20HTTP%20header

# To follow redirects with Curl, you need to use the -L or --location command-line option. 
# The server indicates that the resource has moved to a new location using the 3XX response code and provides the new address with the Location HTTP header.
# curl https://www.reqbin.com/echo -L
