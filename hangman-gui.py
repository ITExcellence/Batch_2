import tkinter as tk
from tkinter import messagebox
from wonderwords import RandomWord


class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.root.geometry("1000x1000")
        self.root.configure(bg="#1f2937")
        self.root.resizable(False, False)

        self.random_word = RandomWord()

        # ---------- Title ----------
        tk.Label(
            root,
            text="🎯 HANGMAN",
            font=("Helvetica", 28, "bold"),
            fg="#60a5fa",
            bg="#1f2937",
        ).pack(pady=10)

        # ---------- Canvas ----------
        self.canvas = tk.Canvas(
            root,
            width=250,
            height=280,
            bg="white",
            highlightthickness=2,
            highlightbackground="black",
        )
        self.canvas.pack(pady=10)

        # ---------- Word ----------
        self.word_label = tk.Label(
            root,
            text="",
            font=("Courier New", 30, "bold"),
            fg="white",
            bg="#1f2937",
        )
        self.word_label.pack(pady=20)

        # ---------- Status ----------
        self.status_label = tk.Label(
            root,
            text="Guess a letter",
            font=("Helvetica", 14),
            fg="#22c55e",
            bg="#1f2937",
        )
        self.status_label.pack()

        # ---------- Entry ----------
        self.entry = tk.Entry(
            root,
            font=("Helvetica", 20),
            justify="center",
            width=3,
        )
        self.entry.pack(pady=10)
        self.entry.focus()

        self.entry.bind("<Return>", lambda event: self.guess())

        # ---------- Buttons ----------
        button_frame = tk.Frame(root, bg="#1f2937")
        button_frame.pack(pady=10)

        self.guess_button = tk.Button(
            button_frame,
            text="Guess",
            font=("Helvetica", 13, "bold"),
            bg="#2563eb",
            fg="white",
            width=10,
            command=self.guess,
        )
        self.guess_button.grid(row=0, column=0, padx=10)

        self.new_button = tk.Button(
            button_frame,
            text="New Game",
            font=("Helvetica", 13, "bold"),
            bg="#16a34a",
            fg="white",
            width=10,
            command=self.new_game,
        )
        self.new_button.grid(row=0, column=1, padx=10)

        # ---------- Guessed Letters ----------
        self.guessed_label = tk.Label(
            root,
            text="Guessed Letters:",
            font=("Helvetica", 14),
            fg="orange",
            bg="#1f2937",
        )
        self.guessed_label.pack(pady=20)

        self.new_game()

    # -----------------------------
    # Draw Gallows
    # -----------------------------
    def draw_gallows(self):
        self.canvas.delete("all")

        # Base
        self.canvas.create_line(20, 260, 220, 260, width=4)

        # Pole
        self.canvas.create_line(60, 260, 60, 30, width=4)

        # Top
        self.canvas.create_line(60, 30, 170, 30, width=4)

        # Rope
        self.canvas.create_line(170, 30, 170, 60, width=3)

    # -----------------------------
    # Draw Hangman
    # -----------------------------
    def draw_hangman(self):

        self.draw_gallows()

        mistakes = 6 - self.lives

        # Head
        if mistakes >= 1:
            self.canvas.create_oval(
                150,
                60,
                190,
                100,
                width=3,
            )

        # Body
        if mistakes >= 2:
            self.canvas.create_line(
                170,
                100,
                170,
                170,
                width=3,
            )

        # Left Arm
        if mistakes >= 3:
            self.canvas.create_line(
                170,
                120,
                140,
                145,
                width=3,
            )

        # Right Arm
        if mistakes >= 4:
            self.canvas.create_line(
                170,
                120,
                200,
                145,
                width=3,
            )

        # Left Leg
        if mistakes >= 5:
            self.canvas.create_line(
                170,
                170,
                145,
                210,
                width=3,
            )

        # Right Leg
        if mistakes >= 6:
            self.canvas.create_line(
                170,
                170,
                195,
                210,
                width=3,
            )

    # -----------------------------
    # New Game
    # -----------------------------
    def new_game(self):

        self.answer = self.random_word.word(
            include_parts_of_speech=["verb"],
            word_min_length=5,
            word_max_length=8,
        )

        self.word = list(self.answer)
        self.display = ["_"] * len(self.word)

        self.lives = 6
        self.guessed = set()

        self.guess_button.config(state="normal")
        self.status_label.config(
            text="Guess a letter!",
            fg="#22c55e",
        )

        self.update_screen()

    # -----------------------------
    # Update GUI
    # -----------------------------
    def update_screen(self):

        self.draw_hangman()

        self.word_label.config(
            text=" ".join(self.display)
        )

        guessed = ", ".join(sorted(self.guessed))

        self.guessed_label.config(
            text="Guessed Letters: " + guessed
        )

        self.entry.delete(0, tk.END)
        self.entry.focus()

    # -----------------------------
    # Guess Logic
    # -----------------------------
    def guess(self):

        letter = self.entry.get().lower()

        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning(
                "Invalid Input",
                "Please enter a single letter."
            )
            return

        if letter in self.guessed:
            messagebox.showinfo(
                "Already Guessed",
                "You already guessed that letter."
            )
            return

        self.guessed.add(letter)

        if letter in self.word:

            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.display[i] = letter

            self.status_label.config(
                text="Correct Guess!",
                fg="#c56922",
            )

        else:

            self.lives -= 1

            self.status_label.config(
                text="Wrong Guess!",
                fg="red",
            )

        self.update_screen()

        if "_" not in self.display:

            self.guess_button.config(state="disabled")

            messagebox.showinfo(
                "Congratulations!",
                f"You won!\n\nThe word was '{self.answer}'."
            )

        elif self.lives == 0:

            self.guess_button.config(state="disabled")

            self.word_label.config(
                text=" ".join(self.word)
            )

            messagebox.showerror(
                "Game Over",
                f"You lost!\n\nThe word was '{self.answer}'."
            )


# -----------------------------
# Main Program
# -----------------------------
root = tk.Tk()
HangmanGUI(root)
root.mainloop()