"""
--- Day 2: Rock Paper Scissors ---

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, 
a giant Rock Paper Scissors tournament is already in progress.
Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the 
players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for 
that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both 
players choose the same shape, the round instead ends in a draw.
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) 
that they say will be sure to help you win. "The first column is what your opponent is going to play: A 
for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help 
with someone's tent.
The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z 
for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.
The winner of the whole tournament is the player with the highest score. Your total score is the sum of 
your scores for each round. The score for a single round is the score for the shape you selected (1 for 
Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if 
the round was a draw, and 6 if you won).
Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you 
would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in 
    a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends 
    in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

Your puzzle answer was 8890.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how 
the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means 
you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the 
round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you 
    also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score 
    of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly 
according to your strategy guide?

"""

class Game:

    # inputs list
    __inputs_list = []


    # read inputs from the file and append them to the list
    @classmethod
    def read_inputs(cls, file):
        with open(file, "r") as f:
            lines = f.read()
            for line in lines.split("\n"):
                Game.__inputs_list.append(line)

    
    # diplay inputs list
    def display_inputs_list(self):
        return Game.__inputs_list

    
    # shape score
    def shape_score(self, shape):
        scores_dict = {
            "X": 1,
            "Y": 2,
            "Z": 3
        }
        return scores_dict[shape]

    
    # win-lose count score
    def outcome_score(self, player1_inp, player2_inp):
        outcome = 0
        
        if player1_inp == "A":
            if player2_inp == "X":
                outcome = 3
            elif player2_inp == "Y":
                outcome = 6
        
        elif player1_inp == "B":
            if player2_inp == "Y":
                outcome = 3
            elif player2_inp == "Z":
                outcome = 6
        
        elif player1_inp == "C":
            if player2_inp == "Z":
                outcome = 3
            elif player2_inp == "X":
                outcome = 6
        
        return outcome

    
    # top secret strategy guide
    def top_secret_strategy(self, player1_inp, player2_inp):
        outcome = 0
        score = 0

        if player2_inp == "X":
            if player1_inp == "A":
                score = 3 + outcome
            elif player1_inp == "B":
                score = 1 + outcome
            else:
                score = 2 + outcome
        
        elif player2_inp == "Y":    
            outcome = 3
            if player1_inp == "A":
                score = 1 + outcome
            elif player1_inp == "B":
                score = 2 + outcome
            else:
                score = 3 + outcome
        
        elif player2_inp == "Z":
            outcome = 6
            if player1_inp == "A":
                score = 2 + outcome
            elif player1_inp == "B":
                score = 3 + outcome
            else:
                score = 1 + outcome
        
        return score

    
    # total score count
    def total_score(self):
        total = 0
        top_secret_total = 0
        game_rounds = Game.__inputs_list
        for round in game_rounds:
            player_1 = round.split(" ")[0]
            player_2 = round.split(" ")[1]
            total += self.shape_score(player_2) + self.outcome_score(player_1, player_2)
            top_secret_total += self.top_secret_strategy(player_1, player_2)
        return f"You scored {total} points in this game\nYours's top secret strategy score is {top_secret_total}"


start_game = Game()
start_game.read_inputs("day-2-input.txt")
print(start_game.total_score())