#AXPV
import random # Factor for generating random winners

# Create Team class
class Team:
    def __init__(self, teamName, teamStrength, teamConf):
        self.teamName = teamName
        self.teamStrength = teamStrength
        self.teamConf = teamConf

# Create Game Class
class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score1 = 0
        self.score2 = 0
        self.winner = None
    # Playing a game, and then determining the winner
    def play_game(self):
        # Base score for an NBA game
        baseScore = random.randint(85, 120)

        # How the scoring works, influenced by randomness and team strength
        self.score1 = baseScore + random.randint(0, 10) + (self.team1.teamStrength // 10)
        self.score2 = baseScore + random.randint(0, 10) + (self.team2.teamStrength // 10)
        print(f"Final score: {self.team1.teamName} {self.score1} - {self.team2.teamName} {self.score2}")
        print("-------------------------------------------------------------------------------------------")
        

        if self.score1 > self.score2:
            self.winner = self.team1
            print(f"The winner is {self.winner.teamName}")
        elif self.score1 < self.score2:
            self.winner = self.team2
            print(f"The winner is {self.winner.teamName}")
        else:
            print("The game is a tie. Replaying...")
            self.play_game()
        
        return self.winner

#Create series class
class Series:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.wins1 = 0
        self.wins2 = 0
        self.game_num = 0  # Fixed: Made this an instance variable
    # For determining the winner of a series
    def play_series(self):
        # Games continue until one team reaches 4 wins
        while self.wins1 < 4 and self.wins2 < 4:
            game = Game(self.team1, self.team2)
            winner = game.play_game()
            self.game_num += 1

            print(f"Game {self.game_num} score: \n{self.team1.teamName}: {game.score1} - {self.team2.teamName}: {game.score2}")

            # Increment wins of winning teams per game played
            if winner == self.team1:
                self.wins1 += 1
            else:
                self.wins2 += 1
        print(f"Starting series: {self.team1.teamName, self.team2.teamName}")
                
        # Printing the series winner (first to 4 wins)
        if self.wins1 == 4:
            print(f"The winner for this round is the {self.team1.teamName} with a series score of {self.wins1} - {self.wins2}")
            return self.team1
        else:
            print(f"The winner for this round is the {self.team2.teamName} with a series score of {self.wins2} - {self.wins1}")
            return self.team2

#Create Bracket class
# FR = First Round
# CS = conference semifinals = second round
# Matchups (Seeding) (1v8, 2v7, 3v6, 4v5)
class Bracket:
    def __init__(self, east_teams, west_teams):
        self.east_teams = east_teams
        self.west_teams = west_teams
        self.east_FR_winners = []
        self.west_FR_winners = []
        self.east_CS_winners = []
        self.west_CS_winners = []
        self.east_conference_champ = []
        self.west_conference_champ = []
        self.NBA_champion = None

    def play_first_round(self):
        print("EASTERN CONFERENCE FIRST ROUND \n")
        
        series_matchups = ([0,7], (1,6), (2,5), (3,4))
        for seed1, seed2 in series_matchups:
            # Made an instance of the series class which includes the arrays of east and west teams
            first_round_east = Series(self.east_teams[seed1], self.east_teams[seed2])
            winner_east_first_round = first_round_east.play_series()
            self.east_FR_winners.append(winner_east_first_round)

        print("WESTERN CONFERENCE FIRST ROUND\n")
        for seed1, seed2 in series_matchups:
            first_round_west = Series(self.west_teams[seed1], self.west_teams[seed2])
            winner_west_first_round = first_round_west.play_series()
            self.west_FR_winners.append(winner_west_first_round)            

# For second round, get winners of first round
    def play_second_round(self):
        print("EASTERN CONFERENCE SECOND ROUND")
        # winner of first  round 1v8 and 4v5
        second_round_east1 = Series(self.east_FR_winners[0], self.east_FR_winners[3])
        winner_east_second_round1 = second_round_east1.play_series()
        self.east_CS_winners.append(winner_east_second_round1)

        # winner of first round 2v7 and 3v6
        second_round_east2 = Series(self.east_FR_winners[1], self.east_FR_winners[2])
        winner_east_second_round2 = second_round_east2.play_series()
        self.east_CS_winners.append(winner_east_second_round2)

        print("WESTERN CONFERENCE SECOND ROUND\n")
        # winner of first  round 1v8 and 4v5
        second_round_west1 = Series(self.west_FR_winners[0], self.west_FR_winners[3])
        winner_west_second_round1 = second_round_west1.play_series()
        self.west_CS_winners.append(winner_west_second_round1)

        # winner of first round 2v7 and 3v6
        second_round_west2 = Series(self.west_FR_winners[1], self.west_FR_winners[2])
        winner_west_second_round2 = second_round_west2.play_series()
        self.west_CS_winners.append(winner_west_second_round1)


# conference finals
    def play_conference_finals(self):
        print  ("EASTERN CONFERENCE FINALS")

        conference_finals_east = Series(self.east_CS_winners[0], self.east_CS_winners[1])
        winner_ecf = conference_finals_east.play_series()
        self.east_conference_champ = winner_ecf

        print ("WESTERN CONFERENCE FINALS")
     
        conference_finals_west = Series(self.west_CS_winners[0], self.west_CS_winners[1])
        winner_wcf = conference_finals_west.play_series()
        self.west_conference_champ = winner_wcf

# nba finals

    def play_nba_finals(self):
        print ("NBA FINALS")
        nba_finals = Series(self.west_conference_champ, self.east_conference_champ)
        nba_champ = nba_finals.play_series()
        self.NBA_champion = nba_champ
        print(f"The {self.NBA_champion.teamName} is the NBA Champion!")

            

            


# Pick eight Eastern Conference Teams
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

#Pick eight Western Conference teams
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


playoff_sim = Bracket(east_teams, west_teams)


# Then call these methods in order to simulate the entire playoffs:
playoff_sim.play_first_round()
playoff_sim.play_second_round()
playoff_sim.play_conference_finals()
playoff_sim.play_nba_finals()