import sys
print ('sys.argv[5]')

#From PHP 
'''username = argv[1]
source = argv[2]
destination = argv[3]
date = argv[4]
category = argv[5]
'''
#things = argv


#google maps API

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

if sys.version_info <= (2, 4):
  error = 'Requires Python Version 2.5 or above... exiting.'
  print >> sys.stderr, error
  sys.exit(1)


#requirements = [
 #   'requests<=2.11.1',
#]

setup(name='googlemaps',
      version='2.4.6-dev',
      description='Python client library for Google Maps API Web Services',
      scripts=[],
      url='https://github.com/googlemaps/google-maps-services-python',
      packages=['googlemaps'],
      license='Apache 2.0',
      platforms='Posix; MacOS X; Windows',
      #setup_requires=requirements,
      #install_requires=requirements,
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Internet',
                   ]
      )

print ("hello")

from googlemaps import GoogleMaps
gmaps = GoogleMaps(api_key)
from googlemaps import convert
from googlemaps.convert import as_list
from gmaps import distance_matrix
parameters = distance_matrix()

print ('parameters')

'''def SQL_connection():
#MYSQL Connection
import MySQLdb
conn = MySQLdb.connect(host= "54.153.76.72",
                  user="ridrdbreader",
                  passwd="ridrdbreader",
                  db="ridrDB")
x = conn.cursor()


#getting route
def get_route(): 
if category == "d":
	try:
   		x.execute("""INSERT INTO `rides`(`source`, `dest`, `ridedate`, `route`) VALUES ("source","destination","date", )""",(188,90))
   		conn.commit()
	

	except:
   		conn.rollback()

conn.close()
'''
