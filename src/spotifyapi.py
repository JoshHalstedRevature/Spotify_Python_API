import urllib, httplib, json
import base64

class SpotifyRequests:
     """Handles communicating with the Spotify API"""
     __SpotifyConnect = httplib.HTTPSConnection('api.spotify.com')
     _access_token = ''
     _Client_ID = '4ffccca0d17a4f70b049aab86f2cc0bb'
     _Client_Secret = '5e2d61615b964c42a14d07e1c61d110c'

     def __init__(self):
          """Constructor"""
          self.passing_credentials()

     def __del__(self):
          """Destructor"""
          self.__SpotifyConnect.close()

     def jsonParsed(self, contentStr):
          """To parse the API return content into simple strings"""
          parsedDict = json.loads(contentStr)
          return parsedDict

     def passing_credentials(self):
          """For getting an access token (expiration is 3600)"""
          authConnection = httplib.HTTPSConnection('accounts.spotify.com')
          
          message = self._Client_ID + ':' + self._Client_Secret
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
          
          if response.status == 200:
               self._access_token = self.jsonParsed(response.read())["access_token"]
               print("Access token is valid for 3600 ...")
          else:
               print(response.read())   # it'll print out the error JSON message

     def search(self, q, rType, market = '', limit = -1, offset = -1, include_external = ''):
          """Will use the Spotify API's search URL to search for keywords in a category"""
          searchHeaders = {
               'Content-Length' : 0,                   # no body so content-length should explicitly be 0
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
          #print(response.status, response.reason)                                                   #replace with logging
          
          if response.status == 200:
               return response.read() 
          else:
               return str(response.status)

     def get_playlist_tracks(self, playlist_id, market = '', fields = '', additional_types = ''):
        """"""
        playlistHeaders = {
               'Content-Length' : 0,                   # no body so content-length should explicitly be 0
               'Accept' : 'application/json',
               'Content-Type' : 'application/json',
               'Authorization' : 'Bearer {}'.format(self._access_token)
          }
          
        params = ''

        if market != '': params += '&' + urllib.urlencode({ 'market' : market})
        if fields != '': params += '&' + urllib.urlencode({ 'fields' : fields})
        if additional_types != '': params += '&' + urllib.urlencode({ 'additional_types' : additional_types})

        self.__SpotifyConnect.request(
               'GET',
               url = '/v1/playlists/{}/tracks?'.format(playlist_id),
               headers = playlistHeaders
          )

        response = self.__SpotifyConnect.getresponse()

        if response.status == 200:
            return response.read()
        else:
            return str(response.status)
