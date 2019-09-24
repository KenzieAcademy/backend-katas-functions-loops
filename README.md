## Katas -- Functions and Loops

A kata is an individual exercise where you practice a programming skill through repetition. This kata focuses on Python loops and functions. The functions start out trivial, and ramp up in difficulty. The main goals of these katas are:

 - Gain familiarity with writing and calling functions that take arguments and return results
 - Decomposing a problem into the various parts of a for-loop
 - Familiarizing with VSCode built-in test suite 
 
You are provided a starter file named `main.py`, which contains an empty definition of each function. Complete each function so it prints the required result to the console. Unlike other katas we've done up until now, most of these build on each other, which means that you'll need to complete them in order.

### Add
Complete the function named `add` which takes two integers and returns their sum.
 - The function should handle negative values
 - Use built-in operators (+) is allowed.
 - Display the result of calling add(2, 4), which should be 6.

### Multiply
Complete the function named `multiply` which takes two integers and returns their product.
 - Use of built-in arithmetic operators or functions is NOT allowed.
 - Use a for-loop which calls the `add` function you wrote earlier.
 - This function must correctly handle negative values.
 - Display the result of calling `multiply(6, -8)`, which should be -48.

### Power
Write a function named `power` that takes two arguments (x and n) and returns the the result of raising x to the nth power.
 - Use of built-in arithmetic operators or functions is NOT allowed.
 - Use functions you wrote in earlier katas to write this function.
 - The function should correctly handle negative values of x (but not y).
 - Display the result of calling `power(2, 8)`, which should be 256.

Another word for this is "exponentiation". In the above example, we arrive at 256 by multiplying 2 by itself 8 times:

    2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 = 256

If we had called power(3, 4), we'd want to multiply 3 by itself 4 times:

    3 * 3 * 3 * 3 = 81

See [this Wikipedia article](https://simple.wikipedia.org/wiki/Exponentiation) for more details on exponentiation.

### Factorial
Write a function named `factorial` that takes a single argument and returns the factorial of that argument.
 - You may not use built-in arithmetic operators or functions.
 - Use functions you wrote in earlier katas to write this function.
 - Display the result of calling `factorial(4)`, which should be 24

    4 * 3 * 2 * 1 = 24

### Fibonacci
Write a function named `fibonacci` that takes an integer n and returns the [nth Fibonacci number](https://simple.wikipedia.org/wiki/Fibonacci_number).
 - You may not use built-in arithmetic operators or functions.
 - Use functions you wrote in earlier katas to write this function.
 - Display the result of calling `fibonacci(8)`, which should be 13:

    0 1 1 2 3 5 8 [13] 21

The number in brackets is the 8th fibonacci number.

### Hints
The answer to most of these will look similar. They will typically involve:
 - declaring a variable to keep track of a final result
 - writing a for loop to consistently modify the result
 - returning the result
 
If you struggle for more than 5 minutes, ask for help! This is an exercise in critical thinking, not torture.

### Testing
This assignment comes bundled with a "Test Suite" -- a set of tests to validate each function you write.  VSCode IDE has a built-in test runner framework.  Read [this article](https://code.visualstudio.com/docs/python/testing) about how to enable test discovery in your VSCode IDE.  You will need to know how to run similar tests in future assignments.

### PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account.
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
5. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.
