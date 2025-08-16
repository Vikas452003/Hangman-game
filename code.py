import tkinter as tk
from tkinter import messagebox

# Backend game data
lives = 5
word = list("den")
ans = ["_"] * len(word)

# Tkinter window
root = tk.Tk()
root.title("Hangman Game")

# Display current word
word_label = tk.Label(root, text=" ".join(ans), font=("Arial", 24))
word_label.pack(pady=20)

# Display lives
lives_label = tk.Label(root, text=f"Lives: {lives}", font=("Arial", 18))
lives_label.pack(pady=10)

# Entry box for guess
guess_entry = tk.Entry(root, font=("Arial", 18))
guess_entry.pack(pady=10)

def check_guess():
    global lives
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                ans[i] = guess
        word_label.config(text=" ".join(ans))
        if "_" not in ans:
            messagebox.showinfo("Game Over", f"You won! The word was {''.join(word)}")
            root.quit()
    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        if lives == 0:
            messagebox.showinfo("Game Over", f"You lost! The word was {''.join(word)}")
            root.quit()

# Button to submit guess
guess_button = tk.Button(root, text="Guess", command=check_guess, font=("Arial", 16))
guess_button.pack(pady=10)

root.mainloop()
