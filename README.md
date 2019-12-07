solution for travelling salesman problem implemented with a tabu search metaheuristic.

sketch of algorithm:
	1. load parameters
	2. use greedy algorithm to generate a base solution
	3. init tabu matrix
	4. start a for loop
	5. generate all possible pair-wise swaps in solution vector and compute their objective function value
	6. pick the best possible swap out of legal swap possibilities as well as illegal swaps that satisfy aspiration criterion
	7. perform the swap and update dynamic memory structures
	8. end of for loop
	
	END IF:
	* for loop ends
	* for X last iterations of for loop (3.) the objective function value has not been optimized satisfyingly enough
	* terminational time has been reached

parameters:
	* X: int()
	* XValue being the value that swaping pairs of vertecies X times should decrease objective function value by
	* number of iterations during which banned pair remains in tabu matrix: int()
	* aspiration criterion value: float()
