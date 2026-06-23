import random
max_lives = 3

def intro():
    print("Welcome to the Python Escape Room")
    print(":Solve the challenges using logic to escape")

def door_one_math_puzzle():
    try:
        answer = int(input("Door 1 : What is value of 7 + 6 * 8 : "))
        return answer == 55 
    except ValueError:
        return False

def door_two_pattern_puzzle(attempts = 2):
    secret = "mystery"
    trails = 0

    while trails < attempts:
        guess = input("Door 2 : Guess the secret word:").lower()
        if guess == "" :
            continue
        if guess == secret :
            return True
        trails += 1
        print("Wrong answer")
    return False

def door_three_code(start = 1, end = 5):
    lucky = random.randint(start,end)
    for i in range(2):
        try:
            guess = int(input("Door 3 : Guess the lucky number(1-5): "))
            if guess == lucky:
                return True
        except ValueError:
            print("Enter a valid number!")
    return False


def reward_badge(*badges):
    return random.choice(badges)

def escape_room():
    lives = max_lives
    collected_badges = set()
    completed_doors=set()
    while True:

        print("\n Choose a Door: ")
        print("1. Math Door")
        print("2. Pattern Door")
        print("3. Lucky Door")
        print("4. Exit Door")
        choice = input("Your Choice: ")
        
        if choice == "1":
            if "1" in completed_doors:
                print("Door 1 already completed!")
            elif door_one_math_puzzle():
                completed_doors.add("1")
                collected_badges.add(reward_badge("Logic Master", "Math Whiz"))
                print("Door Unlocked!")
            else:
                print("Wrong answer")
                lives -= 1

        elif choice == "2":
            if "2" in completed_doors:
                print("Door 2 alreadt completed!")
            elif door_two_pattern_puzzle():
                completed_doors.add("2")
                collected_badges.add(reward_badge("Pattern Pro", "Code Breaker"))
                print("Door Unlocked!")
            else:
                lives -= 1

        elif choice == "3":
            if "3" in completed_doors:
                print("Door 3 already completed!")
            elif door_three_code():
                completed_doors.add("3")
                collected_badges.add(reward_badge("Lucky star", "Risk Taker"))
                print("Door Unlocked!")
            else:
                lives -= 1

        elif choice == "4":
            break

        else:
            print("Invalid door!")
        
        print(f"Lives left{lives}")
        print(f"Badges collected:{collected_badges}")

        if len(collected_badges) == 3:
            print("Congratulations! You Escaped the room!")
            break

        if lives == 0:
            print("Game Over!")
            break

    print("Escape Room Ended. Thanks for playing!")

def main():
    intro()
    escape_room()
main()

