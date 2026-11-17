# Project Summary

## Introduction
I created a Classroom Timetable Generator using Python. The aim was to generate a weekly timetable automatically based on the subjects and their required periods.

## Working
The program takes the number of days, periods per day, and subject details from the user. It checks the total available periods and then generates a timetable by giving priority to subjects with more periods remaining.

It also ensures that a subject is not scheduled more than twice a day.

## Challenges Faced
While developing this project, I faced a few challenges:

**1. Managing subject periods**

It was challenging to distribute all subject periods across different days without exceeding the daily limit of two periods per subject.

*Solution:* I used a dictionary to keep track of the remaining periods of each subject and checked the daily limit before scheduling it.

**2. Selecting the correct subject**

Choosing which subject should be placed in the next available slot while following the given priority rule was a little confusing.

*Solution:* I compared the remaining periods of all subjects and selected the one with the highest count. The original order was maintained when two subjects had equal counts.

**3. Handling invalid inputs**

The program needed to handle cases where the total weekly periods did not match the available timetable slots or a subject required more than two periods in a day.

*Solution:* I added validation checks before generating the timetable to identify these conditions and display suitable error messages.

**4. Testing and debugging**

Getting the expected output for different input conditions required careful checking.

*Solution:* I tested the program using all four given test cases, including normal, minimum, invalid and different valid inputs, and corrected the issues found during testing.

### 3. Conclusion
This project helped me understand how to use Python lists and dictionaries to solve a scheduling problem. I also learned how to apply conditions, loops and input validation to build a program that follows specific constraints.
Solving these challenges helped me understand Python dictionaries, loops, conditions, and scheduling logic better.

## Learning
Through this project, I learned how to use Python lists, dictionaries, loops, and conditional statements to solve a practical problem.
