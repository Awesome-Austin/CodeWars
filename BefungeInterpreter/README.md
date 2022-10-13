# Befunge Interpreter
Esoteric languages are pretty hard to program, but it's fairly interesting to write interpreters for them!

Your task is to write a method which will interpret Befunge-93 code! Befunge-93 is a language in which the code is presented not as a series of instructions, but as instructions scattered on a 2D plane; your pointer starts at the top-left corner and defaults to moving right through the code. Note that the instruction pointer wraps around the screen! There is a singular stack which we will assume is unbounded and only contain integers. While Befunge-93 code is supposed to be restricted to 80x25, you need not be concerned with code size. Befunge-93 supports the following instructions (from [Wikipedia](https://en.wikipedia.org/wiki/Befunge)):
    
| code     | action                                                                                                                                                                                  |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `0-9`    | Push this number onto the stack.                                                                                                                                                        |
| `+`      | Addition:<br/>Pop `a` and `b`, then push `a + b`.                                                                                                                                       |
| `-`      | Subtraction:<br/>Pop `a` and `b`, then push `b - a`.                                                                                                                                    |
| `*`      | Multiplication:<br/>Pop `a` and `b`, then push `a * b`.                                                                                                                                 |
| `/`      | Integer division:<br/>Pop `a` and `b`, then push `b / a`, rounded down.<br/>If `a` is `zero`, push `zero`.                                                                              |
| `%`      | Modulo:<br/>Pop `a` and `b`, then push the `b % a`.<br/>If `a` is zero, push `zero`.                                                                                                    |
| `!`      | Logical NOT:<br/>Pop `a` value. If the value is `zero`, push `1`; otherwise, push `zero`.                                                                                               |
| `&#96;`  | (backtick) Greater than:<br/>Pop `a` and `b`, if `b>a` then push `1`, otherwise push `zero`.                                                                                            |
| `>`      | Start moving `right`.                                                                                                                                                                   |
| `<`      | Start moving `left`.                                                                                                                                                                    |
| `^`      | Start moving `up`.                                                                                                                                                                      |
| `v`      | Start moving `down`.                                                                                                                                                                    |
| `?`      | Start moving in a random cardinal direction.                                                                                                                                            |
| `_`      | Pop `a`;<br/>if `value = 0` then move `right`, otherwise move `left`.                                                                                                                   |
| `&#124;` | Pop `a`;<br/>if `value = 0` then move `down`, otherwise move `up`.                                                                                                                      |
| `"`      | Start string mode:<br/>Push each character's ASCII value all the way up to the next `"`.                                                                                                |
| `:`      | Duplicate value on top of the stack.<br/>If there is nothing on top of the stack, push a `0`.                                                                                           |
| `\`      | Swap two values on top of the stack.<br/>If there is only one value, pretend there is an extra `0` on bottom of the stack.                                                              |
| `$`      | Pop value from the stack and discard it.                                                                                                                                                |
| `.`      | Pop value and output as an integer.                                                                                                                                                     |
| `,`      | Pop value and output the ASCII character represented by the integer code that is stored in the value.                                                                                   |
| `#`      | Trampoline:<br/>Skip next cell.                                                                                                                                                         |
| `p`      | A "put" call (a way to store a value for later use).<br/>Pop `y`, `x` and `v`, then change the character at the position `(x, y)` in the program to the character with ASCII value `v`. |
| `g`      | A "get" call (a way to retrieve data in storage).<br/>Pop `y` and `x`, then push ASCII value of the character at that position in the program.                                          |
| `@`      | End program.                                                                                                                                                                            |
| ` `      | (i.e. a space) No-op. Does nothing.                                                                                                                                                     |

The above list is slightly modified:
* you'll notice if you look at the Wikipedia page that we do not use the user input instructions and dividing by zero simply yields zero.

Here's an example:

    >987v>.v
    v456<  :
    >321 ^ _@

will create the output `123456789`.

So what you must do is create a function such that when you pass in the Befunge code, 
the function returns the output that would be generated by the code.

for example:

    "123456789".equals(new BefungeInterpreter().interpret(">987v>.v\nv456<  :\n>321 ^ _@")

This test case will be added for you.

## Reference
taken from https://www.codewars.com/kata/526c7b931666d07889000a3c