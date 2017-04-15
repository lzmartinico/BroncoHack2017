import sys
import json
from datetime import datetime
from dateutil.parser import parse
import MySQLdb


#From PHP 
username = sys.argv[1]
source = sys.argv[2]
destination = sys.argv[3]
unfdate = sys.argv[4]
category = sys.argv[5]
sessionid = sys.argv[6]

date = unfdate[0:10]


import requests
url = 'https://maps.googleapis.com/maps/api/directions/json'
params = dict(
    origin=source,
    destination=destination,
    key='AIzaSyB21SUWi8UIy-WVLbzOOOAbDugp05LcPz8'
    )
resp = requests.get(url=url,params=params)
data=json.loads(resp.text)

steps = data['routes'][0]['legs'][0]['steps']

for step in steps:
	geoloc +=str(step['start_location']['lat'])+","+str(step['start_location']['lng']) + "|" 
	


#MYSQL Connection
conn1 = MySQLdb.connect(host= "54.153.76.72",
                  user="ridrdbreader",
                  passwd="ridrdbreader",
                  db="ridrDB")
x = conn1.cursor()

if category == "d":
	try:
   		x.execute("""INSERT IGNORE INTO `rides`(`source`, `destination`, `ridedate`, `userid`, `sessionid`, `category`,`route`) VALUES (%s, %s, %s, %s, %s, %s, %s)""",(source,destination,date, username, sessionid, category, geoloc ))
   		conn.commit()	

	except:
   		conn1.rollback()

conn1.close()


