#program to ..
#Python 2.7.5 in HortonWorks
#import logging
from pyspark.sql import SparkSession
import urllib, httplib

class SpotifyRequests:
     """Handles communicating with the Spotify API"""
     __SpotifyConnect = httplib.HTTPSConnection('api.spotify.com')
     _OAuth_Token = 'BQDhq7QX6_bacG9wwbUYYaGArfb3fenMSNAbeAmvDFDapZnZZCe3TOsy4mX_3AMUeRG2Ebocesfi8iTG0D9qPScAYBqk_QGKh_7NpL1iXeuasb_V9xO_cDX465Um1O4UlL37rHcaKM5tIMdLyHrSOO_RAAJHuW0N45JXHC_n' #expires after a day
     _Client_ID = '4ffccca0d17a4f70b049aab86f2cc0bb'
     _Client_Secret = '5e2d61615b964c42a14d07e1c61d110c'
     _headers = {
          'Content-Length' : 0,         # Needs to be set to 0 when passing headers
          'Accept' : 'application/json',
          'Content-Type' : 'application/json',
          'Authorization' : 'Bearer {}'.format(_OAuth_Token)
     }

     def __init__(self):
          pass

     def json(self, contentStr):
          pass

     def renew_OAuth_token(self):
          pass

     def search(self, q, rType, market = '', limit = 0, offset = 5, include_external = ''):
          
          self.__SpotifyConnect.request(
               'GET',
               url = '/v1/search?q=kanye&type=artist',
               headers = self._headers
          )
          response = self.__SpotifyConnect.getresponse()
          #print(response.status, response.reason) #replace with logging
          self.__SpotifyConnect.close()
          return response.read()

def init():
     """The beginning setup of the main function"""
     global spark 
     spark = SparkSession.builder\
          .appName('SparkByExamples.com')\
          .getOrCreate()

def main():
     init()
     spark.stop()

if __name__ == '__main__':
     main()