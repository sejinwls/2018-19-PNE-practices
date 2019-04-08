import http.client
from seq import Seq

HOSTNAME = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000165879.8"

METHOD = "GET"
headers = { "Content-Type" : "text/plain"}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection

seq = Seq(r1.read().decode("utf-8"))
conn.close()
print("The FRAT1 gene has a total of {} bases".format(seq.len()))
print("The FRAT1 gene has {} T bases".format(seq.count("T")))
bases = ["A", "C", "G", "T"]
best_base = ''
base_number = 0
for base in bases:
    if seq.count(base) >= base_number:
        best_base = base
print("The most popular gene in the FRAT1 gene is {}. It represents a {}% of the total".format(best_base,round(seq.perc(best_base),2)))
for base in bases:
    print("The percentage of the base {} is {}%".format(base, round(seq.perc(base),2)))
