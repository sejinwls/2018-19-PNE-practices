import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/count"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)


r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()


count = json.loads(text_json)
print("Total number of jokes:", count["value"])


ENDPOINT = "/categories"
conn = http.client.HTTPConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()


types = json.loads(text_json)

print("Total types of jokes: ", len(types))
print("Categories:", types["value"])

ENDPOINT = "/jokes/random"
conn = http.client.HTTPConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()


joke = json.loads(text_json)

print(joke["value"]['joke'])