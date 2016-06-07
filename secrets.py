import random
import sys

def secrets( count ):

    # get the user input
    guess = raw_input( "Guess: " )
    #print guess

    # check to see if they wanted to exit
    if guess == 'exit':
        print 'Goodbye, my dear.'
        sys.exit()

    # check the length of the guess
    if len( guess ) != 4:
        print 'Invalid guess: ( 4 digits )'
        secrets( count )

    # try to cast the guess as an int
    try:
        guess_int = int( guess )
    # if it's not an int, notify user and start over
    except:
        print 'Invalid guess ( integer )'
        secrets( count )

    # check to see if the guess is correct
    match_flag = True
    for i in range( 0, 4, 1 ):
        if num_str[i] != guess[i]:
            match_flag = False
            break

    if match_flag == True:
        print 'Answer: ' + str( num_int )
        print 'YOU WIN in ' + str( count ) + ' guesses!!'
        sys.exit()

    # what is to be printed to the string
    # initialize to '_' for no match at all
    print_list = {}
    for i in range( 0, 4, 1 ):
        print_list[i] = '_'

    # list to hold whether the values have been used
    used_list = {}
    for i in range( 0, 10, 1 ):
        used_list[i] = 0

    # holds whether the digit has been checked or not
    hit_list = {}
    for i in range( 0, 4, 1 ):
        hit_list[i] = 0

    # first check for matches
    for i in range( 0, 4, 1 ):
        if guess[i] == num_str[i]:
            used_list[int( guess[i] )] = 1
            print_list[i] = '!'
            hit_list[i] = 1

    # check to see if there is that value somewhere else in the number
    for i in range( 0, 4, 1 ):
        # if that value hasn't been viewed yet
        if hit_list[i] == 0:
            hit_list[i] = 1
            # search for that digit's value throughout the string
            for j in range( 0, 4, 1 ):
                # if there's a match
                if guess[i] == num_str[j]:
                    # if that value hasn't already been used
                    if used_list[int( guess[i] )] == 0:
                        print_list[i] = '?'
                        used_list[int( guess[i] )] =  1
                        break

    # print the results to the user
    print print_list[0] + ' ' + print_list[1] + ' ' + print_list[2] + ' ' + print_list[3]

    secrets( count + 1 )

def generate_num():
    num_int = 0
    for i in range( 0, 4, 1 ):
        num_str[i] = random.randint( 0, 9 )
        num_int = num_int + ( num_str[i] * 10 ** ( 3 - i ) )
        num_str[i] = str( num_str[i] )
    return num_str, num_int

if __name__ == '__main__':
    # generate the number as an iterable dict and as an int
    num_str = {}
    num_str, num_int = generate_num()
    count = 1
    
    print '**** Welcome to Secrets ****'
    print 'Guess a 4 digit number\n!-correct    ?-digit is somewhere else in the number    _-digit isn\'t in the number\nType exit to leave the game :('

    secrets( count )

