#program to ..
#Python 2.7.5 in HortonWorks
from pyspark.sql import SparkSession
import urllib, httplib

# Globals for now
OAuth_Token = 'BQDhq7QX6_bacG9wwbUYYaGArfb3fenMSNAbeAmvDFDapZnZZCe3TOsy4mX_3AMUeRG2Ebocesfi8iTG0D9qPScAYBqk_QGKh_7NpL1iXeuasb_V9xO_cDX465Um1O4UlL37rHcaKM5tIMdLyHrSOO_RAAJHuW0N45JXHC_n' #expires after a day
Client_ID = '4ffccca0d17a4f70b049aab86f2cc0bb'
Client_Secret = '5e2d61615b964c42a14d07e1c61d110c'

def init():
     spark = SparkSession.builder\
          .appName('SparkByExamples.com')\
          .getOrCreate()
     
     #searching for kanye
     headers = {
          'Content-Length' : 0,         # Needs to be set to 0
          'Accept' : 'application/json',
          'Content-Type' : 'application/json',
          'Authorization' : 'Bearer {}'.format(OAuth_Token)
     }

     connection = httplib.HTTPSConnection('api.spotify.com')
     
     connection.request(
          'GET',
          url = '/v1/search?q=kanye&type=artist',
          headers = headers
     )

     print(connection)

     response = connection.getresponse()
     print(response.status, response.reason)
     data = response.read()
     print(data)

     connection.close()

def main():
     init()

if __name__ == '__main__':
     main()