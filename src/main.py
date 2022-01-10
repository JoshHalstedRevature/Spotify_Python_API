#program to ..
#Python 2.7.5 in HortonWorks
#import logging
#from pyspark.sql import SparkSession
import urllib, httplib, json
import base64

class SpotifyRequests:
     """Handles communicating with the Spotify API"""
     __SpotifyConnect = httplib.HTTPSConnection('api.spotify.com')
     _access_token = 'BQB5b9QK_nn78YmAJfZEnRz2xb2L7pjE4x6ieE0iUl6gcBLvUULRt0XO-bK6-J0s6IlTdlI9uMeVPouWP5d9xZssu3yEpElRZJ35ER8aNM2b00Z9h80Lrdu-y_0oIuK4sAoLcysqiFaD4pJ9cZ012ucXMC_CcIcdbHKwuf8P' #expires after a day
     _Client_ID = '4ffccca0d17a4f70b049aab86f2cc0bb'
     _Client_Secret = '5e2d61615b964c42a14d07e1c61d110c'

     def __init__(self):
          """Constructor"""
          pass

     def __del__(self):
          """Destructor"""
          self.__SpotifyConnect.close()

     def jsonParsed(self, contentStr):
          """To parse the API return content into simple strings"""
          parsedString = json.loads(contentStr) # ??
          return parsedString

     def passing_credentials(self):
          """For getting an access token (expiration is 3600)"""
          authConnection = httplib.HTTPSConnection('accounts.spotify.com')
          
          message = self._Client_ID + ':' + self._Client_Secret
#          encoded_message = str(base64.b64encode(message.encode('ascii')))
          encoded_message = str(base64.b64encode(message))

          params = urllib.urlencode({
               'grant_type' : 'client_credentials'
          })

          authHeaders = {
               'Authorization' : 'Basic ' + encoded_message,
               'Content-Type' : 'application/x-www-form-urlencoded',
          }

          authConnection.request(
               'POST',
               url = '/api/token',
               body = params,
               headers = authHeaders
          )

          response = authConnection.getresponse()

          print(response.status, response.reason)  
          
          if response.status == 200:
               print(response.read())
               #self._access_token =  response.read() #need to parse this JSON String
               #Example of the output string:
               #{"access_token":"BQBYyox-Gte1kabunNBWRB5e302Euzi13fa5dxt-FSbZmoyf-kYDsw7zGaXVld2GU39LMoS-PX-y8Zncj6Q","token_type":"Bearer","expires_in":3600}
          else:
               print(response.read())

     def search(self, q, rType, market = '', limit = -1, offset = -1, include_external = ''):
          """Will use the Spotify API's search URL to search for keywords in a category"""
          searchHeaders = {
               'Content-Length' : 0,                   # no body so content-length should be 0
               'Accept' : 'application/json',
               'Content-Type' : 'application/json',
               'Authorization' : 'Bearer {}'.format(self._access_token)
          }
          
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
               headers = searchHeaders
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
     #init() #comment out when testing outside of the VM
     SpotifyRequests().passing_credentials()

     #spark.stop()  #comment out when testing outside of the VM

if __name__ == '__main__':
     main()