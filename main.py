import random

while True:
    print("PRESS HELP TO GET INSTRUCTIONS")
    print('Press 1 for Tic Tac Toe\nPress 2 to play tictactoe with computer\nPress 3 for Rock Paper Scissor\nPress 4 for Hangman')
    print('Press 5 for Basic Car game\nPress 6 for Number Guessing Game')
    print('Enter QUIT to break this loop')
    cmd = input(">")
    if cmd.lower() == "help":
        
        print('Press 1 for Tic Tac Toe\nPress 2 to play tictactoe with computer\nPress 3 for Rock Paper Scissor\nPress 4 for Hangman')
        print('Press 5 for Basic Car game\nPress 6 for Number Guessing Game')
        print('Enter QUIT to break this loop')
        print('Press help for help . Oh i forgot that is the way i got here right XD')

    #cybertrauma
    elif cmd == '1':
        data = ["1","2","3","4","5","6","7","8","9"]
        
        def board(data):
            return data[0] +"|"+ data[1] +"|"+ data[2] + "\n"+ '------'+"\n" + data[3] +'|'+ data[4] +'|'+ data[5] + "\n" + '------' +"\n" + data[6] +'|'+ data[7] +'|'+ data[8] + "\n"

        def marker(data,x,turn):
            while True:
                    if x >9 or x <0:
                        print("try again !Wrong input")
                        x = int(input("enter"))
                    elif data[x-1] =="X" or data[x-1] == "O":
                        print("try again !Wrong input")
                        x = int(input("enter"))
                    elif turn%2 == 0:
                        data[x-1] = "O"
                        break
                    elif turn%2 == 1:
                        data[x-1] = "X"
                        break
                    else :
                        print("There is something  wrong")




        def win_check(data):

            if data[0]==data[1] and data[1]==data[2]:
                    print(f'{data[0]} won the match')
                    return 1
            elif data[3]==data[4] and data[4]==data[5]:
                    print(f'{data[3]} won the match')
                    return 1
            elif data[6]==data[7] and data[7]==data[8]:
                    print(f'{data[6]} won the match')
                    return 1
            elif data[0]==data[3] and data[3]==data[6]:
                    print(f'{data[0]} won the match')
                    return 1
            elif data[1]==data[4] and data[4]==data[7]:
                    print(f'{data[1]} won the match')
                    return 1
            elif data[2]==data[5] and data[5]==data[8]:
                    print(f'{data[2]} won the match')
                    return 1
            elif data[0]==data[4] and data[4]==data[8]:
                    print(f'{data[0]} won the match')
                    return 1
            elif data[2]==data[4] and data[4]==data[6]:
                    print(f'{data[2]} won the match')
                    return 1

        turn = 0
        print(board(data))
        while turn < 9:
            if win_check(data) == 1:
                break
            elif turn%2 == 1:
                x = int(input("enter(player X):"))
                if x.lower() = "quit":
                    break
                else:
                    marker(data,x,turn)
                    turn += 1
                    print(board(data))
            elif turn%2 == 0:
                x = int(input("enter(player O):"))
                if x.lower() = "quit":
                    break
                else:
                    marker(data,x,turn)
                    turn += 1
                    print(board(data))
        if turn == 9 and  win_check(data) != 1:
            print("this was a TIE")
        print("Press 1 to play again.....")
    #cybertrauma
    elif cmd == '2':
        data = ["1","2","3","4","5","6","7","8","9"]
        def board(data):
            return data[0] +"|"+ data[1] +"|"+ data[2] + "\n"+ '------'+"\n" + data[3] +'|'+ data[4] +'|'+ data[5] + "\n" + '------' +"\n" + data[6] +'|'+ data[7] +'|'+ data[8] + "\n"

        def marker(data,x,turn):
            while True:
                    if x >9 or x <0:
                        print("try again !Wrong input")
                        x = int(input("enter(USER)"))
                    elif data[x-1] =="X" or data[x-1] == "O":
                        print("try again !Wrong input")
                        x = int(input("enter"))
                    elif turn%2 == 0:
                        data[x-1] = "O"
                        break
                    elif turn%2 == 1:
                        data[x-1] = "X"
                        break
                    else :
                        print("There is something  wrong")




        def win_check(data):

            if data[0]==data[1] and data[1]==data[2]:
                    print(f'{data[0]} won the match')
                    return 1
            elif data[3]==data[4] and data[4]==data[5]:
                    print(f'{data[3]} won the match')
                    return 1
            elif data[6]==data[7] and data[7]==data[8]:
                    print(f'{data[6]} won the match')
                    return 1
            elif data[0]==data[3] and data[3]==data[6]:
                    print(f'{data[0]} won the match')
                    return 1
            elif data[1]==data[4] and data[4]==data[7]:
                    print(f'{data[1]} won the match')
                    return 1
            elif data[2]==data[5] and data[5]==data[8]:
                    print(f'{data[2]} won the match')
                    return 1
            elif data[0]==data[4] and data[4]==data[8]:
                    print(f'{data[0]} won the match')
                    return 1
            elif data[2]==data[4] and data[4]==data[6]:
                    print(f'{data[2]} won the match')
                    return 1

        turn = 0
        mylist = [1,2,3,4,5,6,7,8,9]
        print(board(data))
        while turn < 9:
            if win_check(data) == 1:
                break
            elif turn%2 == 1:
                x = int(input("enter(USER):"))
                if x.lower() = "quit":
                    break
                else:
                    marker(data,x,turn)
                    turn += 1
                    print(board(data))
                    mylist.remove(x)
            elif turn%2 == 0:
                x = random.choice(mylist)
                print(f"computer's input was {x}")
                marker(data,x,turn)
                turn += 1
                print(board(data))
        if turn == 9 and  win_check(data) != 1:
            print("this was a TIE")
    #AbhiramKonduru
    elif cmd == '3':
        print("NOTE: the person to score 5 points first wins")
        list = ["rock","paper","scissor"]
        computer = 0
        user = 0
        def show_input(x,y):
            print(f"computer's input was {x}")
            print(f"user's input was {y}")
        def show_score(x,y):
            print(f"computer's score is {computer}")
            print(f"user's score is     {user}")
        while True:
            x = random.choice(list)
            y = input("Rock?Paper? or scissor?").lower()
            if y.lower() = "quit":
                break
            else:
                if computer == 5:
                    print('Computer won the game')
                    print('exiting to main menu...')
                    break
                elif user == 5:
                    print('User won the game')
                    print('exiting to main menu...')
                    break
                elif x == y:
                    show_input(x,y)
                    print("This was a tie")
                    show_score(x,y)
                elif x == "rock" and y == "paper" :
                    show_input(x,y)
                    print("User got a point")
                    user +=1
                    show_score(x,y)
                elif y == "rock" and x == "paper":
                    show_input(x,y)
                    print("Computer got a point")
                    computer +=1
                    show_score(x,y)
                elif x == "rock" and y == "scissor" :
                    show_input(x,y)
                    print("Computer got a point")
                    computer +=1
                    show_score(x,y)
                elif y == "rock" and x == "scissor" :
                    show_input(x,y)
                    print("User got a point")
                    user +=1
                    show_score(x,y)
                elif x == "scissor" and y == "paper" :
                    show_input(x,y)
                    print("Computer got a point")
                    computer +=1
                    show_score(x,y)
                elif y == "scissor" and x == "paper" :
                    show_input(x,y)
                    print("user got a point")
                    user +=1
                    show_score(x,y)
                else:
                    print("something is wrong")
    #cybertrauma
    elif cmd == '4':
        
        word_list = ['wares','soup','mount','extend','brown','expert','tired','humidity','backpack','crust','dent','market','knock','smite','windy','coin','throw','silence','bluff','downfall','climb','lying','weaver','snob','kickoff','match','quaker','foreman','excite','thinking','mend','allergen','pruning','coat','emerald','coherent','manic','multiple','square','funded','funnel','sailing','dream','mutation','strict',
        'mystic','film','guide','strain','bishop','settle','plateau','emigrate','marching','optimal','medley','endanger','wick','condone','schema','rage','figure','plague','aloof','there','reusable','refinery','suffer','affirm',]
            


        def get_word():
            word = random.choice(word_list)
            return word.upper()


        def play(word):
            word_completion = "_" * len(word)
            guessed = False
            guessed_letters = []
            guessed_words = []
            tries = 6
            print("Let's play Hangman!")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")
            while not guessed and tries > 0:
                guess = input("Please guess a letter or word: ").upper()
                if len(guess) == 1 and guess.isalpha():
                    if guess in guessed_letters:
                        print("You already guessed the letter", guess)
                    elif guess not in word:
                        print(guess, "is not in the word.")
                        tries -= 1
                        guessed_letters.append(guess)
                    else:
                        print("Good job,", guess, "is in the word!")
                        guessed_letters.append(guess)
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == guess]
                        for index in indices:
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        if "_" not in word_completion:
                            guessed = True
                elif len(guess) == len(word) and guess.isalpha():
                    if guess in guessed_words:
                        print("You already guessed the word", guess)
                    elif guess != word:
                        print(guess, "is not the word.")
                        tries -= 1
                        guessed_words.append(guess)
                    else:
                        guessed = True
                        word_completion = word
                else:
                    print("Not a valid guess.")
                print(display_hangman(tries))
                print(word_completion)
                print("\n")
            if guessed:
                print("Congrats, you guessed the word! You win!")
            else:
                print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


        def display_hangman(tries):
            stages = [  # final state: head, torso, both arms, and both legs
                        """
                        --------
                        |      |
                        |      O
                        |     \\|/
                        |      |
                        |     / \\
                        -
                        """,
                        # head, torso, both arms, and one leg
                        """
                        --------
                        |      |
                        |      O
                        |     \\|/
                        |      |
                        |     / 
                        -
                        """,
                        # head, torso, and both arms
                        """
                        --------
                        |      |
                        |      O
                        |     \\|/
                        |      |
                        |      
                        -
                        """,
                        # head, torso, and one arm
                        """
                        --------
                        |      |
                        |      O
                        |     \\|
                        |      |
                        |     
                        -
                        """,
                        # head and torso
                        """
                        --------
                        |      |
                        |      O
                        |      |
                        |      |
                        |     
                        -
                        """,
                        # head
                        """
                        --------
                        |      |
                        |      O
                        |    
                        |      
                        |     
                        -
                        """,
                        # initial empty state
                        """
                        --------
                        |      |
                        |      
                        |    
                        |      
                        |     
                        -
                        """
            ]
            return stages[tries]


        def main():
            word = get_word()
            play(word)
            while input("Play Again? (Y/N) ").upper() == "Y":
                word = get_word()
                play(word)


        if __name__ == "__main__":
            main()
    #AbhiramKonduru
    elif cmd == '5':
        cmd = ""
        start = False
        print('enter help for getting help in game')
        while cmd.lower() != "quit":
            cmd = input(">>").lower()
            if cmd == "help":
                print("help - for help")
                print("start - to start the car")
                print("stop - to stop the car")
            elif cmd == "start":
                if start == False:
                    start = True
                    print ("car started ready to go")
                else:
                    print ("car already started")
            elif cmd == "stop":
                if start == False :
                    print("the car is already stopped")
                else:
                    start = False 
                    print ("the car has been stopped")
            elif cmd == "quit":
                print ("quitting..")
                print('YOU ARE NOW IN THE MAIN SCREEN!')
                break  
            else :
                print("i dont inderstand that")
    #AbhiramKonduru
    elif cmd == '6':
        rand_number = random.randint(0,100)
        print(rand_number)
        while True:
            user_guess = int(input("GUESS A NUMBER BETWEEN 0 and 100 : "))
            if user_guess.lower() = 'quit':
                break
            else:
                if  rand_number>user_guess:
                    print('Your Guess was lower than the number. Try again!')
                elif user_guess>rand_number:
                    print('Your Guess was higher that the number. Try again!')
                elif rand_number == user_guess:
                    print('Congratulations! You guessed it right')
                    print("press 6 to start over!")  
                    break 
        

    elif cmd.lower() == 'quit':
        break


