🎯 Domain Range Number Guessing Game
Welcome to the Domain Range Number Guessing Game, a fun Python-based command-line experience where you set the limits—and the computer tries to stump you with a random number between them. Are you ready to guess your way to victory?
📜 Description
This game lets the user:
- Choose a range (lower and upper limits)
- Attempt to guess a randomly generated number within that range
- Receive hints until they guess correctly
Each round provides feedback like "A little lower!" or "Higher, Higher!" to guide the guesser toward the target number.
🚀 How to Run
- Make sure you have Python installed on your machine.
- Save the code to a .py file (e.g., guess_game.py)
- Run the program in your terminal.
🎮 How to Play
- You'll be prompted to enter a lower and upper limit for the number to guess.
- Make your guess within the specified range.
- The program gives hints until you guess the correct number.
- After guessing correctly, it shows a summary of your performance including number of attempts.
🧠 Game Logic Highlights
- Input validation ensures that both limits and guesses are numeric and within range.
- A random number is generated using random.randrange().
- The game loops until the correct number is guessed, tracking the number of attempts.
- After success, a summary is displayed.
🛠️ Requirements
- Python 3.x
- No external libraries needed beyond the built-in random module
💡 Notes
- Be sure that your upper limit is greater than your lower limit, or you'll be prompted to correct it.
- This game is entirely text-based and runs in the console.
