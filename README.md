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
1. valid palindrome: left, right pointer; use .isalnum() bool and .lower()
2. 2sum O(1) memory: left, right pointer; if less than target increase left, if more decrease right since it is sorted non-decreasing
3. 3sum: first sort array; for each n in nums, use left and right pointer to find target - n; handle dups by starting n at last instance of dup; and avoid dups at left, right iteration
4. container with most water: left, right pointer; calculate area, whichever is min(left, right), iterate that
5. trapping rain water: left, right pointer; keep track of leftMax, rightMax; move wtv is smaller; as you iterate add up rain water max - height; this works bc if ur at pointer's max, no water can be trapped

### Stack
1. valid parenthesis: open = add it to stack; close = check top of stack and pop, if not match then return false
2. minStack: in stack keep track of elems relation to min rather than elem; when encounter new min use diff for old min so it is negative and u can keep track
3. reverse polish notation: add nums to stack; when you see operator, empty stack and use operator on the two nums; add result to stack; only 2 vals in stack at any time
4. daily temps: maintain monotonic decreasing stack, if you encounter a warmer temp, start popping from stack, stack holds array [index, temp] vals
5. car fleet: if a car's time to finish is less than the car starting in front of it, it joins the front car's fleet; go through list of positions/times in reverse and add up fleets
6. largest recatangle histogram: stack storing (startIndex, height) monotonic increasing; when shorter bar appears, pop taller bars and calc areas, updating startIndex for short bar

### Binary Search
1. binary search: use left and right pointer and calculate median of left and right
2. search 2d matrix: same strategy as binary search of list, treat matrix as one long list, calculate row/col using // and % operators like valid sudoku
3. koko bananas: k is rate we want to optimize rate; binary search from k=1 to k=max(piles) or lowest rate is 1 and highest rate is largest pile
4. find min in rotated sorted array: two sorted segments of array, min always in right segment; compare mid to right and move right or left to min
5. search rotated sorted array: left, right pointer; determine which side of mid is sorted; check if target in range of sorted side; update left or right