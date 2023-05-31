print("""
Name: Hatem Alfarra
NSID: Hma194
Student #: 11291988
Section: 145-01
""")

print('**********************************************************')

import numpy as np




print("\nWelcome to a simple version of 'Conway's game of life'\n")

print('Rules & instructions:-\n')
print("""In a world of limited rules, small changes to the starting conditions result in vastly different alterations in 
that world without the need of further input from the player. In this game you give me a text file following the rules
given in return for the next step of the world in a game of life world. On a grid every cell interacts with its neighboring
cells. A cell is either alive (*) or dead (-). At each step the following transitions are possible:
  - Any living cell with less than 2 neighbours dies of loneliness.
  - Any living cell with 2 or 3 neighbours remain alive.
  - Any living cell with more than 3 dies of claustrophobia.
  - Any dead cells with exactly 3 neighbours become alive, rising from the ashes like a phoenix.

""")

def Conway(input_textfile_numbers):
    """
    Purpose:
        Play an iteration of the game of life
    Pre-conditions:
        For the parameter an array of equal height and width should be inputted
    Post-conditions:
        A new array is created and is the same size as the array for the parameter
    Return:
        An array of 1s and 0s after 1 cycle/iteration of the game of life. This happens only if the inputted array is
         a square array.
    """

    dimensions = np.shape(input_textfile_numbers)
    x = dimensions[0]
    y = dimensions[1]

    if x != y:
        print('Please use a square array (width equals height) instead')

    output_textfile_numbers = np.zeros((x, y))

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):

            count = 0

            if input_textfile_numbers[i][j] == 1:
                if i != 0:
                    if input_textfile_numbers[i-1][j] == 1:
                        count += 1
                if i < (dimensions[0] - 1):
                    if input_textfile_numbers[i+1][j] == 1:
                        count += 1
                if j != 0:
                    if input_textfile_numbers[i][j-1] == 1:
                        count += 1
                if j < (dimensions[1] - 1):
                    if input_textfile_numbers[i][j+1] == 1:
                        count += 1

                if count < 2:
                    output_textfile_numbers[i][j] = 0
                elif count == 2 or count == 3:
                    output_textfile_numbers[i][j] = 1
                elif count > 3:
                    output_textfile_numbers[i][j] = 0


            elif input_textfile_numbers[i][j] == 0:
                if i != 0:
                    if input_textfile_numbers[i-1][j] == 1:
                        count += 1
                if i < (dimensions[0] - 1):
                    if input_textfile_numbers[i+1][j] == 1:
                        count += 1
                if j != 0:
                    if input_textfile_numbers[i][j-1] == 1:
                        count += 1
                if j < (dimensions[1] - 1):
                    if input_textfile_numbers[i][j+1] == 1:
                        count += 1

                if count == 3:
                    output_textfile_numbers[i][j] = 1

    return output_textfile_numbers


def symbols_to_numbers(input_textfile):
    """
    Purpose:
        convert a text file of * and - symbols to an array where the *'s become 1's and -'s become 0's
    Pre-conditions:
        Text file of * and - symbols only
    Post-conditions:
        None
    Return:
        An array with 1s and 0s
    """

    new_array = []
    for line in input_textfile:
        row = line.strip()

        new_row = []
        for symbol in row:
            if symbol == '*':
                new_row.append(1)
            elif symbol == '-':
                new_row.append(0)

        new_array.append(new_row)

    array = np.array(new_array)

    return array


def numbers_to_symbols(output_textfile_numbers):
    """Purpose:
        Convert an array with 1s and 0s to a text file where 1s become * symbols and 0s become - symbols
    Pre-conditions:
        Array with 1s and 0s only
    Post-conditions:
        None
    Return:
        A text file with * and - symbols"""

    symbol_map = {1: '*', 0: '-'}


    rows, cols = output_textfile_numbers.shape
    lines = []

    for i in range(rows):
        line = ''.join([symbol_map[value] for value in output_textfile_numbers[i]])
        lines.append(line)

    output_textfile_to_be = '\n'.join(lines)

    return(output_textfile_to_be)


def output_textfile(output_textfile_numbers, output_textfile_to_be):
    """
    Purpose:
            Creating a new file 'nxn_updated.txt' where n is the size of the grid
    Pre-conditions:
            2 parameters where the first is an array of 1s and 0s, and the second is the text to be written in the new
            file
    Post-conditions:
            Any file with the same name will be overwritten by this new information and replaced by it
    Return:
            A file containing the contents from the second parameter
            """


    n = str(len(output_textfile_numbers))

    new_name = n + 'x' + n + '_updated.txt'

    output_textfile = open(new_name, 'w')
    output_textfile.write(output_textfile_to_be)

    output_textfile.close()





def game_loop(input_textfile):
    """
        Purpose:
                Encapsulates all the functions needed for the 'game of life' game
        Pre-conditions:
                Text file of symbols given as a parameter
        Post-conditions:
                A file is created that is the next iteration of the file given using the rules and requirements of the game.
                Any file named in the same convention is replaced creating a new file 'nxn_updated.txt' where n is the
                 size of the grid
        Return:
                None
                """

    input_textfile_numbers = symbols_to_numbers(input_textfile)

    output_textfile_numbers = Conway(input_textfile_numbers)

    output_textfile_to_be = numbers_to_symbols(output_textfile_numbers)

    output_textfile(output_textfile_numbers, output_textfile_to_be)


# Allows looping through the program if another iteration is desired to be run
while True:
    input_file = input('Enter text file name: ')
    input_textfile = open(input_file, 'r')
    game_loop(input_textfile)



