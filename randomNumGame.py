import random  

def main():
    randomnum = random.randint(1,10)
    higher_or_lower(randomnum)


def higher_or_lower(randomnum):
    for i in range(1,4,1):
        guess = int(input("What's your guess: "))
        if randomnum<guess:
            print("Your guess was too high")
        elif randomnum>guess:
            print("Your guess was to low")
        elif randomnum==guess:
            print("You got it")
            return
    print(f'Sorry you didnt get it, it was {randomnum}')
    

if __name__ == "__main__":
    main()
