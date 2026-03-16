import random

import time

from colorama import init,Fore,Back,Style

points = 0

def linesmall():
    print("-----------------")

def linemed():
    print("--------------------------------")

def linelong():
    print("-------------------------------------------------")



print(Style.RESET_ALL + "")
print(Back.RED + "     _________     ")
print("  ,-'    |    '-,  ")
print(" /-,     |     ,-\\ ")
print("|   \\    |    /   |")
print("|    |   |   |    |")
print("|----|---|---|----|")
print("|    |   |   |    |")
print("|   /    |    \\   |")
print(" \\-'     |     '-/ ")
print("  '-,_________,-'  ")
print("")


print(Style.RESET_ALL + "")
print("Enter your players name.")
linelong()
playername = input()

linelong()
print("Enter your players position: ")
print("1. PG")
print("2. SG")
print("3. SF")
print("4. PF")
print("5. C")
positioninput = int(input("-> "))

positions = ["PG","SG","SF","PF","C"]
position = positions[positioninput-1]

homeaway = [["Home:","|", "Away:"]]



linelong()
print("Please choose overall. (70-99)")
rating = int(input("-> "))


ovran = 4

randomness = 0
for i in range(0,ovran):
    randomness += (random.randint(-7,7))
points = int((rating-68)+(randomness/ovran))
averagepoints = int(rating-68)

randomness = 0
for i in range(0,ovran):
    randomness += (random.randint(-3,3))
rebounds = int((positioninput * 2 + 4)*((rating - 66)/33)+(randomness/ovran))
averagerebounds = int((positioninput * 2 + 4)*((rating - 66)/33))

randomness = 0
for i in range(0,ovran):
    randomness += (random.randint(-2,2))
if position == "PG":
    assists = int(12*((rating-66)/33)+(randomness/ovran))
    averageassists = int(12*((rating-66)/33))
if position == "SG":
    assists = int(10*((rating-66)/33)+(randomness/ovran))
    averageassists = int(10*((rating-66)/33))
if positioninput>2:
    assists = int((11-positioninput)*((rating-66)/33)+(randomness/ovran))
    averageassists = int((11-positioninput)*((rating-66)/33))

average = averagepoints + averagerebounds + averageassists

def regSeason():

    predict = 4 #Higher -> More Predictable

    games = 82
    totalpoints = 0
    totalrebounds = 0
    totalassists = 0
    totalwins = 0

    totalTDB = 0
    highpts = 0
    highast = 0
    highreb= 0


    aid = int((rating-70)/2-7.5)


    for i in range(0,games):
        overallpts = 0
        overallreb = 0
        overallast = 0
        overallopponent = 0
        overallplayers = 0
        for n in range(0,predict):
            overallpts += random.randint(0, points * 2)
            overallreb += random.randint(0, rebounds * 2)
            overallast += random.randint(0, assists * 2)
            overallplayers += random.randint(74-average+aid,154-average+aid)
            overallopponent += random.randint(74, 154)
        linelong()
        homeScore = int(overallplayers/predict+overallpts/predict+overallreb/predict+overallast/predict)
        awayScore = int(overallopponent/predict)

        if homeScore==awayScore:
            Kobe = random.randint(1,2)
            if Kobe == 1:
                homeScore += 1
            else:
                awayScore += 1

        if homeScore>awayScore:
            totalwins += 1
            print("You:",Fore.GREEN + str(homeScore),Style.RESET_ALL + "|","Them:", Fore.RED + str(awayScore), Style.RESET_ALL + "| Record:",str(totalwins)+"-"+str((i+1)-totalwins))
        else:
            print("You:",Fore.RED + str(homeScore),Style.RESET_ALL + "|","Them:", Fore.GREEN + str(awayScore), Style.RESET_ALL + "| Record:",str(totalwins)+"-"+str((i+1)-totalwins))
        print("PTS:", int(overallpts/predict), "|", "REB:", int(overallreb/predict), "|", "AST:", int(overallast/predict))
        lebron = input()

        if int(overallpts/predict) > highpts:
            highpts = int(overallpts/predict)
        if int(overallreb/predict) > highreb:
            highreb = int(overallreb/predict)
        if int(overallast/predict) > highast:
            highast = int(overallast/predict)
        if int(overallpts/predict) > 9 and int(overallreb/predict) > 9 and int(overallast/predict) > 9:
            totalTDB += 1

        totalpoints = totalpoints + int(overallpts/predict)
        totalrebounds = totalrebounds + int(overallreb/predict)
        totalassists = totalassists + int(overallast/predict)

    PPG = int(totalpoints/games)

    RPG = int(totalrebounds/games)

    APG = int(totalassists/games)

    linelong()

    time.sleep(0.5)
    print("")
    print("Team Record ->  ",str(totalwins)+"-"+str(82-totalwins))
    time.sleep(0.2)
    linemed()
    print("Stat Averages")
    time.sleep(0.1)
    print("PTS:", PPG,"|", "REB:", RPG, "|", "AST:", APG)
    time.sleep(0.2)
    linemed()
    print("Game Highs:")
    time.sleep(0.1)
    print("PTS:", highpts,"|", "REB:", highreb, "|", "AST:", highast)
    time.sleep(0.2)
    linemed()
    print("Triple Doubles:",totalTDB)

    return totalwins

