# TRIAL EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
 - You can use any resource online, but **please work individually**
 - Instead of copy-pasting your answers and solutions, write them in your own words.


# Tasks
## 1-5. Complete the tasks seen in the 1-5.py files! (~90 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently with descriptive commit messages [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm used in exercise 2. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

I used a 'for' loop to solve exercise 2. In our case, the input was a string. So a for loop checks if the upcoming character in a string exists. If it does, it then checks if the conditions are met, in out case, checks if the character is equal to "a". If it is True, it adds one to a pre-defined variable named counter, and then returns to the beginning of the loop. If it's False, it doesn't do anything to the current character and returns to the beginning of the loop. While back at the beginning, it will move on to the second character in the string. It will continue to repeat the cycle until it once finds, that the next character in the string doesn't exist, therefore we have arrived at the end of our string. Then it breaks the loop and returns the counter.

![alt text](https://github.com/oliviaisarobot/trial-exam-python/blob/master/forloop.jpg?raw=true "For loop flowchart")

### How can you get a random number in python? [2p]
#### Your answer:

First you need to import the module called "random" in order to work with random numbers. Then you have multiple options to generate random numbers.
- random.randint(a, b) generates a random whole number between "a" and "b", whole numbers you have to specify.
- random.random() will generate a random float number that will always be between 0.0 and 1.0.
- random.uniform(a, b) is the combination of the previous two, it generates a random float number between "a" and "b", whole or float numbers you have to specify.
- random.randrange(a) will generate a random whole number between 0 and "a-1".
- random.randrange(a, b, c) will generate a random whole number between "a" and "b-1", by the step of "c". For example, f "c" is 2, it will only generate even numbers.
- random.choice([a, b, c]) will return a random element from a sequence we have to previously specify. The elements of the sequence can be either strings or integers.

### What does M stand for in MVC? [2p]
#### Your answer:

MVC stands for Model View Controller, which is a software design rule that separates the logic of the application from the database and the visual. The M or the Model handles all the data that the application works with. The Controller has a unidirectional communication with the model, which means that it can pull data and functions from the Model and it can also rewrite information that the Model stores. The Model can also contain exceptions and error handling.
