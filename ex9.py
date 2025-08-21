import random

class Rock_paper_scissor():
    def __init__(self, rounds):
        self.rounds = int(rounds)
        self.current = 0
        self.wins_p1 = 0
        self.wins_ai = 0
        self.choice = ['rock', 'paper', 'scissor']

    def computer(self):
        return random.choice(self.choice)

    def nguoi_thang(self, player_choice, computer):
        if player_choice == computer:
            return 'draw'
        elif player_choice == computer:
            self.current += 1
            print(f"Hoa!")
        elif (player_choice == 'rock' and computer == 'paper') or (player_choice == 'paper' and computer == 'scissor'):
            self.wins_ai += 1
            print(f"Computer won!")
        elif (player_choice == "rock" and computer == 'scissor') or (player_choice == "scissor" and computer == 'paper'):
            self.wins_p1 += 1
            print(f"You won!")

    def game(self):
        if self.wins_p1 > self.rounds // 2:
            return True, 'PLayer'
        elif self.wins_ai > self.rounds // 2:
            return True, 'AI'
        elif self.current >= self.rounds:
            if self.wins_p1 > self.wins_ai:
                return True, 'Player'
            if self.wins_ai > self.wins_p1:
                return True, 'AI'
            else:
                return True, 'Draw'
        else:
            return False, None
    def play(self, player_choice):
        self.rounds += 1
        ai = self.computer()
        winner = self.nguoi_thang(player_choice, ai)
        return ai, winner

if __name__ == '__main__':
    game = Rock_paper_scissor(5)
    while True:
        player_input = input("Rock, Paper, hay Scissor?: ").lower()
        try:
            ai, winner = game.play(player_input)
        except ValueError as e:
            print(e)
            continue
        print(f"Computer chon: {ai}")
        if winner == 'draw':
            print(f"Draw")
        else:
            print(f"Nguoi thang: {winner}")
        over, champion = game.game()
        if over:
            if champion == 'draw':
                print(f"Draw!")
            else:
                print(f"Nguoi thang: {champion}")
            break




