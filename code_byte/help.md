# TABLE OF CONTENTS

1. FUNCTIONS
    1. [SET POINTER](#0---set-pointer-position)
    2. [SET COLOR](#1---set-color)
    3. [SET VARIABLE (BYTE)](#2---set-variable-byte)

# FUNCTIONS

## 0 - SET POINTER POSITION

* takes 5 arguments
1. abs or rel/num or var
    * 0 absolute, number
    * 1 relative, number
    * 2 absolute, variable (integer)
    * 3 relative, variable (integer)
2. x coordinate, takes up two arguments
      * for numbers:
        * absolute is integer (0-63)
        * relative is signed byte (0-7)
        * first digit is sign: 1 = negative, 0 = positve
    * for variables:
        * byte is the variable number, variables work like numbers above
3. y coordinate, takes up two arguments
    * for numbers:
        * absolute is integer (0-63)
      * relative is signed byte (0-7)
        * first digit is sign: 1 = negative, 0 = positve
    * for variables:
       * byte is the variable number, variables work like numbers above

## 1 - SET COLOR

* takes 1 argument
1. list of colors:
    * 0 - Black
    * 1 - White
    * 2 - Red
    * 3 - Green
    * 4 - Blue
    * 5 - Yellow
    * 6 - Magenta
    * 7 - Cyan

## 2 - SET VARIABLE (BYTE)

* takes 3 arguments
1. which variable
2. there are four options
    * 0 - number
    * 1 - from byte variables
    * 2 - from integer variables
    * 3 - from pointer's color
3. based on options for argument 2
    * the number as a byte
    * the variable byte
    * the variable byte
    * nothing, but MUST be written

## 3 - SET VARIABLE (INTEGER)

* takes 4 arguments
1. which variable
2. there are six options
    * 0 - number
    * 1 - from byte variables
    * 2 - from integer variables
    * 3 - color
    * 4 - marker x
    * 5 - markey y
3. based on options for argument 2
    * the number as a integer
    * the variable byte (two digits)
    * the variable byte (two digits)
    * nothing, but MUST be written (two digits)
    * nothing, but MUST be written (two digits)
    * nothing, but MUST be written (two digits)