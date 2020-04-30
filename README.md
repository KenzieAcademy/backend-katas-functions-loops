# Functions and Loops

This exercise focuses on Python loops and functions. The functions start out trivial, and ramp up in difficulty. The main goals of these exercises are:

 - Gain familiarity with writing and calling functions that take arguments and return results
 - Decompose a problem into the various parts of a for-loop
 - Familiarize with VS Code built-in test suite 
 
You are provided a starter file named `main.py`, which contains an empty definition of each function. Complete each function so that it prints the required result to the console. Most of these build on each other, which means that you'll need to complete them in order.

### Add
Complete the function named `add` which takes two integers and returns their sum.
 - The function should handle negative values
 - Use of built-in operator `+` is allowed
 - Display the result of calling add(2, 4), which should be 6

### Multiply
Complete the function named `multiply` which takes two integers and returns their product.
 - Use of built-in operator `-` and the `abs()` function is allowed
 - Use of all other built-in arithmetic operators or functions is __not__ allowed (e.g. `*`, `**`, `+`, `/`, `//`, `sum()`, etc.)
 - Use a for-loop which calls the `add()` function you wrote earlier
 - This function must correctly handle negative values
 - Display the result of calling `multiply(6, -8)`, which should be -48

### Power
Write a function named `power` that takes two arguments (x and n) and returns the the result of raising x to the nth power.
 - Use of built-in arithmetic operators or functions is __not__ allowed
 - Use the functions you wrote in the previous exercises to write this function
 - The function should correctly handle negative values of x (but not y)
 - Display the result of calling `power(2, 8)`, which should be 256

Another word for this is *exponentiation*. In the above example, we arrive at 256 by multiplying 2 by itself 8 times:

    2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 = 256

If we had called power(3, 4), we'd want to multiply 3 by itself 4 times:

    3 * 3 * 3 * 3 = 81

See [this Wikipedia article](https://simple.wikipedia.org/wiki/Exponentiation) for more details on exponentiation.

### Factorial
Write a function named `factorial` that takes a single argument and returns the factorial of that argument.
 - You may __not__ use built-in arithmetic operators or functions
 - Use the functions you wrote in the previous exercises to write this function
 - Display the result of calling `factorial(4)`, which should be 24

    4 * 3 * 2 * 1 = 24

### Fibonacci
Write a function named `fibonacci` that takes an integer `n` and returns the [nth Fibonacci number](https://simple.wikipedia.org/wiki/Fibonacci_number). For the purposes of this assignment, we'll be using the _classical_ series, which starts counting at 0, rather than the _combinatorial_ series, which starts counting at 1.
 - You may not use built-in arithmetic operators or functions
 - Use the functions you wrote in the previous exercises to write this function
 - Display the result of calling `fibonacci(8)`, which should be 21

    `0 1 1 2 3 5 8 13 [21] ...`

The number in brackets is the 8th fibonacci number, if we start counting terms from 0 instead of 1.

### Hints
The answer to most of these will look similar. They will typically involve:
 - declaring a variable to keep track of a final result
 - writing a for loop to consistently modify the result
 - returning the result
 
If you struggle for more than 5 minutes, ask for help! This is an exercise in critical thinking, not torture.

### Testing
This assignment comes bundled with a "Test Suite" &mdash; a set of tests to validate each function you write. VS Code has a built-in test runner framework. Read [this article](https://code.visualstudio.com/docs/python/testing) about how to enable test discovery in VS Code. You will need to know how to run similar tests in future assignments.

## PR (Pull Request) Workflow for this assignment
1. *Fork* this repository into your own personal GitHub account.
2. *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev` and checkout the branch.
5. Commit your changes, then `git push` the branch back to your own GitHub account.
5. From your own GitHub repo, create a pull request (PR) *from your `dev` branch back to **your own** master*.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline within your pull request in your GitHub account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes. This is the code review iteration cycle.
