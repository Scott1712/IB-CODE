#19/03/26


class SongNode:
    def __init__(self,title,artist,date): #Create node
        self.title = title
        self.artist = artist
        self.date = date
        self.prev = None
        self.next = None

class Playlist():

    def __init__(self): #When linked list is created
        self.head = None
        self.tail = None
        self.current = None

    def add_songs(self,title,artist,date):
        node = SongNode(title,artist,date) #Create a node
        if not self.head: #If the playlist is currently empty
            self.head = node
            self.tail = node
            self.current = node
        else:
            node.prev = self.tail #Connect current node to previous
            self.tail.next = node #Connect previous node to current
            self.tail = node      #Change the 'tail'

    def show_current(self):
        if self.current: #If there is a song in the playlist
            print("Now playing",self.current.title,"by",self.current.artist)
        else:
            print("ERROR -> No songs in playlist")

    def next_track(self):
        if self.current and self.current.next: #If there is another song
            self.current = self.current.next
        else:
            print("ERROR -> No more songs in playlist")

    def prev_track(self):
        if self.current and self.current.prev: #If you're not on the first song
            self.current = self.current.prev
        else:
            print("ERROR -> You are on first song")





my_vibe = Playlist() #Create object, my_vibe is a list, type Playlist()

stop = False

print("This is a playlist creator, where you can add and play songs from your playlist")
while stop != True:
    choice = 0
    while choice < 1 or choice > 5:
        try:
            print("")
            print("What do you want to do?")
            print("1. Add song")
            print("2. Play song")
            print("3. Go to next song")
            print("4. Go to previous song")
            print("5. Quit")
            choice = int(input("    -> "))
            if choice < 1 or choice > 5:
                print("Please enter a valid number")
        except TypeError:
            print("Please enter an integer")

    if choice == 1:
        title = str(input("Enter song title: "))
        artist = str(input("Enter song artist: "))
        date = int(input("Enter song date: "))
        my_vibe.add_songs(title,artist,date)
        print(title,"added")

    if choice == 2:
        my_vibe.show_current()

    if choice == 3:
        my_vibe.next_track()
        my_vibe.show_current()

    if choice == 4:
        my_vibe.prev_track()
        my_vibe.show_current()

    if choice == 5:
        stop = True









my_vibe.add_songs("Back to Black","Amy Winehouse",2007) #Create node
my_vibe.add_songs("Losing My Religion","R.E.M.",1991) #Create node
my_vibe.add_songs("Hotel California","Eagles",1976) #Create node

my_vibe.show_current() #Play the head node

my_vibe.next_track() #Go to next node
my_vibe.show_current()

my_vibe.next_track()
my_vibe.show_current()

my_vibe.prev_track() #Go to previous node
my_vibe.show_current()


