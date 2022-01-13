#program to ..
#Python 3.9.6
import pyspark
import requests
import MergeData

# Globals for now
OAuth_Token = 'BQAagdfCBY0GqVjL8wixXIBcoJeVvjo7DUj3xMAbgnxltPI3fIB5OlzkkituDrcFLSt14h-KO47jllQpFDUJHTybXzxpcg35raiga0IMvhBmkjXYS9Mt3TPnDVDwAu-2pz-wYINSBdOEMaXuDuuGWTJIVpiywgd7jfviaeFv'
Client_ID = '4ffccca0d17a4f70b049aab86f2cc0bb'
Client_Secret = '5e2d61615b964c42a14d07e1c61d110c'

def init():
     # spark = SparkSession.builder\
     #      .appName('SparkByExamples.com')\
     #      .getOrCreate()
     
     #searching for kanye
     headers = {
          'Accept' : 'application/json',
          'Content-Type' : 'application/json',
          'Authorization' : f'Bearer {OAuth_Token}'
     }

     content = requests.get(
          'https://api.spotify.com/v1/search?q=kanye&type=artist',
          headers = headers
     )

     print(content.json())

def main():
     init()
     MergeData.MergeCSVs

if __name__ == '__main__':
     main()