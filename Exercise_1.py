# Good Guys/Bad Guys
"""
Create three classes, a superclass called “Characters”
that will be defined with the following attributes and methods:
    a. Attributes: name, team, height, weight
    b. Methods: sayHello
The sayHello method should output the statement “Hello, my name is Max and
I'm on the good guys”. The team attribute should be declared to a string of
either “good” or “bad.”. The other two classes, which will be subclasses, will
be “GoodPlayers” and “BadPlayers.” both classes will inherit “Characters” and
super all the attributes that the superclass requires. The subclasses do not need
any other methods or attributes. Instantiate one player on each team, and call
the sayHello method for each. The output should result in the following:

>>> "Hello, my name is Max and I'm on the good guys"
>>> "Hello, my name is Tony and I'm on the bad guys
"""




class Characters():
    def __init__(self, name, team, height, weight):
        self.name = name
        self.team = team
        self.height = height
        self.weight = weight


    def sayHello(self):
        if self.team == 'good':
            team_name = 'good guys'
            print(f'Hello, my name is {self.name} and I\'m on the {team_name}')

        elif self.team == 'bad':
            team_name = 'bad guys'
            print(f'Hello, my name is {self.name} and I\'m on the {team_name}')

class GoodPlayers(Characters):
     pass
      

class BadPlayers(Characters):
    pass
        

Player1 = GoodPlayers('max','good', 6,75)
Player2 = BadPlayers('Tony','bad',5.5,70)

Player1.sayHello()
Player2.sayHello()