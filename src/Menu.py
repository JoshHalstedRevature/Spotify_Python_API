
class Menu:
    """"""
    def historical_newest_choice(self, SpotifyRequestHandler):
        """"""
        choice = input("Would you like to use (h)istorical data or (n)ewest data?").lower()
    
        if choice != 'h'|'n':
            print("Invalid entry!!!")
            return self.historical_newest_choice(SpotifyRequestHandler)
        
        if choice == 'h':
            self.historical_path_choice(SpotifyRequestHandler)
        elif choice == 'n':
            self.newest_path_choice(SpotifyRequestHandler)

    def historical_path_choice(self, SpotifyRequestHandler):
        """"""
        choice = int(input("""
                            What would you like to see?
                            
                            1: What tracks are most popular amongst Spotify users?
                            2: How many tracks gained popularity over 90 out of 100?
                            3: Which tracks released in March 2020 gained popularity over 80?
                            4: Is there a correlation between popularity and a track's traits?
                            5: How long should an average track last according to today's standards?
                            6: What is the correlation between tracks' different features?
                            7: Who is currently most popular and what genres do they represent?
                            """))

        if choice < 1 or choice > 7:
            print("Invalid entry. Please try again")
            return self.historical_path_choice(SpotifyRequestHandler)
          
    def newest_path_choice(self, SpotifyRequestHandler):
        """"""
        choice = input("""
                        What would you like to do?
                        
                        s: Search for playlist, tracks, artists
                        g: Look at the most popular playlists by genre
                        t: Look at the top artists
                        """).lower()

        if choice != 's'|'g'|'t':
            print("Invalid entry. Please try again")
            return self.newest_path_choice(SpotifyRequestHandler)

        if choice == 's':
            self.search_fillin(SpotifyRequestHandler)
        elif choice == 'g':
            self.genre_choice(SpotifyRequestHandler)
        elif choice == 't':
            self.top_artists(SpotifyRequestHandler)

    def search_fillin(self, SpotifyRequestHandler):
        """"""
        keywords = input("Enter the search terms >>> ")
        searchType = input("Enter the type of search >>> ")
        market = input("Enter markets (blank?) >>> ")
        limit = input("Enter limit (blank?) >>> ")
        offset = input("Enter offset (blank?) >>> ")

        SpotifyRequestHandler.search(
            keywords, searchType, market, limit, offset)

    def genre_choice(self, SpotifyRequestHandler):
        """"""
        pass

    def top_artists(self, SpotifyRequestHandler):
        """"""
        pass

    def main_menu(self, SpotifyRequestHandler):
        """"""
        result = self.historical_newest_choice(SpotifyRequestHandler)
