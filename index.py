import random

def game_loop():
    words = ["apple", "banana"]
    chosen_word = random.choice(words)
    hidden = ["_"]*len(chosen_word)
    health = 5
    won = False
    guess_list = []

    while not won:
        for c in hidden:
            print(c, " " ,end="")
        print()
        guess = input("Guess a character: ").lower()
        found_correct = False
        if guess in guess_list:
            print("The letter was guessed!")
            continue
        for i, c in enumerate(list(chosen_word)):
            if guess == c:
                found_correct = True
                hidden[i] = guess
                guess_list.append(c)
        if "".join(hidden) == chosen_word:
            won = True
        if not found_correct:
            health -= 1
            if health == 0:
                break
    
    print("You won!") if won else print("Game Over!")

if __name__ == "__main__":
    game_loop() 


