# Data Structures and Algorithms
algorithms practice

# Notes

### Arrays/Hashing
1. group anagrams: dictionary of tuple -> list; each key will be a representation of character counts `count = [0] * 26`. `index = ord(char) - ord('a')`
2. top k: dictionary of number -> freqs; double array where primary index represents frequency, second array stores ints at that frequency
3. encode/decode strings: encoder writes length of string before string to indicate to decoder how many chars, but ends the int in '#' to handle double digits
ex: `["Hello","World"] -> "5#Hello5#World"`
4. product of array except itself: use prefix array and postfix array and multiply
5. valid sudoku: use floor division and % modulus to represent 3x3 squares `val = board[3*(b//3) + r][3*(b%3) + c]`
6. longest consecutive sequence: put everything in set; find starters (x-1 not in set); figure out that starter's length by checking if x + 1 is in set

### Two Pointers
1. x
2. 

### Stack
1. x
2. 
