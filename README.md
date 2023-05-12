# Hamiltonian-Path-Approach
This was a Biology case study i have done with fellow members. Hamiltonian distance is a measure of the dissimilarity between two Hamiltonian cycles in a graph. It is defined as the minimum number of edges that must be traversed in order to transform one cycle into the other. This measure is particularly useful in the field of computational biology, where it can be used to compare different solutions to the Hamiltonian cycle problem, which is to find a cycle that visits every vertex in a graph exactly once.

<h2>Topological Sorting Algorithm</h2>
This is a Python script that implements the topological sorting algorithm on a directed acyclic graph. The algorithm takes an input file containing multiple graphs and returns a topologically sorted order for each graph if it exists, or -1 if the graph contains a cycle.

<h2>Input format</h2>
The input file should contain one or more graphs, where each graph is represented as follows:

The first line of each graph contains a single integer k (1 ≤ k ≤ 100), which represents the number of edges in the graph.
The next k lines each contain two integers u and v (1 ≤ u, v ≤ n), which represent an edge from vertex u to vertex v in the graph.
The last line of each graph contains two integers n (1 ≤ n ≤ 100) and m (1 ≤ m ≤ n), which represent the number of vertices in the graph and the number of edges, respectively.
<h2>Output format</h2>
For each graph in the input file, the script outputs either:

A line containing "1" followed by the vertices in a valid topologically sorted order separated by spaces, if such an order exists.
A line containing "-1" if the graph contains a cycle.
<h2>Usage</h2>
To use the script, simply update the "data" variable in the code to point to your input file and run the script. The output will be printed to the console.
<h2>Example</h2>
To run the script on an input file named "file.txt", simply update the "data" variable to point to the file and run the script. The output will be printed to the console.
