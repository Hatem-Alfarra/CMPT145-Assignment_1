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

    dimensions = np.shape(input_textfile_numbers)

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):

            print(input_textfile_numbers[i][j])




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



while True:
    input_file = input('Enter text file name: ')
    input_textfile = open(input_file, 'r')

    input_textfile_numbers = symbols_to_numbers(input_textfile)
    print(input_textfile_numbers)

    Conway(input_textfile_numbers)



