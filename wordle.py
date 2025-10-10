# Author   : Dominik Gielarowiec    
# Email    : digelarowiec@umass.edu 
# Spire ID : 35150500

import random

def get_guess():
    guess = input("What word is this?: ").upper()
    return guess

def print_word(guess):
    spaced = " ".join(guess)
    print(spaced)

def exact_match_compare(sol, guess):
    solution = list(sol)
    prompt = list(guess)
    feedback =[]
    for i in range(len(solution)):
        if (len(solution)>i and len(prompt)>i):
            if(solution[i]==prompt[i]):
                feedback.append("🟢")
            else:
                feedback.append("🔴")
        else:
            break
    return feedback


def make_solution():
    rando = ["WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"]
    sol = random.choice(rando)
    return sol


def one_turn(sol):
    sol = make_solution()
    guess = get_guess()
    print_word(guess)
    feedback = exact_match_compare(sol, guess)
    print( " ".join(feedback))
    if feedback == ["🟢"]* len(sol):
        print("Congratulations!")
        exit()
    else:
        print("Sorry you didnt get it.")



soln = make_solution()
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
print(f"Word was \"{soln}\", better luck next time.")
    


