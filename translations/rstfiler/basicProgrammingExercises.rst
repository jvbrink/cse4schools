
Exercise 1
==========

1. Create a script that prints out the text “Hello, World!” to the
   screen.

2. Create a script that prints out the value of :math:`4\cdot5 + 2` to
   the screen. Do you get a different result if you write
   :math:`2 + 4\cdot5`?

3. Create a script that calculates :math:`2^{10}` and prints the result
   to the screen.

4. Create a script that calculates :math:`\sqrt 3` and prints the result
   to the screen. You will need to import the
   :math:`\verb+sqrt+`-command (squareroot) from pylab

Exercise 2
==========

To convert a temperature from degrees Celsius :math:`C`, to degrees
Fahrenheit :math:`F`, we use the following formula

.. math:: F = \frac{9}{5}C + 32.

1. Create a script that calculates the degrees Fahrenheit from a
   temperature given in degrees Celsius.

2. Use the script to find the degrees in Fahrenheit for the following
   temperatures: :math:`20^\circ`, :math:`0^\circ`, :math:`-40^\circ`.

Exercise 3
==========

1. Create a script where you save the first and last name of someone.
   Then print out a message for that person

2. Print the number of characters in the persons first and last name. To
   do this, you will need the command :math:`\verb+len(name)+`, which
   returns the length of a string, i.e. the number of characters. For
   example :math:`\verb+len("Jonas")+` returns 5.
3. Create a program that asks the user their name, and then prints a
   message that includes the name they gave.

Exercise 4
==========

1. Ask the user for 5 adjectives and store them in 5 different
   variables. **Hint:** an adjective is a describing word.
2. Test your program by printing all five words.
3. Write a “fill in the blank” adjective story, and print it so that the
   5 adjectives the user gave is included in the story.
4. Test your program.
5. If everything is working correctly, you can now hide your editor and
   run the program. Then get a friend to supply the adjectives!

Exercise 5
==========

Find the mistakes in the following programs (there is one mistake per
program). Try to fix the programs so they work correctly

1. 

.. sagecellserver:: python

    name = Per 
    print "Hi there %s!" % name

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-523dbd3675c8> in <module>()
    ----> 1 name = Per
          2 print "Hi there %s!" % name
    

    NameError: name 'Per' is not defined


2. 

.. sagecellserver:: python

    x = 24
    y = 36
    print X + y

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-e29de7b657e0> in <module>()
          1 x = 24
          2 y = 36
    ----> 3 print X + y
    

    NameError: name 'X' is not defined


3. 

.. sagecellserver:: python

    def greet(name)
    	print "Hi there %s" % name

::


      File "<ipython-input-3-eed0d26049d9>", line 1
        def greet(name)
                       ^
    SyntaxError: invalid syntax
    


4. 

.. sagecellserver:: python

    location = "Oslo"
    temperature = -18
    print "The temperature in %s is now %i" (location, temperature)

::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-19a9da1b564d> in <module>()
          1 location = "Oslo"
          2 temperature = -18
    ----> 3 print "The temperature in %s is now %i" (location, temperature)
    

    TypeError: 'str' object is not callable


5. 

.. sagecellserver:: python

    def double(x):
    	result = 2*x
    
    print double(2)

.. parsed-literal::

    None
    

6. 

.. sagecellserver:: python

    def greet(name):
    print "Hi there %s" % name
    greet("Mary")

::


      File "<ipython-input-8-b79ce41c3cec>", line 2
        print "Hi there %s" % name
            ^
    IndentationError: expected an indented block
    


Exercise 6
==========

1. Define a function :math:`\verb+celcius_to_fahrenheit+` which takes
   degrees C as input and returns the corresponding degrees Fahrenheit.
   Remember that the formula for converting from Celsius to Fahrenheit
   is :math:`F = \frac{9}{5}C + 32.`

2. Use the function to find the degrees in Fahrenheit for the following
   temperatures: :math:`20^\circ`, :math:`0^\circ`, :math:`-40^\circ`.

3. Write a loop where you iterate through the degrees in C from
   :math:`-100` up to :math:`100`, and use your function to print out
   the corresponding degrees Fahrenheit. **Hint 1:** Use the
   :math:`\verb+range+` function. **Hint 2:** You have to call your
   function inside the loop.

Exercise 7
==========

1. Write a script where you save the first name of someone. Then you
   print out a greeting if the name equals your name.
2. Define a function that takes a number, x, as input and returns 2\*x
   if the input is positive. If the number is negative it should just
   return 0.

Exercise 8
==========

Now we will use the :math:`\verb+range+` together with loops to
calculate some mathematical sums.

