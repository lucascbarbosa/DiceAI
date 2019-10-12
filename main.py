from random import randint

class Player():
    
    def __init__(self,current_round, dices,points,round_score,limit):
        self.current_round = current_round
        self.dices = dices
        self.points = points
        self.round_score = round_score
        self.limit = limit
        self.rolls = []

    def rolls_count(self,rolls):
        counts = []
        for i in range(1,7):
            counts.append(rolls.count(i))
        return counts

    def roll(self):
        self.rolls = []
        for i in range(self.dices):
            self.rolls.append(randint(1,6))

        print(self.rolls)
        bust = True
        counts = self.rolls_count(self.rolls)
        for count in counts:
            if count < 3:
                pass
            else:
                bust = False
        if counts[4] != 0 and counts[0] != 0:
            bust = False

        if bust:
            self.round_score = 0
            print("You busted!\n")
        else:
            self.select()
            
    def select(self):
        selections = []
        selections = input('Select the index of the dices you want to score, comma separated: ').split(',')
        if len(selections) == 0:
            self.points += self.round_score
        self.dices -= len(selections)
        selections = list(map(int,selections))
        print('Selected: ', end=" ", flush=True)
        for sel in selections:
            print(str(self.rolls[sel-1])+',', end=" ", flush=True)
        print('\n')
        new_rolls = []
        for sel in selections:
            new_rolls.append(self.rolls[sel-1])
        counts = self.rolls_count(new_rolls)
        self.score(counts)   
            

    def score(self,counts):
        score = 0    
        ones = counts[0]
        fives = counts[4]
        #handle the case for the one
        if ones % 3 == 0:
            score += (ones/3)*1000
        else:
            rest = ones % 3
            score += rest*100 + (ones - rest)/3*1000
        #handle the other cases
        
        for i in range(1,6):
            count = counts[i]
            if count >= 3:
                score+= (i+1)*(count-2)*100
            elif i == 4:#in the case of the five, where you get 50 points per dice
                score += count*50
        if score == 0:
            print('No points made. Select other dices. \n')
            self.select()

        self.round_score += score
    
        print("Player's round: %d\n"%(self.round_score))
        print("Player's total score: %d\n"%(self.points))

        Pass = input('You wanna pass(y/n)?\n')
        
        if Pass == 'y':
            self.points += self.round_score
            self.dices = 6
            print("Player's total score: %d"%(self.points))
            self.round_score = 0
        else:
            self.roll()
    
    def win(self):
        return self.points >= self.limit
       
def main():
    option = int(input("Welcome to dice AI. Type [1] to rules, [2] to play with another one and [3] to play against AI.\n"))

    if option == 1:
        print("\n\nRules: \n")

    if option == 2:
        print('\n\nPvP\n')
        player1 = Player(0,6,0,0,1000)
        player2 = Player(0,6,0,0,1000)
        while not player1.win() and not player2.win():
            print("Player 1's round")
            player1.roll()
            print("Player 2's round")
            player2.roll()    

    if option == 3:
        print("PvAI\n")

if __name__ == "__main__":
    main()