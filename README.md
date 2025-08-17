# Hangman-game
Simple word guessing game built using python 

This project demonstrates how to combine **Python backend logic** with a **GUI frontend**.

## Features include:

- Word guessing game with lives system  
- Interactive UI using Tkinter  
- Random word support (can be extended)

## How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   cd hangman-game

## Explanation:

"tkinter" is a built-in GUI toolkit(library) in python used for GUI experience in code.
"messagebox" is a  function used to show pop-up alerts (You won / You  lost)

lives = 5 (Player has 5 lives)
word is converted to list of letters.
ans holds word length of underscores.

root - tk.Tk() creates a window and root.title is the window title

word_label = tk.Label(root, text=" ".join(ans), font=("Arial", 24))
" ".join(ans) → Converts ['_', '_', ...] into " _ _ _ _ _ _ "

word_label.pack(pady=20) 
places the window in 20px vertical padding

lives_label = tk.Label(root, text=f"Lives: {lives}", font=("Arial", 18))
Shows the remaining lives and updates them

guess_entry = tk.Entry(root, font=("Arial", 18))
Creates input box where player enters letters they guessed

def check_guess():
    global lives
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

global lives → Allows modifying the global lives variable.
guess_entry.get() → Gets the letter typed by the user.
.lower() → Ensures the guess is lowercase (so "A" == "a").
guess_entry.delete(0, tk.END) → Clears the input box after guessing.

if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                ans[i] = guess
        word_label.config(text=" ".join(ans))

Checks if the guessed letter is in the word.
If yes → replaces the "_" at correct positions with the guessed letter.
Updates the displayed word with .config().

        if "_" not in ans:
            messagebox.showinfo("Game Over", f"You won! The word was {''.join(word)}")
            root.quit()

If no underscores are left → word is fully guessed → player wins.
Shows a message box, then exits game.

If the guess is wrong
    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")

Deducts 1 life.
Updates the lives label.

        if lives == 0:
            messagebox.showinfo("Game Over", f"You lost! The word was {''.join(word)}")
            root.quit()

If lives reach 0 → player loses.
Shows losing message and quits.

Button to Submit Guess

guess_button = tk.Button(root, text="Guess", command=check_guess, font=("Arial", 16))
guess_button.pack(pady=10)

A button that runs check_guess() when clicked.
Start the Game

root.mainloop()

Starts Tkinter’s event loop.
Keeps the window open, listening for user actions (like button clicks, typing, etc.).