1. Calculate the sum of all odd numbers below zero

2. Calculate the sum of all square numbers up to and including 10000.
   **Hint:** We want the sum

.. math:: 1 + 4 + 9 + 16 + \ldots + 10000 = \sum_{i=1}^{100} i^2.

3. Calculate the sum of the infinite series

.. math:: 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \ldots

**Hint:** Every term in the sum is smaller than the last, and so
eventually the terms are really small. So it is sufficient to consider
the first 1000 terms, because the terms after this will contribute very
little to the final result.

Exercise 9
==========

Use the function :math:`\verb!randint!` to simulate rolling the
following dice:

1. One six sided die
2. One 20 sided die
3. Three six sided dice
4. Three coins

Exercise 10
===========

1. Write a :math:`\verb+while+` loop that keeps flipping a coin until
   you get tails a total of 5 times.
2. Write a :math:`\verb+while+` loop that flips a coin 10 times and
   prints the number of tails you get.
3. Write a :math:`\verb+for+` loop that flips a coin 10 times and prints
   the number of tails you get.

Exercise 11
===========

1. Write a program that draws a random number between 1 and 100
2. Expand your program so that it asks the user to guess the number.
   Print a message to tell the user if their guess was right or wrong.
3. Change the program so that the user knows if they guessed too high or
   too low if they missed.
4. Expand your program again with a :math:`\verb!while!` loop that keeps
   asking the user to guess until they guess correctly. For each guess
   tell the user if they guessed too high or too low.

Exercise 12
===========

We will now create a simple version of the card game war. You should do
this step by step and test you code between each step

1. Implement a deck of cards as a list.
2. Change your program to include two decks, one for you and one for
   your opponent. Shuffle both decks with :math:`\verb!shuffle()!` from
   the :math:`\verb!random!` library.
3. Define a function named battle. Have the function use
   :math:`\verb!pop!` to remove the top cards from both decks and then
   print them to the screen.
4. Expand your function so that it checks which card 'beats' the other
   by comparing their symbol. You have to be creative with your
   :math:`\verb!if!` tests to find the 'highest' card.
5. Have you function put both cars back in the winners deck and shuffle
   both decks.
6. If both your cards are equally good, war begins. Define a function,
   war, that pops 3 cards from both decks, and then compares the third
   card from both decks. Give all cards to the winner.
7. Create a :math:`\verb!while!` loop that continues the game until you
   or your opponent is out of cards. For every iteration you should use
   :math:`\verb!raw_input()!` so that the user can press enter to play
   again.
8. Make you program nicer. You can for example print a longer message at
   the beginning of the game. And you can create a nice message after
   every battle to explain which cards where shown and what the result
   of the battle was. Clean up your code to make it pretty and
   organized.

Exercise 13
===========

1. Plot :math:`e^x` for :math:`x\in[0,2]`
2. Create a plot to show the following three functions:

   .. math:: e^x, \qquad e^{-x}, \qquad 1/e^{x}.

   You will need the :math:`\verb+axis+` command to select reasonable
   axis for you figure.
3. Make your plot look nicer with the functions :math:`\verb+axis+`,
   :math:`\verb+xlabel+`, :math:`\verb+legend+`, :math:`\verb+title+`
   and :math:`\verb+grid+.`
4. Save your plot as a .pdf file and as a .png file. Make sure that the
   files are saved correctly,and that they look the way you expect.

Exercise 14 (Challenging!)
==========================

A prime number is a number that is only divisible by itself and 1. The
first 10 prime numbers are

.. math:: 2,3,5,7,11,13,17,19,23,29.

1. Define a function that takes a number :math:`n` as input and then
   checks if it is a prime number. The function should return
   :math:`\verb+True+` if :math:`n` is a prime number, and
   :math:`\verb+False+` if it is not.
2. Use your function to write all prime numbers below 1000. To make sure
   your program is correct, you can check if it found 168 prime numbers.

Exercise 15 (Challenging!)
==========================

The Fibonacci numbers begin like this

.. math:: 1,1,2,3,5,8,13,21,34,55,89,144,...

Observe that we find the next number in the sequence by adding the
previous two numbers. So the next number is 89 + 144 = 233. More
mathematically, we can say that the :math:`n`\ th Fibonacci number is
given by

.. math::  F_n = F_{n-1} + F_{n-2}

With :math:`F_1 = 1` and :math:`F_2 = 1`

1. Define a function that takes n as an argument and returns the
   :math:`n`\ th Fibonacci number.
2. Use your function to print the first 50 Fibonacci numbers.


