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
- I was thinking of making the game without using arrays, but it would be easier and using for loops I can iterate through an entire array. Reading surrounding cells would be done by subtracting or adding 1 to the x and y axis of the examined cell.
- To ensure correct and efficient software constant testing and improving of the code would be necessary.
- To ensure a robust software I will test the code with unusual inputs and perhaps add error print messages to tell the user what they have done wrong.
- To ensure adaptability my code should consist of many functions rather than just one. 
- To ensure reusability I will attempt having the program ask the user if they would like to see the next iteration after it has run once, or input a new text file. 

--

### **How do I know the program will work correctly?**

Ans - I do not know for certain the program will always work correctly, but constant testing and working in small steps will help avoid bugs and would allow me to solve problems as they arise. This would help arriving at a program that does the required job and works correctly.

### **What situations may break my program?**

Ans - Situations that may break my program would be tested for during the testing stage and possibly include:
* Unexpected content of inputted file including empty file.
* The symbols make a rectangle rather than a square (x != y)
* Wrong file format inputted.
* Unexpected grid size (I will solve this by allowing almost any grid size as input rather than just 1*1, 2 *2, and 3 *3 (Rubust and adaptable))
* Other input file issues
* Output file's name already exists (using the 'w' might overwrite over an already existing file. I am not sure how and if I can solve this).


### **Are there ways to make the program more efficient?**

Ans - I am unsure, but perhaps some of my considerations would make a more efficient program. Those considerations include: 

* Instead of looking for the dead cells symbol (-), the program would look for alive cells symbol (*) only. There is no need to count dead cells.



### **Have I made choices that reduce future adaptability?**

Ans - If I do find such choices I will attempt to modify the program to be more adaptable. 
The nature of the assignment of requiring accepting a specific format (for the input text file) and expecting the same format for the output might make it less desirable to use because it is not interactive. There is also the design of the program required that requires the code to run one iteration and save it in another file that would make it more difficult to run several iterations.
After this assignment I would want to learn (whether in course or on my own) how to make the game interactive in that it is visible boxes to be highlighted (alive) and many iterations can run one after the other.
The code could be made to accept more than just the symbols used in the assignment document so that several representations of live and dead cells could be used to play the game (currently I do not have the skills to have the program accept both the symbols required and other variations of the symbols or making the game represent visible boxes)




### **Which parts of this program might be useful in another project?**

Ans - 
* Parts of this program could be useful for a bigger project of a less simple version of the game of life than the one used such as considering all surrounding boxes or making a visual representation of the game so that the input is not a text file.
* Another use of the code would the use of some functions to interpret text files with the (* and -) symbols. 
* A function to export a certain value or desired output into a new file could be used and taken from the program I am to write.