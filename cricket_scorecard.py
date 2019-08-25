#!/usr/bin/env python
class Match:
    def __init__(self, home, away):
        self.home = Team(home)
        self.away = Team(away)
        self.overs = 0
        self.extras = 0

    def match_score(self):
        return print(self.home.score(), self.away.score())

    def ball(self,ball, bowler,batsman):


class Team:
    def __init__(self,team):
        self.team = team
        self.runs = 0
        self.wickets = 0
    def score(self):
        return print(self.team + ": %2d-%1d" %(self.runs,self.wickets))

class Batter(Team):
    def __init__(self, team, name):
        super().__init__(team)
        self.name = name
        self.bts_runs = 0
        self.balls_faced = 0
        self.out = ""

class Bowler(Team):
    def __init__(self, team, name):
        super().__init__(team)
        self.name = name
        self.overs = 0
        self.wickets = 0
        self.maidens = 0
        self.bwl_extras = 0



mtc1 = Match("eng","aus")
mtc1.match_score()