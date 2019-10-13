from random import randint
import math as m

class Agent(): #Mother class with the methods we will use both in player and ai classes
    
    def __init__(self,current_round, dices,points,round_score,limit):
        self.current_round = current_round
        self.dices = dices
        self.points = points
        self.round_score = round_score
        self.limit = limit
        self.rolls = []
        self.stop = False  
        self.bust = False 
    

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
        self.bust = True
        counts = self.rolls_count(self.rolls)
        for count in counts:
            if count < 3:
                pass
            else:
                self.bust = False
        if counts[4] != 0 or counts[0] != 0:
            self.bust = False

        if self.bust:
            self.round_score = 0
            self.dices = 6
            self.stop = True
            print("You busted!\n")
            print("Player's total score: %d\n\n"%(self.points))


    def win(self):
        return self.points >= self.limit
    
class Player(Agent):
             
    def select(self):
        selections = []
        selections = input('Select the index of the dices you want to score, comma separated: ').split(',')
        print(selections)
        try:
            selections = list(map(int,selections))
            print('Selected: ', end=" ", flush=True)
            for sel in selections:
                print(str(self.rolls[sel-1]), end=" ", flush=True)
            print('\n')
            new_rolls = []
            for sel in selections:
                new_rolls.append(self.rolls[sel-1])
            counts = self.rolls_count(new_rolls)
            self.score(counts)  
        except ValueError:
            print("Please select at least one dice.")
            self.select()
        
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
        self.Pass(counts)

    def Pass(self,counts):

        Pass = input('You wanna pass(y/n)?\n')
        
        if Pass.lower() == 'y':
            self.points += self.round_score
            self.stop = True
            self.dices = 6
            print("Player's total score: %d\n\n"%(self.points))
            self.round_score = 0
        elif Pass.lower() == 'n':
            self.dices -= sum(counts)
            self.roll()
        else:
            print("Error.")
            self.Pass(counts)
   
class AI(Agent):

    def decision(self):
        current_score = 0
        future_score = 0
        counts = self.rolls_count(self.rolls)
        print(counts)
        combos = []
        for count in counts:
            idx = counts.index(count)
            if count >= 3:
                combos.append((idx+1,count))
        print(combos)
        for dice_value,count  in combos:           
            current_score += dice_value*(count-2)*100
        dices = self.dices - (counts[0]+counts[4])#remove all ones and fives
        print(dices)
        for i in range(2,7):
            for j in range(dices):
                if not i == 5:
                    prob = float(1/m.pow(6,(dices-1)))
                    future_score += prob*i*(j-1)*100 #i = dice_value, j = dice_count
        if future_score < current_score: #select all combos

            pass

        
        else: #release all dices 
            pass
               
    
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
            while not player1.stop:
                player1.roll()
                if not player1.bust:
                    print('oi')
                    player1.select()
                print('foo1')
            player1.stop = False
            print("Player 2's round")
            while not player2.stop:
                player2.roll() 
                if not player2.bust:
                    player2.select() 
                print('foo2')                
            player2.stop = False
              

    if option == 3:
        print("PvAI\n")
        player = Player(0,6,0,0,1000)
        ai = AI(0,6,0,0,1000)
        while not player.win() and not ai.win():
            print("Player's round")
            while not player.stop:
                player.roll()
                if not player.bust:
                    player.select()
                print('foo')
            player.stop = False
            print("AI's round")
            while not ai.stop:
                ai.roll()
                if not ai.bust:
                    ai.decision()


if __name__ == "__main__":
    main()