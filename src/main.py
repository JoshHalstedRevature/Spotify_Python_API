#program to ..
#Python 2.7.5 in HortonWorks
from sparkcontrol import SparkControl
from spotifyapi import SpotifyRequests
from AmazonS3 import AmazonS3
from Menu import Menu

def main():
     sc = SparkControl() # comment out when testing in VSCode
     sr = SpotifyRequests() 

     print(sr.get_playlist_tracks("37i9dQZF1EQpgT26jgbgRI"))     #example of the repsonse from an api call
     AmazonS3().upload()
     print("Test file uploaded")

     Menu.main_menu()

if __name__ == '__main__':
     main()