def playoffs():

    rounds = ["1st Round","Conference Semis","Conference Finals","NBA Finals","Champions"]

    time.sleep(1)
    print("")
    print("You made the playoffs!")
    lebron = input()
    advance = True

    seriesLost = 0

    played = 0

    totalpoints = 0
    totalrebounds = 0
    totalassists = 0
    totalwins = 0

    totalTDB = 0
    highpts = 0
    highast = 0
    highreb= 0

    predict = 4 #Higher -> More Predictable
    aid = int((rating-70)/2-7.5)



    for i in range(0,4):

        if advance == True:

            wins = 0
            otherwins = 0

            print("")
            print("")
            print("")
            print("You advanced to the",rounds[i])
            time.sleep(0.3)
            lebron = input()

            while wins != 4 and otherwins != 4:

                played += 1
                print("")
                print("")
                print("Game",wins+otherwins+1,"-",rounds[i],"     Series ->",wins,"-",otherwins)
                linelong()
                lebron = input()


                overallpts = 0
                overallreb = 0
                overallast = 0
                overallopponent = 0
                overallplayers = 0
                for n in range(0,predict):
                    overallpts += random.randint(0, points * 2)
                    overallreb += random.randint(0, rebounds * 2)
                    overallast += random.randint(0, assists * 2)
                    overallplayers += random.randint(74-average+aid,154-average+aid)
                    overallopponent += random.randint(74, 154)
                homeScore = int(overallplayers/predict+overallpts/predict+overallreb/predict+overallast/predict)
                awayScore = int(overallopponent/predict)

                if homeScore==awayScore:
                    Kobe = random.randint(1,2)
                    if Kobe == 1:
                        homeScore += 1
                    else:
                        awayScore += 1

                if homeScore>awayScore:
                    wins += 1
                    print("You:",Fore.GREEN + str(homeScore),Style.RESET_ALL + "|","Them:", Fore.RED + str(awayScore), Style.RESET_ALL + "")
                else:
                    otherwins += 1
                    print("You:",Fore.RED + str(homeScore),Style.RESET_ALL + "|","Them:", Fore.GREEN + str(awayScore), Style.RESET_ALL + "")
                linelong()
                print("PTS:", int(overallpts/predict), "|", "REB:", int(overallreb/predict), "|", "AST:", int(overallast/predict))
                lebron = input()
                if int(overallpts/predict) > highpts:
                    highpts = int(overallpts/predict)
                if int(overallreb/predict) > highreb:
                    highreb = int(overallreb/predict)
                if int(overallast/predict) > highast:
                    highast = int(overallast/predict)
                if int(overallpts/predict) > 9 and int(overallreb/predict) > 9 and int(overallast/predict) > 9:
                    totalTDB += 1

                totalpoints = totalpoints + int(overallpts/predict)
                totalrebounds = totalrebounds + int(overallreb/predict)
                totalassists = totalassists + int(overallast/predict)
            time.sleep(0.5)
            print("")
            if otherwins == 4:
                advance = False
                print("You lost the",rounds[i],otherwins,"-",wins)
                seriesLost = i
            else:
                print("You won the",rounds[i],wins,"-",otherwins)
                if i == 3:
                    seriesLost = 4
            time.sleep(1)

    PPG = int(totalpoints/played)

    RPG = int(totalrebounds/played)

    APG = int(totalassists/played)

    time.sleep(0.5)
    print("")
    print("")
    print("")
    print("Playoff Result ->  ",rounds[seriesLost],"("+str(wins)+"-"+str(otherwins)+")")
    time.sleep(0.2)
    linemed()
    print("Stat Averages")
    time.sleep(0.1)
    print("PTS:", PPG,"|", "REB:", RPG, "|", "AST:", APG)
    time.sleep(0.2)
    linemed()
    print("Game Highs:")
    time.sleep(0.1)
    print("PTS:", highpts,"|", "REB:", highreb, "|", "AST:", highast)
    time.sleep(0.2)
    linemed()
    print("Triple Doubles:",totalTDB)



if regSeason() > 40:
    playoffs()
else:
    print("")
    print("You failed to make the playoffs...")


