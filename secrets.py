import random
import sys
# int i = random.randint( 0, 9 )

def secrets():

    # get the user input
    guess = raw_input( "Guess: " )
    print guess

    # check to see if they wanted to exit
    if guess == 'exit':
        print 'Goodbye, my dear.'
        sys.exit()

    # check the length of the guess
    if len( guess ) != 4:
        print 'Invalid guess: ( 4 digits )'
        secrets()

    # try to cast the guess as an int
    try:
        guess = int( guess )
    # if it's not an int, notify user and start over
    except:
        print 'Invalid guess ( integer )'
        secrets()

    if guess == num_int:
        print 'YOU WIN!!'
        sys.exit()

    guess = str( guess )
    print guess[0]
        

    secrets()

def generate_num():
    num_int = 0
    for i in range( 0, 4, 1 ):
        num_str[i] = random.randint( 0, 9 )
        num_int = num_int + ( num_str[i] * 10 ** ( 3 - i ) )
    return num_str, num_int

if __name__ == '__main__':
    # generate the number as an iterable dict and as an int
    num_str = {}
    num_str, num_int = generate_num()
    secrets()

