import turtle
import pandas as pd
from tkinter import simpledialog, messagebox, Tk
import time

class MapGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("US States Map Game")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)
        self.t = turtle.Turtle()
        self.t.penup()
        self.states_data = pd.read_csv("50_states.csv")
        self.states_found = []
        self.correct_guesses = 0
        self.start_time = None

    def load_map(self):
        self.screen.bgpic("blank_states_img.gif")
        self.screen.update()

    def show_state_name(self, state, x, y):
        self.t.goto(x, y)
        self.t.write(state, align="center", font=("Poppins", 15, "bold"))

    def is_valid_state(self, state):
        return state.lower() in self.states_data["state"].str.lower().values

    def get_state_guess(self):
        guess = simpledialog.askstring("Guess the State", "Enter a state name:")
        if guess is None:
            return None
        return guess.title()

    def check_guess(self, guess):
        if self.is_valid_state(guess) and guess not in self.states_found:
            self.states_found.append(guess)
            self.correct_guesses += 1
            row = self.states_data[self.states_data["state"].str.lower() == guess.lower()].iloc[0]
            self.show_state_name(guess, row["x"], row["y"])
            messagebox.showinfo("Correct!", f"{guess} is correct!")
        else:
            messagebox.showerror("Incorrect", "Please enter a valid state name.")

    def play_game(self):
        self.load_map()
        self.start_time = time.time()
        while len(self.states_found) < 50:
            guess = self.get_state_guess()
            if guess is None:
                break
            self.check_guess(guess)
        if self.correct_guesses == 50:
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            messagebox.showinfo("Congratulations!", f"You found all the states!\nTime: {minutes} minutes {seconds} seconds")
        else:
            messagebox.showinfo("Game Over", "You've exited the game.")
        self.screen.mainloop()

    def close_game(self):
        self.screen.bye()


