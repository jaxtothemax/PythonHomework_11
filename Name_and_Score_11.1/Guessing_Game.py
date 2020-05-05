import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0
name = str(input("Enter your name: "))

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

print("-----Scores from previous players-----")
for score_dict in score_list:
    print("Player: " + score_dict['name'] + ", " + str(score_dict["attempts"]) + " attempts, secret number: " + str(score_dict["secret_number"]) + ", date: " + score_dict["date"])


while True:
    
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"secret_number": secret, "name": name, "attempts": attempts, "date": str(datetime.datetime.now())})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")