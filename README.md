# PE-69
https://projecteuler.net/problem=69

# Introduction
According to the problem statement, we must find n less than one million where n/phi(n) is the largest. The first approach to this solution involved using Python to calculate the answer. However, as will be shown later, the answer was infeasible to find through code alone.

# First attempt

My first attempt at the problem involved using code to calculate the solution through brute force. The code used is "PE_69"

# PE_69

This program consists of three functions: phi, coprime, and main. Main calls on phi, which calls on coprime.

# coprime

Let n be an integer and i be an integer less than n. For n and i to be coprime, the only common positive integer divisor between them must be 1

Coprime requires two inputs: an integer n and an integer i. The function returns either True or False. The function iterates from a starting integer j up to n. If both i and n are evenly divisible by j, then i and n cannot be coprime thus returning false. If the function never finds a j evenly divisible from n and i, then n and i must be coprime. Thus, the function returns True.

# phi

Phi requires a single input: an integer n. The function iterates through every positive integer i less than n and calls the coprime function. If the function returns True, the phi counter increments. The function returns the number of coprime integers, as is described by the definition of Euler's totient function in the problem description

# main
Main iterates through every n from 2 up to a determined integer. Ideally, this second integer would be 1,000,000, however, problems arose. Those problems will be detailed later. Main calls the phi function and assigns the value to its own phi. Main calculates an omega, defined by n/phi(n), and replaces the old value of omega if the new one is larger. If a larger one is found, the corresponding n and omega are printed.


# problems

The program executed perfectly for values of n less than 1000. With the great increase in the number of calculations for each incrementing n, the program required exponentially more time to operate. The program was left running for several minutes to find the answer for which n is less than 10,000, and was terminated due to inefficiency.

# Where to go?

While it could be possible to leave the program running so that an answer could be found, it was not feasible to do so. Instead, I opted to look for patterns based on current results to see if there were any ways to optimize the program. Upon observing the first 4 values of omega, a noticeable pattern emerged. 

|  n  | Omega |
|-----|-------|
|  2  |   2   |
|  6  |   3   |
| 30  |  3.75 |
|210  |4.375  |

Each subsequent n in the table is multiplied by the previous n and the next odd number. 2 * 3 = 6, 6 * 5 = 30, and 30 * 7 = 210. This pattern breaks with the next n, but a new one emerges.

|  n  | Omega |
|-----|-------|
|  2  |   2   |
|  6  |   3   |
| 30  |  3.75 |
|210  |4.375  |
|2310|4.8125|

The next n is multiplied by a factor of 11. This number clearly breaks the pattern, but there is still significance to it. 11 is prime! As are 3, 5, and 7. It can be concluded that to find the next largest omega, the previous n must be multiplied by the next prime number. We can test this by multiplying our current n by 13 and running the answer through a version of our program that will solely test that number. 

2310 * 13 = 30030

Upon
