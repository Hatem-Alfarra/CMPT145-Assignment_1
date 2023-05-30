`Name: Hatem Alfarra`  
`Student #: 11291988`  
`NSID: Hma194`

Note: This project is for assignment 1 question 3 for the course CMPT 145

---------------------------------
=====================

# Design Goals:
**            **

### Main objective: 

> 1. Document `design decisions and ideas` for the project before coding the game
 
> 2. Code a simple version of the game **`Conway's game of life`** following certain instructions

> 3. `Test-driven development (TDD)` while designing the game. The process is to be `documented` in this README.md file


--

Design decisions and ideas:

- To design the game of life I am thinking of the input txt file and how a function can process then output the next step without altering the initial text file.
- First a function should open the file to read it.
- Information in the text file should be converted to a format that is iterable or that can be read. I am thinking of creating array's using numpy to house the game.
- I should be able to find a way to count symbols ('-' and '*'). It should be possible to use conditional statements to count alive cells using *'s (the symbol), but if not I can make a function to convert dead cells to 0's and alive cells to 1's (this would make counting neighboring cells easy), but hopefully I do not have to do that and using symbols is enough because converting symbols to 1s and 0s might make my code slower (an extra 2 steps of converting to numbers and converting back to symbols later).
- Dimensions of the array would be determined using the len function to count content of the input file (.strip() and other methods to format the content of the array).
- Arrays will be made with help of numpy.
- A loop will go through the content of the array and using conditional statements the outcomes will be recorded in a new array or list.
  - Game rules and more: 
    - If the alive cell has less than 2 (0 or 1) neighboring alive cells it dies.
    - If the alive cell has 2 or 3 neighbors it remains alive.
    - If a dead cell has exactly 3 neighbors it becomes alive.
    - If the alive cell has more than 3 neighbors it dies.
    - Initially only orthogonal neighbors are considered (up, down, left, and right)
    - The code should contain a function Conway(input_textfile), where the parameter is a file inputted.
    - The resulting grid/outcome should be stored in a new file named 'nxn_updated.txt', where n is the size of the grid.
- The resulting list or array would need to be saved in a new file so a function should create a file for writing (using open and 'w').