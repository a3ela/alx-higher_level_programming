# 0x00-python-hello_world

## `0-run`
a Shell script that runs a Python script.

The Python file name will be saved in the environment variable  `$PYFILE`

## `1-run_inline`

Done!
a Shell script that runs Python code.

The Python code will be saved in the environment variable  `$PYCODE`

## `2-print.py`
a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

## 3-print_number.py
print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

## `4-print_float.py`
print the float stored in the variable `number` with a precision of 2 digits.

## `5-print_string.py`
print 3 times a string stored in the variable `str`, followed by its first 9 characters..
## `6-concat.py`
print `Welcome to Holberton School!`

##  `7-edges.py`
-   `word_first_3`  should contain the first 3 letters of the variable  `word`
-   `word_last_2`  should contain the last 2 letters of the variable  `word`
-   `middle_word`  should contain the value of the variable  `word`  without the first and last letters

## 8-concat_edges.py
print `object-oriented programming with Python`, followed by a new line.

## 9-easter_egg.py
prints “The Zen of Python”, by TimPeters, followed by a new line..


## 10-check_cycle.c, lists.h
a function in C that checks if a singly linked list has a cycle in it.

-   Prototype:  `int check_cycle(listint_t *list);`
-   Return:  `0`  if there is no cycle,  `1`  if there is a cycle

## `100-write.py`

Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

## 101-compile

a script that compiles a Python script file.

The Python file name will be stored in the environment variable  `$PYFILE`

The output filename has to be  `$PYFILEc`  (ex:  `export PYFILE=my_main.py`  => output filename:  `my_main.pyc`)
## 102-magic_calculation.py
Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
