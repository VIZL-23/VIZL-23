import random

def print_dots(count=1):
    """Prints a specified number of dots."""
    print('.' * count)

def toss():
    ask = int(input("PRESS 1 FOR ODD, PRESS 2 FOR EVEN: "))
    if ask == 1:
        print_dots()
        oddask = int(input("ENTER YOUR TOSS NUMBER (0 to 10): "))
        if 0 <= oddask <= 10:
            oddbot = random.randint(1, 10)
            oddbotplusoddask = oddbot + oddask
            print("YOUR INPUT:", oddask)
            print("COMPUTER INPUT:", oddbot)
            if oddbotplusoddask % 2 == 0:
                print("YOU HAVE LOST THE TOSS")
                compwintoss()
            else:
                youwintoss()

    elif ask == 2:
        print_dots()
        evenask = int(input("ENTER YOUR TOSS NUMBER (0 to 10): "))
        if 0 <= evenask <= 10:
            evenbot = random.randint(1, 10)
            evenbotplusevenask = evenbot + evenask
            print("YOUR INPUT:", evenask)
            print("COMPUTER INPUT:", evenbot)
            if evenbotplusevenask % 2 == 1:
                print("YOU HAVE LOST THE TOSS")
                compwintoss()
            else:
                youwintoss()

    else:
        toss()

def compwintoss():
    tosscompwin = random.randint(1, 2)
    if tosscompwin == 1:
        print("COMPUTER CHOOSES TO BOWL")
        print_dots(2)

        yourscore = 0
        while True:
            computerbowl = random.randint(1, 10)
            youbat = int(input("ENTER YOUR NUMBER (0 TO 10): "))
            if 0 <= youbat <= 10:
                print_dots(3)
                print("YOUR INPUT:", youbat)
                print("COMPUTER INPUT:", computerbowl)
                print_dots(3)

                if youbat == computerbowl:
                    print("OUT")
                    print("YOUR TOTAL SCORE IS", yourscore)
                    yourscore += 1
                    break
                else:
                    yourscore += youbat
                    print("YOUR SCORE IS", yourscore)

        print("COMPUTER NEEDS", yourscore, "TO WIN")
        print_dots(2)
        computerscore = 0
        while True:
            computerbat = random.randint(1, 10)
            youbowl = int(input("ENTER YOUR NUMBER (0 TO 10): "))
            if 0 <= youbowl <= 10:
                print_dots(3)
                print("YOUR INPUT:", youbowl)
                print("COMPUTER INPUT:", computerbat)
                computerscore += computerbat
                print_dots(3)

                if computerscore < yourscore:
                    print("COMPUTER SCORE IS", computerscore)
                    print("NEED", yourscore - computerscore, "TO WIN")
                elif youbowl == computerbat:
                    print("OUT")
                    print("COMPUTER SCORE IS", computerscore)
                    break
                elif computerscore >= yourscore:
                    print("COMPUTER HAS WON")
                    print_dots(9)
                    print("COMPUTER HAS WON")
                    toss()
                else:
                    print("MATCH DRAW")
                    toss()

    elif tosscompwin == 2:
        print("COMPUTER CHOOSES TO BAT")
        print_dots(2)

        computerscore = 0
        while True:
            computerbat = random.randint(1, 10)
            youbowl = int(input("ENTER YOUR NUMBER (0 TO 10): "))
            if 0 <= youbowl <= 10:
                print("YOUR INPUT:", youbowl)
                print("COMPUTER INPUT:", computerbat)
                computerscore += computerbat
                print_dots(3)

                if youbowl == computerbat:
                    print("OUT")
                    print("COMPUTER SCORE IS", computerscore)
                    computerscore += 1
                    break
                else:
                    print("COMPUTER SCORE IS", computerscore)
                    print_dots(3)

        print("YOU NEED", computerscore, "TO WIN")
        yourscore = 0
        while True:
            computerbowl = random.randint(1, 10)
            youbat = int(input("ENTER YOUR NUMBER (0 TO 10): "))
            if 0 <= youbat <= 10:
                print("YOUR INPUT:", youbat)
                print("COMPUTER INPUT:", computerbowl)
                print_dots(3)

                if youbat == computerbowl:
                    print("OUT")
                    print("YOUR TOTAL SCORE IS", yourscore, ". YOU LOSE BY", computerscore - yourscore, "RUNS")
                    toss()
                elif yourscore < computerscore:
                    yourscore += youbat
                    print("YOUR SCORE IS", yourscore)
                elif yourscore >= computerscore:
                    print("YOU WIN THE MATCH")
                    print_dots(7)
                    toss()
                else:
                    print("DRAW MATCH")
                    toss()

toss()
