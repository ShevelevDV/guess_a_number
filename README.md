# Project 0. Guess a number

## Description of the task
The algorithm should set a random integer number in a range set by user and try to guess it. The algorithm should  guess the number in less than 20 tries for a range from 1 to 100.

## Approach to solution
To guess the number the algorith randomly selects a random integer number and compares to the set number it is trying to guess. If the number is not guessed and the selected number is lower than the set number it is trying to guess, then the selected number becomes the lower boundary of the range in which the search is performed. If the selected number is higher than the set number it is trying to guess, then the selected number becomes the higher boundary of the range in which the search is performed. The cycle is repeated untill the set number is guessed. 

The efficiency on the algorithms for a range from 1 to 100 estimated over 10000 runs is around 8 tries. 