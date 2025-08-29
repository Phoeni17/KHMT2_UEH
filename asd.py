import random
import KBB as tk
from KBB import *

class Rock_paper_scissors:
    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0

    def computer_choice(self):
        return random.choice(['Kéo', 'Búa', 'Bao'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'Hòa'
        else:
            if user_choice == 'Kéo':
                if computer_choice == 'Bao':
                    self.user_wins += 1
                    return 'Bạn thắng'
                else:
                    self.computer_wins += 1
                    return 'Máy tính thắng'
            elif user_choice == 'Búa':
                if computer_choice == 'Kéo':
                    self.user_wins += 1
                    return 'Bạn thắng'
                else:
                    self.computer_wins += 1
                    return 'Máy tính thắng'
            elif user_choice == 'Bao':
                if computer_choice == 'Búa':
                    self.user_wins += 1
                    return 'Bạn thắng'
                else:
                    self.computer_wins += 1
                    return 'Máy tính thắng'

    def check_game_winner(self):
        if self.user_wins > self.total_rounds // 2:
            return 'Bạn đã thắng cả trò chơi!'
        elif self.computer_wins > self.total_rounds // 2:
            return 'Máy tính đã thắng cả trò chơi!'
        elif self.current_round >= self.total_rounds:
            if self.user_wins > self.computer_wins:
                return 'Bạn đã thắng cả trò chơi!'
            elif self.computer_wins > self.user_wins:
                return 'Máy tính đã thắng cả trò chơi!'
            else:
                return 'Trò chơi hòa!'
        else:
            return None

game = None

def start_game():
    global game
    rounds = entry_rounds.get()
    game = Rock_paper_scissors(int(rounds))
    label_status.config(text=f"Trò chơi bắt đầu với {rounds} vòng. Chọn Kéo, Búa hoặc Bao để chơi!", fg="black")
    entry_rounds.config(state=tk.DISABLED)
    btn_start.config(state=tk.DISABLED)
    label_result.config(text="")
    label_score.config(text=f"Điểm bạn: 0 - Máy tính: 0 | Vòng: 0/{game.total_rounds}")

def play(user_choice):
    if game is None:
        label_status.config(text="Vui lòng bắt đầu trò chơi trước.", fg="red")
        return
    if game.current_round >= game.total_rounds:
        label_status.config(text="Trò chơi đã kết thúc. Nhấn bắt đầu để chơi lại.", fg="red")
        return

    computer_choice = game.computer_choice()
    game.current_round += 1
    result = game.determine_winner(user_choice, computer_choice)

    label_result.config(text=f"Máy tính chọn: {computer_choice}\nKết quả vòng: {result}")
    label_score.config(
        text=f"Điểm bạn: {game.user_wins} - Máy tính: {game.computer_wins} | Vòng: {game.current_round}/{game.total_rounds}")

    winner = game.check_game_winner()
    if winner:
        label_status.config(text=winner, fg="blue")
        entry_rounds.config(state=tk.NORMAL)
        btn_start.config(state=tk.NORMAL)
    else:
        label_status.config(text="Chọn tiếp Kéo, Búa hoặc Bao để chơi vòng tiếp theo.", fg="black")


root = tk.Tk ()
root.title("Oẳn Tù Tì - Đơn giản :3")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)
label_rounds = tk.Label(frame_top, text="Nhập số vòng chơi:")
label_rounds.pack(side=tk.LEFT)
entry_rounds = tk.Entry(frame_top, width=5)  # Đây là ô nhập số vòng
entry_rounds.pack(side=tk.LEFT, padx=5)
btn_start = tk.Button(frame_top, text="Bắt đầu", command=start_game)
btn_start.pack(side=tk.LEFT)

label_status = tk.Label(root, text="", fg="red")
label_status.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_rock = tk.Button(frame_buttons, text='✌️ Kéo', width=10, command=lambda: play('Kéo'))
btn_paper = tk.Button(frame_buttons, text='✊ Búa', width=10, command=lambda: play('Búa'))
btn_scissors = tk.Button(frame_buttons, text='🖐 Bao', width=10, command=lambda: play('Bao'))

btn_rock.pack(side=tk.LEFT, padx=5)
btn_paper.pack(side=tk.LEFT, padx=5)
btn_scissors.pack(side=tk.LEFT, padx=5)

label_result = tk.Label(root, text="", font=("Arial", 14), fg="blue")
label_result.pack(pady=5)

label_score = tk.Label(root, text="", font=("Arial", 12))
label_score.pack()

root.mainloop()