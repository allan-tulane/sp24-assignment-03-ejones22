# CMPS 2200 Assignment 3
## Answers

**Name:**___Emma Jones________


Place all written answers from `assignment-03.md` here for easier grading.

1a. Initial value of N is greatest val, where 2^k < N, then N - 2^k until N = 0

1b. The least amount of coins are used in every instance because the largest possible coin is selected in each iteration therefore the algorithm is optimal. 

1c. Work = O(log n), Span = O(log n)

2a. One counterexample is making N=14 if the denominations are 9, 7, 1. The the geometrica solution would yeild 1 9-coin and 5 1-coins for a total of 6 coins when the ideal solution is only 2 7-coins.

2b. The optimal substructure property is if an optimal solution can be constructed from optimal solutions of its subproblems. An optimal solution can be derived by reviewing the second highest denomination, in turn running every possible combination, including of course the optimal one.   

2c. A top-down solution for this specific problem could be creating an array for given N values and then finding the solution starting with both the first and second denomination, working down to lesser ones, which will yeild all possible outcomes. Then comparing the list to find the smallest value to return the optimal solution. Work: O(n), Span: O(n)

