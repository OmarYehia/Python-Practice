import math
import random


# Problem 1
def distance_between_points(p1, p2):
    return math.sqrt(pow((p2[1] - p1[1]), 2) + pow((p2[0] - p1[0]), 2))


print("Problem 1 - Distance between points (0, 0) and (0, 2):",
      distance_between_points((0, 0), (0, 2)))
print("-" * 10)


# Problem 2
def get_unique_numbers(numbers):
    return set(numbers)


print("Problem 2 - Unique numbers for list [1, 2, 2, 3, 2]:",
      get_unique_numbers([1, 2, 2, 3, 2]))
print("-" * 10)


# Problem 3
def scramble_string(str1, str2):
    mid1 = math.ceil(len(str1) / 2)
    mid2 = math.ceil(len(str2) / 2)
    return (str1[:mid1] + str2[:mid2]) + (str1[mid1:] + str2[mid2:])


print("Problem 3 - str1 = abcde and str2 = omar:",
      scramble_string("", "omar"))
print("-" * 10)


# Problem 4
def most_popular_words(*args):
    words = []
    frq = {}

    if len(args) != 1:
        return "Invalid usage, please enter a single file name"

    # Reading the file
    with open(args[0]) as f:
        words = f.read().split()
        for word in words:
            if word in frq:
                frq[word] += 1
            else:
                frq.update({word: 1})
        f.close()

    frq = sorted(frq.items(), key=lambda x: x[1], reverse=True)

    for i in range(20):
        if i == len(frq):
            break
        print(f"{i + 1}- \"{frq[i][0]}\" was repeated {frq[i][1]} times.")


print("Problem 4:")
most_popular_words('input_file_p4.txt')
print("-" * 10)


# Problem 5
def remove_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join([x for x in input_string if x not in vowels])


print("Problem 5:",
      remove_vowels("This is a very intersting string to remove vowels from"))
print("-" * 10)


# Problem 6
def character_location(input_string, ch):
    locations = []

    for i in range(len(input_string)):
        if ch.lower() == input_string[i].lower():
            locations.append(i)
    return locations if len(locations) > 0 else "Not found"


print("Problem 6:", character_location("Google", "o"))
print("-" * 30)


# Bonus
def guess_the_number():
    random_range = 100
    lucky_number = random.randint(0, random_range)
    retries = 10
    guessed_numbers = []
    high_number_messages = ["Maybe try a lower number?",
                            "No, still too high", "Go LOWER!"]
    low_number_messages = ["Maybe try a higher number?",
                           "No, still too low", "Go HIGHER!"]

    # Reading previous game information
    with open('bonus_game.txt', "r") as f:
        scores = f.read().split(',')
        games_played = int(scores[0])
        games_won = int(scores[1])
        f.close()

    # Welcome message
    print(
        f"Hello! You've played {games_played} game so far and won {games_won} of them")

    # Game Logic
    while retries > 0:
        print(f"Remaining trials = {retries}")
        user_input = int(
            input(f"Please choose a random number between 0 - {random_range} inclusive:\n"))
        if user_input == lucky_number:
            print("Wow! You guessed it! Now try to guess the new number")
            guessed_numbers = []
            lucky_number = random.randint(0, random_range)
            games_won += 1
        elif user_input > random_range:
            print(
                f"This number is out of range! Only guess numbers between 0 - {random_range}")
        elif user_input in guessed_numbers:
            print("You've already guessed this number before ^_^")
        elif user_input > lucky_number:
            print(high_number_messages[random.randint(0, 2)])
            retries -= 1
        elif user_input < lucky_number:
            print(low_number_messages[random.randint(0, 2)])
            retries -= 1
        guessed_numbers.append(user_input)

    # Updating scores file
    games_played += 1
    with open('bonus_game.txt', "w") as f:
        f.write(f"{games_played},{games_won}")
        f.close()

    new_game = input("Game over, would you like to play another game? (y,n)")
    guess_the_number() if new_game == 'y' else print("Thank you for playing today!")


guess_the_number()
