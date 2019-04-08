import http.client
import json

# -- API information
HOSTNAME = "www.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000157764?content-type=text/plain"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)


r1 = conn.getresponse()
print()
print("Response received: ", end='')
print(r1.status, r1.reason)
text_json = r1.read().decode("utf-8")
count = json.loads(text_json)
conn.close()
