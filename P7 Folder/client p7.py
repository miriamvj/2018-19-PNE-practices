import http.client
import json
from Seq import Seq
import collections
PORT = 80
SERVER = 'rest.ensembl.org'

conn = http.client.HTTPConnection(SERVER, PORT)
conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

r1 = conn.getresponse()

data = r1.read().decode('utf-8')
general = json.loads(data)

information = Seq(general['seq'])


print("Total information:", information.len())
print("Number of total T bases:",information.count('T') )
print('The maximum number is:', max(information.count('A'),information.count('C'),information.count('G'),information.count('T')))
popular = collections.Counter(information.strbase).most_common(1)[0]
popularbase = popular[0]
print("The most popular is: ", popular[0], "and the percentage is: {}".format(information.percentage(str(popular[0]))))
print('The percentage of Gs:', information.percentage('G'), '%')
print('The percentage of As:', information.percentage('A'), '%')
print('The percentage of Cs:', information.percentage('C'), '%')
print('The percentage of Ts:', information.percentage('T'), '%')