#27/11/25

class teams:

    def __init__(self, nickname, stadium):
        self.nickname = nickname
        self.stadium = stadium
        print(self.nickname,"-> Created")
        print("")

    def explain(self):
        print("Team ->",self.nickname)
        print("Stadium ->",self.stadium)
        print("")

arsenal = teams("Gunners","The Emirates")
chelsea = teams("The Blues","Stanford Bridge")
liverpool = teams("The Reds","Anfield")
manCity = teams("Cityzens","Etihad")
manUtd = teams("Red Devils","Old Trafford")
tottenham = teams("Spurs","Tottenham Hotspur Stadium")

x = input("")

arsenal.explain()
chelsea.explain()
liverpool.explain()
manCity.explain()
manUtd.explain()
tottenham.explain()