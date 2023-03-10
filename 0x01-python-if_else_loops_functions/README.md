# 0x01-python-if_else_loops_functions

## 0-positive_or_negative.py
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.<br>
      The output of the program  is: 
           <ul> <li>The number, followed by</li>
            <li>if the number is greater than 0: `is positive`</li>
            <li> if the number is 0: `is zero`</li>
            <li>if the number is less than 0: `is negative`</li>
            </ul>
            
## 1-last_digit.py
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.<br><br>
-   The output of the program should be:
    -   The string  `Last digit of`, followed by
    -   the number, followed by
    -   the string  `is`, followed by the last digit of  `number`, followed by
        -   if the last digit is greater than 5: the string  `and is greater than 5`
        -   if the last digit is 0: the string  `and is 0`
        -   if the last digit is less than 6 and not 0: the string  `and is less than 6 and not 0`
    -   followed by a new line
##  2-print_alphabet.py
a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
## 3-print_alphabt.py
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- -   Print all the letters except  `q`  and  `e`
##  4-print_hexa.py
Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)
```
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
```
## 5-print_comb2.py
Write a program that prints numbers from `0` to `99`.
- Numbers must be separated by  `,`, followed by a space
-   Numbers should be printed in ascending order, with two digits
-   The last number should be followed by a new line
## `6-print_comb3.py`
Write a program that prints all possible different combinations of two digits.

-   Numbers must be separated by  `,`, followed by a space
-   The two digits must be different
-   `01`  and  `10`  are considered the same combination of the two digits  `0`  and  `1`
##  7-islower.py
Write a function that checks for lowercase character.

-   Prototype:  `def islower(c):`
-   Returns  `True`  if  `c`  is lowercase
-   Returns  `False`  otherwise
## 8-uppercase.py
function that prints a string in uppercase followed by a new line.

-   Prototype:  `def uppercase(str):`
## 9-print_last_digit.py

Write a function that prints the last digit of a number.

-   Prototype:  `def print_last_digit(number):`
-   Returns the value of the last digit
## 10-add.py
a function that adds two integers and returns the result.

-   Prototype:  `def add(a, b):`
-   Returns the value of  `a + b`
## 11-pow.py
a function that computes  `a`  to the power of  `b`  and return the value.

-   Prototype:  `def pow(a, b):`
-   Returns the value of  `a ^ b`
## 12-fizzbuzz.py

a function that prints the numbers from 1 to 100 separated by a space.

-   For multiples of three print  `Fizz`  instead of the number and for multiples of five print  `Buzz`.
-   For numbers which are multiples of both three and five print  `FizzBuzz`.
-   Prototype:  `def fizzbuzz():`
## 13-insert_number.c, lists.h


a function in C that inserts a number into a sorted singly linked list.

-   Prototype:  `listint_t *insert_node(listint_t **head, int number);`
-   Return: the address of the new node, or  `NULL`  if it failed
## 100-print_tebahpla.py

a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.
## 101-remove_char_at.py

a function that creates a copy of the string, removing the character at the position  `n`  (not the Python way, the “C array index”).

-   Prototype:  `def remove_char_at(str, n):`
## 102-magic_calculation.py


the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
