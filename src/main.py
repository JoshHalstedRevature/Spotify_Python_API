#program to ..
#Python 2.7.5 in HortonWorks
from sparkcontrol import SparkControl
from spotifyapi import SpotifyRequests

def main():
     sc = SparkControl() # comment out when testing in VSCode
     SpotifyRequests().passing_credentials()

if __name__ == '__main__':
     main()