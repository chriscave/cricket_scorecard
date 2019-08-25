#!/usr/bin/env python
class Innings:
    def __init__(self, batting, bowling):
        """

        :param batting: is a Team class
        :param bowling: is another Team class
        """
        self.batting = Team(batting)
        self.bowling = Team(bowling)
        self.balls = 0
        self.extras = 0

    def overs(self):
        return int(self.balls / 6) + ((self.balls % 6) / 10)

    def innings_score(self):
        return print(self.batting.score())

    def ball(self,ball, bowler,batsman):
        if type(ball) == str:
            if ball == "W":
                pass

            elif ball == "w" or ball == "nb":
                pass

            elif ball == "lb" or ball == "b":
                pass

        else:
            self.balls += 1

            batsman.balls_faced += 1
            batsman.bts_runs += ball
            batsman._team.runs += ball

            bowler.balls += 1
            bowler.runs_against += ball






class Team:
    def __init__(self,team):
        self.team = team
        self.runs = 0
        self.wickets = 0
    def score(self):
        return print(self.team + ": %2d-%1d" %(self.runs,self.wickets))

class Batter:
    def __init__(self, team, name):
        self._team = team
        self.name = name
        self.bts_runs = 0
        self.balls_faced = 0
        self.out = ""

class Bowler:
    def __init__(self, team, name):
        self._team = team
        self.name = name
        self.balls = 0
        self.wickets = 0
        self.maidens = 0
        self.runs_against = 0
        self.bwl_extras = 0

    def overs(self):
        return int(self.balls / 6) + ((self.balls % 6) / 10)


inn1 = Innings("eng","aus")
strauss = Batter(inn1.batting,"strauss")
lee = Bowler(inn1.bowling,"lee")
inn1.ball(2,lee,strauss)
inn1.innings_score()
print(inn1.batting.runs)
print(inn1.balls)
print(lee.overs())
