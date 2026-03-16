#11/12/25

players = []

class player:
    def __init__(self,name,nationality,age):
        self.name = name
        self.nationality = nationality
        self.age = age
        print("")
        print("   ->",self.name,"added")
        print("")

    def show_info(self):
        print(f"{self.name} is {self.nationality} and is {self.age} years old")

    def get_name(self):
        return self.name

class goalkeeper(player):
    def __init__(self,name,nationality,age,cleanSheets,saves):
        super().__init__(name,nationality,age)
        self.cleanSheets = cleanSheets
        self.saves = saves

    def show_stats(self):
        print(f"{self.name} has {self.saves} saves and {self.cleanSheets} clean sheets")

class defender(player):
    def __init__(self,name,nationality,age,cleanSheets,tackles):
        super().__init__(name,nationality,age)
        self.cleanSheets = cleanSheets
        self.tackles = tackles

    def show_stats(self):
        print(f"{self.name} has {self.tackles} tackles and {self.cleanSheets} clean sheets")

class midfielder(player):
    def __init__(self,name,nationality,age,assists,goals):
        super().__init__(name,nationality,age)
        self.assists = assists
        self.goals = goals

    def show_stats(self):
        print(f"{self.name} has {self.goals} goals and {self.assists} assists")

class attacker(player):
    def __init__(self,name,nationality,age,assists,goals):
        super().__init__(name,nationality,age)
        self.assists = assists
        self.goals = goals

    def show_stats(self):
        print(f"{self.name} has {self.goals} goals and {self.assists} assists")

def menu():
    answer = 0
    while answer < 1 or answer > 4:
        print("")
        print("What do you want to do?")
        print(" 1. See a player's information")
        print(" 2. See a player's statistics")
        print(" 3. Create a player")
        print(" 4. Quit")
        try:
            answer = int(input("     -> "))
            while answer < 0 or answer > 4:
                print("Enter a valid number please")
                answer = int(input("     -> "))
        except ValueError:
            print("Enter a number please")
    if answer == 1:
        playerInfo()
    if answer == 2:
        playerStats()
    if answer == 3:
        createPlayer()
    if answer == 4:
        global go
        go = False

def playerInfo():
    global players

    print("")
    if len(players)==0:
        print("No players have been added yet")
    else:
        answer = 0
        while answer < 1 or answer > len(players)+1:
            print("")
            print("Which player's information do you want?")
            for i in range(0,len(players)):
                print(" "+str(i+1)+".",players[i].get_name())
            print(" "+str(len(players)+1)+".","Go Back")
            try:
                answer = int(input("     -> "))
                while answer < 0 or answer > len(players)+1:
                    print("Enter a valid number please")
                    answer = int(input("     -> "))
            except ValueError:
                print("Enter a number please")
        if answer != len(players)+1:
            print("")
            players[answer-1].show_info()

def playerStats():
    global players

    print("")
    if len(players)==0:
        print("No players have been added yet")
    else:
        answer = 0
        while answer < 1 or answer > len(players)+1:
            print("")
            print("Which player's statistics do you want?")
            for i in range(0,len(players)):
                print(" "+str(i+1)+".",players[i].get_name())
            print(" "+str(len(players)+1)+".","Go Back")
            try:
                answer = int(input("     -> "))
                while answer < 0 or answer > len(players)+1:
                    print("Enter a valid number please")
                    answer = int(input("     -> "))
            except ValueError:
                print("Enter a number please")
        if answer != len(players)+1:
            print("")
            players[answer-1].show_stats()


def createPlayer():
    answer = 0
    while answer < 1 or answer > 5:
        print("")
        print("What position does the player play?")
        print(" 1. Attacker")
        print(" 2. Midfielder")
        print(" 3. Defender")
        print(" 4. Goalkeeper")
        print(" 5. Go Back")
        try:
            answer = int(input("     -> "))
            while answer < 0 or answer > 5:
                print("Enter a valid number please")
                answer = int(input("     -> "))
        except ValueError:
            print("Enter a number please")
    if answer != 5:
        print("")
        print("What is the name of the player?")
        playerName = input("     -> ")
        print("")
        print("What is the nationality of the player?")
        playerNation = input("     -> ")
        print("")
        print("What is the age of the player?")
        playerAge = int(input("     -> "))

        stat1 = 0
        stat2 = 0

        if answer == 1 or answer == 2:
            print("")
            print("How many assists does the player have?")
            stat1 = int(input("     -> "))
            print("")
            print("How many goals does the player have?")
            stat2 = int(input("     -> "))
        if answer == 3 or answer == 4:
            print("")
            print("How many clean sheets does the player have?")
            stat1 = int(input("     -> "))
            if answer == 3:
                print("")
                print("How many tackles does the player have?")
                stat2 = int(input("     -> "))
            if answer == 4:
                print("")
                print("How many saves does the player have?")
                stat2 = int(input("     -> "))

        if answer == 1:
            playerName = attacker(playerName,playerNation,playerAge,stat1,stat2)
        if answer == 2:
            playerName = midfielder(playerName,playerNation,playerAge,stat1,stat2)
        if answer == 3:
            playerName = defender(playerName,playerNation,playerAge,stat1,stat2)
        if answer == 4:
            playerName = goalkeeper(playerName,playerNation,playerAge,stat1,stat2)
        if answer < 5 and answer > 0:
            players.append(playerName)


go = True

print("This is an OOP program that holds statistics and information for any footballer you want")
print("You can add players of any position and add their stats and info")
print("Then you can display any of this from any player you want")

while go:
    menu()
