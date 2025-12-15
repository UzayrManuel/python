favourite_games = ['CS2', 'Minecraft', 'Runescape', 'Fortnite', 'PUBG']
favourite_series = ['big bang theory', 'peaky blinders', 'breaking bad']
favourite_artists = ['j cole', 'billie eilish', 'eminem', 'kendrick lamar', 'ariana grande', 'bruno mars']

welcome_message = 'Hi. Welcome to MY FAVS.\nThese are my current lists:'

def show_games():
    for index, game in enumerate(favourite_games, start=1):
        print(index, game)
        

def show_series():    
    for index, series in enumerate(favourite_series, start=1):
        print(index, series.title())
        
def show_artists():    
    for index, artist in enumerate(favourite_artists, start=1):
        print(index, artist.title())
        
def pause():
    back_to_menu = input("Press Enter to return to Menu")
        
while True:
    print(welcome_message)
    list_options = input("1. Uzayr's Favourite Games\n2. Uzayr's Favourite Series\n3. Uzayr's Favourite Artists\n\nChoose a list to view: ")
    if list_options == '1':
        print("\nThese are my favorite games:")
        show_games()
        pause()               
    elif list_options == '2':
        print("These are my favorite series:")
        show_series()
        pause()        
    elif list_options == '3':
        print("These are my favorite artists:")
        show_artists()
        pause()        
    else:
        print("That is not a valid option, please select an option from the list")
        pause()