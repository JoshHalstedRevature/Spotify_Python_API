#program to ..
#Python 2.7.5 in HortonWorks
#import logging
#from pyspark.sql import SparkSession
import urllib, httplib

class SpotifyRequests:
     """Handles communicating with the Spotify API"""
     __SpotifyConnect = httplib.HTTPSConnection('api.spotify.com')
     _OAuth_Token = 'BQB5b9QK_nn78YmAJfZEnRz2xb2L7pjE4x6ieE0iUl6gcBLvUULRt0XO-bK6-J0s6IlTdlI9uMeVPouWP5d9xZssu3yEpElRZJ35ER8aNM2b00Z9h80Lrdu-y_0oIuK4sAoLcysqiFaD4pJ9cZ012ucXMC_CcIcdbHKwuf8P' #expires after a day
     _Client_ID = '4ffccca0d17a4f70b049aab86f2cc0bb'
     _Client_Secret = '5e2d61615b964c42a14d07e1c61d110c'
     _headers = {
          'Content-Length' : 0,         # Needs to be set to 0 when passing headers
          'Accept' : 'application/json',
          'Content-Type' : 'application/json',
          'Authorization' : 'Bearer {}'.format(_OAuth_Token)
     }

     def __init__(self):
          """Constructor"""
          pass

     def __del__(self):
          """Destructor"""
          self.__SpotifyConnect.close()

     def json(self, contentStr):
          """To parse the API return content in to simple strings"""
          pass

     def renew_OAuth_token(self):
          """Will acquire or renew an OAuth token programatically"""
          pass

     def search(self, q, rType, market = '', limit = -1, offset = -1, include_external = ''):
          """Will use the Spotify API's search URL to search for keywords in a category"""
          params = urllib.urlencode({
               'q' : q,
               'type' : rType
          })

          if market != '': params += '&' + urllib.urlencode({ 'market' : market})
          if limit != -1: params += '&' + urllib.urlencode({ 'limit' : limit})
          if offset != -1: params += '&' + urllib.urlencode({ 'offset' : offset})
          if include_external != '': params += '&' + urllib.urlencode({ 'include_external' : include_external})     

          self.__SpotifyConnect.request(
               'GET',
               url = '/v1/search?{}'.format(params),
               headers = self._headers
          )

          response = self.__SpotifyConnect.getresponse()
          #print('api.spotify.com/v1/search?{}'.format(params))                                     #replace with logging 
          print(response.status, response.reason)                                                   #replace with logging
          
          if response.status == 200:
               return response.read() 
          else:
               return str(response.status)

def init():
     """The beginning setup of the main function"""
     global spark 
     spark = SparkSession.builder \
          .appName('SparkByExamples.com') \
          .getOrCreate()

def main():
     #init()
     print(SpotifyRequests().search("kanye west", "artist")) 

     #spark.stop()

if __name__ == '__main__':
     main()