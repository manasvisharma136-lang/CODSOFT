import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Rock, Paper, Scissors")
        self.window.geometry("450x450")
        self.window.configure(bg="#2c3e50")  # Dark sleek background
        
        # Game State
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0
        
        # --- UI ELEMENTS ---
        
        # Title
        self.title_label = tk.Label(
            window, text="Rock, Paper, Scissors", 
            font=("Helvetica", 18, "bold"), fg="#ecf0f1", bg="#2c3e50", pady=10
        )
        self.title_label.pack()
        
        # Score Board
        self.score_label = tk.Label(
            window, text="You: 0  |  Computer: 0", 
            font=("Helvetica", 14), fg="#f1c40f", bg="#2c3e50", pady=10
        )
        self.score_label.pack()
        
        # Display Results
        self.result_label = tk.Label(
            window, text="Make your move to start the game!", 
            font=("Helvetica", 12, "italic"), fg="#bdc3c7", bg="#2c3e50", wraplength=400, pady=20
        )
        self.result_label.pack()

        # Action Label
        self.action_label = tk.Label(
            window, text="", font=("Helvetica", 14, "bold"), fg="#e74c3c", bg="#2c3e50"
        )
        self.action_label.pack(pady=10)
        
        # Buttons Container
        self.btn_frame = tk.Frame(window, bg="#2c3e50")
        self.btn_frame.pack(pady=20)
        
        # Stylized Buttons
        self.rock_btn = tk.Button(
            self.btn_frame, text="✊ Rock", font=("Helvetica", 12, "bold"), 
            width=10, bg="#34495e", fg="white", activebackground="#1abc9c",
            command=lambda: self.play("rock")
        )
        self.rock_btn.grid(row=0, column=0, padx=5)
        
        self.paper_btn = tk.Button(
            self.btn_frame, text="✋ Paper", font=("Helvetica", 12, "bold"), 
            width=10, bg="#34495e", fg="white", activebackground="#1abc9c",
            command=lambda: self.play("paper")
        )
        self.paper_btn.grid(row=0, column=1, padx=5)
        
        self.scissors_btn = tk.Button(
            self.btn_frame, text="✌️ Scissors", font=("Helvetica", 12, "bold"), 
            width=10, bg="#34495e", fg="white", activebackground="#1abc9c",
            command=lambda: self.play("scissors")
        )
        self.scissors_btn.grid(row=0, column=2, padx=5)
        
        # Reset Button
        self.reset_btn = tk.Button(
            window, text="Reset Game", font=("Helvetica", 10), 
            bg="#95a5a6", fg="black", command=self.reset_game
        )
        self.reset_btn.pack(side="bottom", pady=20)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        
        # Display what emojis correspond to choices
        emojis = {"rock": "✊", "paper": "✋", "scissors": "✌️"}
        
        result_text = f"You chose: {user_choice.capitalize()} {emojis[user_choice]}\n"
        result_text += f"Computer chose: {computer_choice.capitalize()} {emojis[computer_choice]}"
        
        # Determine Outcome
        if user_choice == computer_choice:
            self.action_label.config(text="IT'S A TIE!", fg="#95a5a6")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.action_label.config(text="YOU WIN!", fg="#2ecc71")
            self.user_score += 1
        else:
            self.action_label.config(text="COMPUTER WINS!", fg="#e74c3c")
            self.computer_score += 1
            
        # Update Labels
        self.result_label.config(text=result_text)
        self.score_label.config(text=f"You: {self.user_score}  |  Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="You: 0  |  Computer: 0")
        self.result_label.config(text="Game reset. Make your move!")
        self.action_label.config(text="")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()