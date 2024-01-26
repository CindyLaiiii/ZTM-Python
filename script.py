from random import randint

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("You are a genious!")
            return True
    else:
        print('hey, I said 1~10')
        return False

answer = randint(1, 10)

if __name__ == '__main__':
    while True:
        try:
            guess = int(input("guess a number 1~10:"))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print("Please enter a number")
            continue
