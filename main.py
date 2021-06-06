import random, hanging


def choose_lang():
    language = input("Please select your language: Albanian, English or German: ")
    difficulty = input("Please select your difficulty: Easy, Medium, Expert: ")

    if language.lower() == 'albanian':
        if difficulty.lower() == 'easy':
            fin = open('albwords.txt')
        elif difficulty.lower() == 'medium':
            fin = open('albwordsMed.txt')
        elif difficulty.lower() == 'expert':
            fin = open('albwordsExp.txt')
        else:
            choose_lang()

    elif language.lower() == 'english':
        if difficulty.lower() == 'easy':
            fin = open('words.txt')
        elif difficulty.lower() == 'medium':
            fin = open('engwordsMed.txt')
        elif difficulty.lower() == 'expert':
            fin = open('engwordsExp.txt')
        else:
            choose_lang()

    elif language.lower() == 'german':
        if difficulty.lower() == 'easy':
            fin = open('gerwords.txt')
        elif difficulty.lower() == 'medium':
            fin = open('gerwordsMed.txt')
        elif difficulty.lower() == 'expert':
            fin = open('gerwordsExp.txt')
        else:
            choose_lang()
    else:
        return choose_lang()
    return fin


print('Welcome to hangman game!')
fin = choose_lang()
# fin = open('words.txt')

words = [line.strip().lower() for line in fin.readlines()]


def play():
    while True:

        word = random.choice(words)
        length = len(word)
        misses = 0

        print(f"Guess the word with {length} letters")

        been_guessed = []
        word_list = []

        for i in range(length):
            word_list.append('_')

        print(*word_list)
        print(word)

        points_total = 0
        word_char_points = len(set(word))
        print(word_char_points)

        while True:
            letter = input("Guess a letter: ")
            if letter not in word and letter not in been_guessed:
                if word_char_points > 0:
                    word_char_points -= 1
                    print(word_char_points)
                misses += 1
                print(hanging.hangman[misses])
                if misses == 5:
                    print('You lost')
                    exit_or_play()

            if letter in been_guessed:
                print("This letter has already been guessed before:")
            been_guessed.append(letter)

            while not letter.isalpha():
                print("Input is invalid:")
                letter = input("Guess a letter: ")

            for i in range(length):
                if letter == word[i]:
                    word_list[i] = letter

            if '_' not in word_list:
                print("You won")
                exit_or_play()
            print(*word_list)
            return word_char_points
    points_total = word_char_points + points_total
    return points_total
# test2

# This definition lets you play again or exit the game after you lost.
def exit_or_play():
    ext_or_play = input("To play again type 'play', to exit the game type 'exit': ")
    while ext_or_play != 'exit' and \
            ext_or_play != 'play':
        ext_or_play = input("To play again type 'play', to exit the game type 'exit': ")
    else:
        if ext_or_play.lower() == 'exit':
            print("Your total points are: " + points_total)
            exit()
        elif ext_or_play.lower() == 'play':
            play()


play()
