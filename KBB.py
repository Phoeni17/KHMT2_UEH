from KBB import *
from random import randint
from PIL import Image, ImageTk

class Rock_paper_scissor():
    def __init__(self, root):
        self.root = root
        self.root.title("Keo Bua Bao")
        self.root.geometry("727x600")
        self.root.config(bg="#003773")

        try:
            rock = "/Users/congminh/rock.webp"
            paper = "/Users/congminh/paper.webp"
            scissors = "/Users/congminh/scissor.png"

            rock_im= Image.open(rock).resize((150, 150))
            paper_im = Image.open(paper).resize((150, 150))
            scissors_im = Image.open(scissors).resize((150, 150))

            self.rock_im = ImageTk.PhotoImage(rock_im)
            self.paper_im = ImageTk.PhotoImage(paper_im)
            self.scissors_im = ImageTk.PhotoImage(scissors_im)

            self.image_list = [self.rock_im, self.paper_im, self.scissors_im]
        except FileNotFoundError:
            print("Khong tim thay anh")
            self.root.destroy()
            exit()

        self.total_rounds = 0
        self.current_round = 0
        self.player_score = 0
        self.ai_score = 0

        self.round_frame = Frame(self.root, bg="#003773")
        self.round_frame.pack(pady=10)

        Label(self.round_frame, text="So round(s): ", font=("Times", 16), fg="white", bg="#003773").pack(side=LEFT)
        self.round_entry = Entry(self.round_frame, width=5, font=("Times", 16))
        self.round_entry.pack(side=LEFT, padx=5)
        self.start_button = Button(self.round_frame, text="Bắt đầu", font=("Times", 16), command=self.start_game)
        self.start_button.pack(side=LEFT, padx=5)

        self.round_label = Label(self.root, text="", font=("Times", 16), fg="white", bg="#003773")
        self.round_label.pack()

        self.computer_label = Label(self.root, image=None, bg="#003773")
        self.computer_label.pack(pady=20)

        self.result_label = Label(self.root, text="Bao nhieu round(s)", font=("Times", 24), bg="#003773", fg="white")
        self.result_label.pack(pady=20)

        self.player_frame = Frame(self.root, bg="#003773")
        self.player_frame.pack(pady=20)

        self.rock_button = Button(self.player_frame, image=self.rock_im, command=lambda: self.play_game(0), bd=0, state=DISABLED)
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = Button(self.player_frame, image=self.paper_im, command=lambda: self.play_game(1), bd=0, state=DISABLED)
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = Button(self.player_frame, image=self.scissors_im, command=lambda: self.play_game(2), bd=0, state=DISABLED)
        self.scissors_button.grid(row=0, column=2, padx=10)

    def start_game(self):
        try:
            rounds = int(self.round_entry.get())
            if rounds <= 0:
                raise ValueError
        except ValueError:
            self.result_label.config(text="Nhap so")
            return

        self.total_rounds = rounds
        self.current_round = 0
        self.player_score = 0
        self.ai_score = 0

        self.result_label.config(text="Chon di")
        self.round_label.config(text=f"Round: {self.current_round} / {self.total_rounds}")

        self.rock_button.config(state=NORMAL)
        self.paper_button.config(state=NORMAL)
        self.scissors_button.config(state=NORMAL)

        self.computer_label.config(image='')

    def play_game(self, player_choice):
        if self.current_round >= self.total_rounds:
            self.result_label.config(text="Het game")
            return

        ai = randint(0, 2)
        self.computer_label.config(image=self.image_list[ai])

        self.current_round += 1
        self.round_label.config(text=f"Round: {self.current_round} / {self.total_rounds}")

        if player_choice == ai:
            result_text = "Hoa con AI luon, cung cung"
        elif (player_choice == 0 and ai == 2) or (player_choice == 1 and ai == 0) or (player_choice == 2 and ai == 1):
            result_text = "Thang con AI luon, kinh vay"
            self.player_score += 1
        else:
            result_text = "Thua con AI luon, ga the"
            self.ai_score += 1

        self.result_label.config(text=result_text)

        if self.current_round == self.total_rounds:
            self.rock_button.config(state=DISABLED)
            self.paper_button.config(state=DISABLED)
            self.scissors_button.config(state=DISABLED)

            if self.player_score > self.ai_score:
                final_text = f"Ban thang con AI voi ti so: {self.player_score} - {self.ai_score}!"
            elif self.player_score < self.ai_score:
                final_text = f"Ga qua, ban thua con AI voi ti so: {self.player_score} - {self.ai_score}!"
            else:
                final_text = f"Ban hoa con AI voi ti so: {self.player_score} - {self.ai_score}!"

            self.result_label.config(text=final_text)


if __name__ == "__main__":
    root = Tk()
    game = Rock_paper_scissor(root)
    root.mainloop()