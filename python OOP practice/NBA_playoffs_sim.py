#AXPV
import random
# Create team class
class Team:
    def __init__(self, teamName, teamStrength, teamConf):
        self.teamName = teamName
        self.teamStrength = teamStrength
        self.teamConf = teamConf

# Create Game Class
class Game:
    def __init__(self):
        # Score
        pass

#Create series class
class Series:
    def __init__(self):
        pass
#Create Bracket class
class Bracket:
    def __init__(self):
        pass
#Initialize 8 teams per conference

east_teams = [
    Team("Cleveland Cavaliers", 95, "east"),
    Team("New York Knicks", 94, "east"),
    Team("Boston Celtics", 97, "east"),
    Team("Milwaukee Bucks", 93, "east"),
    Team("Indiana Pacers", 88, "east"),
    Team("Detroit Pistons", 85, "east"),
    Team("Orlando Magic", 85, "east"),
    Team("Atlanta Hawks", 89, "east")
]

west_teams = [
    Team("Oklahoma City Thunder", 90, "west"),
    Team("Denver Nuggets", 97, "west"),
    Team("Los Angeles Lakers", 98, "west"),
    Team("Golden State Warriors", 97, "west"),
    Team("Houston Rockets", 90, "west"),
    Team("Los Angeles Clippers", 92, "west"),
    Team("Memphis Grizzlies", 92, "west"),
    Team("Minnesota Timberwolves", 93, "west")
]