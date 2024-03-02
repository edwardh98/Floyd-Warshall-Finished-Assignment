# Floyd-Warshall-Finished-Assignment
Assignment for University - Finished Version

Floyd's Algorithm - Recursive Implementation This project explores a recursive implementation of Floyd's algorithm for finding all-pairs shortest paths in a weighted graph. It includes a unit test, performance analysis, and a comparison against an iterative implementation.

Project Structure 
src/floyd_warshall.py: Contains the recursive implementation of Floyd's algorithm. 
tests/test_floyd_warshall.py: Houses unit tests to verify the implementation's correctness. 
requirements.txt: Lists project dependencies.
individual_report.pdf: Finished report/ analysis 

Installation Clone the repository:
Bash git clone https://github.com/edwardh98/floyd-warshall-finished-assignment

Install dependencies:
Bash pip install -r requirements.txt

Usage Run the algorithm: 
Python from src.floyd_warshall import floyd_warshall_recursive

Replace the following:
graph = [ [0, 3, 8, float('inf')], [float('inf'), 0, float('inf'), 1], [float('inf'), 4, 0, float('inf')], [2, float('inf'), -5, 0] ] n = len(graph) distance_matrix = floyd_warshall_recursive(graph, n) print(distance_matrix)

Testing Run unit tests:
Bash pytest

The individual_report.pdf file contains:
A detailed explanation of the recursive and iterative implementation. Testing strategy and coverage discussion. Performance analysis and hypothesis on differences between recursive and iterative versions.
